import sys, os

if sys.platform == 'linux' and '/usr/lib64/python3.6' not in sys.path:
    sys.path.append('/usr/lib64/python3.6')

import pbs
from traceback import TracebackException

try:
    """Main Hook Script"""
    pass

except SystemExit:
    pass

except Exception as err:
    msg = list(TracebackException.from_exception(err).format())
    event = pbs.event()
    event.reject(f'{event.hook_name} hook failed: {msg}')