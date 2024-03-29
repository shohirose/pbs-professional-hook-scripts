import sys
import re
import time
import os

# RHEL 7.x supports Python 3.6
if sys.platform == 'linux' and '/usr/lib64/python3.6' not in sys.path:
    sys.path.append('/usr/lib64/python3.6')

import pbs
import subprocess as sp
from pathlib import Path
import json
from typing import Dict, Tuple
from traceback import TracebackException


class FlexlmLicenseManager:
    """Flexlm license manager

    Attributes:
        lmutil (pathlib.Path): Absolute path to lmutil
        servers (list[str]): License servers
        daemon (str): License daemon
        timeout (int): Time out in seconds for a license query
        encoding (str): Encoding for stdout and stderr
    """

    def __init__(self, lmutil: Path, server: str, daemon: str, timeout: int = 5, encoding: str = "utf-8"):
        self.lmutil = lmutil
        self.server = server
        self.daemon = daemon
        self.timeout = timeout
        self.encoding = encoding

    @staticmethod
    def parse_query(lines: str, feature: str) -> Tuple[int, int]:
        """Parse a license query result.

        Args:
            lines (str): standard output of a license query
            feature (str): license feature name

        Returns:
            Tuple[int, int]: The number of issued and used license features

        Raises:
            ValueError: If the license feature is not found.
        """
        regex = re.compile(
            f'Users of {feature}:  \(Total of (\d+) licenses?? issued;  Total of (\d+) licenses?? in use\)')
        m = regex.search(lines)

        if not m:
            raise ValueError(
                f'License feature is not found: {feature}')

        issued = int(m.group(1))
        used = int(m.group(2))
        return issued, used

    def get_license_nums(self, feature: str) -> Tuple[int, int]:
        """Get the number of issued and used license features,

        Args:
            feature (str): license feature name

        Returns:
            Tuple[int, int]: The number of issued and used license features

        Raises:
            ValueError: If the license feature is not found.
            subprocess.TimeoutExpired: If timeout happened.
            subprocess.CalledProcessError: If a called process failed.
        """
        cmd = [str(self.lmutil), 'lmstat', '-c', self.server,
               '-f', feature, '-S', self.daemon]
        result = sp.run(cmd, stdout=sp.PIPE, stderr=sp.PIPE,
                        encoding=self.encoding, timeout=self.timeout, check=True)
        return self.parse_query(result.stdout, feature)


class HookConfig:
    """Hook configuration

    Attributes:
        resources (dict[str, str]): Resource names of each license feature
        lmutil (Path): Path to lmutil command
        license_server (str): License server
        license_daemon (str): License daemon
        stamp_file (Path): Path to the time stamp file. Default path is "/tmp/flexlm_stamp.txt".
        interval_time (float): (optional) Interval time in seconds between license checks. Default is 10 seconds.
        delaying_time (float): (optional) Delaying time in seconds when licenses are not available. Default is 60 seconds.
    """

    def __init__(self, config_file: Path):
        """
        Args:
            config_file (Path): Path to the config file in JSON format
        """
        with open(config_file, mode="r") as f:
            j = json.load(f)
            self.resources: Dict[str, str] = j["resources"]
            self.lmutil = Path(j["lmutil"])
            self.license_server: str = j["license_server"]
            self.license_dameon: str = j["license_daemon"]
            self.stamp_file = Path(
                j.get("stamp_file", "/tmp/flexlm_stamp.txt"))
            self.interval_time: float = j.get("interval_time", 10.0)
            self.delaying_time: float = j.get("delaying_time", 60.0)


try:
    """Main Hook Script"""
    event = pbs.event()
    job = event.job

    config = HookConfig(Path(pbs.hook_config_filename))
    resources = dict(
        filter(lambda x: x[1] in job.Resource_List, config.resources.items()))

    # Do not apply this hook if resources are not found.
    if not resources:
        sys.exit()

    # Check if enough time has passed to avoid the racing condition for a license query.
    if config.stamp_file.exists():
        elapsed_time = time.time() - os.stat(config.stamp_file).st_mtime
        if elapsed_time < config.interval_time:
            job.Execution_Time = pbs.duration(
                time.time() + config.interval_time - elapsed_time)
            event.reject(
                "Too little time passed from the last run. Delaying the job.")

    flexlm = FlexlmLicenseManager(
        lmutil=config.lmutil, server=config.license_server, daemon=config.license_dameon)

    for feature, resource in resources.items():
        required_num = job.Resource_List[resource]        
        issued_num, used_num = flexlm.get_license_nums(feature)
        if issued_num == 0:
            event.reject(f"License '{feature}' is not issued.")
        available_num = issued_num - used_num
        if available_num < required_num:
            job.Execution_Time = pbs.duration(
                time.time() + config.delaying_time)
            event.reject(
                f"License '{feature}' is not available. Delaying the job.")

    with open(config.stamp_file, mode="w") as f:
        f.write("Check")

    event.accept("Licenses are available. Accepting the job.")

except SystemExit:
    pass

except (ValueError, sp.TimeoutExpired, sp.CalledProcessError) as err:
    event.reject(f"{event.hook_name} hook failed: {err}")

except Exception as err:
    event = pbs.event()
    msg = list(TracebackException.from_exception(err).format())
    event.reject(f"{event.hook_name} hook failed: {msg}")
