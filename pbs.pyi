from enum import Enum
from typing import Any, Dict, Tuple, List, Iterable


class _JobState(Enum):
    BEGUN = 1
    EXITING = 2
    EXPIRED = 3
    FINISHED = 4
    HELD = 5
    MOVED = 6
    QUEUED = 7
    RUNNING = 8
    SUSPEND = 9
    SUSPEND_USERACTIVE = 10
    TRANSIT = 11
    WAITING = 12


JOB_STATE_BEGUN = _JobState.BEGUN
JOB_STATE_EXITING = _JobState.EXITING
JOB_STATE_EXPIRED = _JobState.EXPIRED
JOB_STATE_FINISHED = _JobState.FINISHED
JOB_STATE_HELD = _JobState.HELD
JOB_STATE_MOVED = _JobState.MOVED
JOB_STATE_QUEUED = _JobState.QUEUED
JOB_STATE_RUNNING = _JobState.RUNNING
JOB_STATE_SUSPEND = _JobState.SUSPEND
JOB_STATE_SUSPEND_USERACTIVE = _JobState.SUSPEND_USERACTIVE
JOB_STATE_TRANSIT = _JobState.TRANSIT
JOB_STATE_WAITING = _JobState.WAITING


class _QueueType(Enum):
    EXECUTION = 1
    ROUTE = 2


QTYPE_EXECUTION = _QueueType.EXECUTION
QTYPE_ROUTE = _QueueType.ROUTE


class _VnodeType(Enum):
    PBS = 1


ND_PBS = _VnodeType.PBS


class _VnodeSharingType(Enum):
    DEFAULT_EXCL = 1
    DEFAULT_EXCLHOST = 2
    DEFAULT_SHARED = 3
    FORCE_EXCL = 4
    FORCE_EXCLHOST = 5
    IGNORE_EXCL = 6


ND_DEFAULT_EXCL = _VnodeSharingType.DEFAULT_EXCL
ND_DEFAULT_EXCLHOST = _VnodeSharingType.DEFAULT_EXCLHOST
ND_DEFAULT_SHARED = _VnodeSharingType.DEFAULT_SHARED
ND_FORCE_EXCL = _VnodeSharingType.FORCE_EXCL
ND_FORCE_EXCLHOST = _VnodeSharingType.FORCE_EXCLHOST
ND_IGNORE_EXCL = _VnodeSharingType.IGNORE_EXCL


class _VnodeState(Enum):
    BUSY = 1
    DOWN = 2
    FREE = 3
    JOBBUSY = 4
    JOB_EXCLUSIVE = 5
    OFFLINE = 6
    PROV = 7
    RESV_EXCLUSIVE = 8
    STALE = 9
    STATE_UNKNOWN = 10
    UNRESOLVABLE = 11
    WAIT_PROV = 12


ND_BUSY = _VnodeState.BUSY
ND_DOWN = _VnodeState.DOWN
ND_FREE = _VnodeState.FREE
ND_JOBBUSY = _VnodeState.JOBBUSY
ND_JOB_EXCLUSIVE = _VnodeState.JOB_EXCLUSIVE
ND_OFFLINE = _VnodeState.OFFLINE
ND_PROV = _VnodeState.PROV
ND_RESV_EXCLUSIVE = _VnodeState.RESV_EXCLUSIVE
ND_STALE = _VnodeState.STALE
ND_STATE_UNKNOWN = _VnodeState.STATE_UNKNOWN
ND_UNRESOLVABLE = _VnodeState.UNRESOLVABLE
ND_WAIT_PROV = _VnodeState.WAIT_PROV


class _EventType(Enum):
    RESVSUB = 1
    RESV_END = 2
    QUEUEJOB = 3
    MODIFYJOB = 4
    MOVEJOB = 5
    RUNJOB = 6
    PERIODIC = 7
    EXECJOB_BEGIN = 8
    EXECJOB_PROLOGUE = 9
    EXECJOB_LAUNCH = 10
    EXECJOB_ATTACH = 11
    EXECJOB_PRESUME = 12
    EXECJOB_PRETERM = 13
    EXECJOB_EPILOGUE = 14
    EXECJOB_END = 15
    EXECHOST_STARTUP = 16
    EXECHOST_PERIODIC = 17


RESVSUB = _EventType.RESVSUB
RESV_END = _EventType.RESV_END
QUEUEJOB = _EventType.QUEUEJOB
MODIFYJOB = _EventType.MODIFYJOB
MOVEJOB = _EventType.MOVEJOB
RUNJOB = _EventType.RUNJOB
PERIODIC = _EventType.PERIODIC
EXECJOB_BEGIN = _EventType.EXECJOB_BEGIN
EXECJOB_PROLOGUE = _EventType.EXECJOB_PROLOGUE
EXECJOB_LAUNCH = _EventType.EXECJOB_LAUNCH
EXECJOB_ATTACH = _EventType.EXECJOB_ATTACH
EXECJOB_PRESUME = _EventType.EXECJOB_PRESUME
EXECJOB_PRETERM = _EventType.EXECJOB_PRETERM
EXECJOB_EPILOGUE = _EventType.EXECJOB_EPILOGUE
EXECJOB_END = _EventType.EXECJOB_END
EXECHOST_STARTUP = _EventType.EXECHOST_STARTUP
EXECHOST_PERIODIC = _EventType.EXECHOST_PERIODIC


class _ServerState(Enum):
    IDLE = 1
    ACTIVE = 2
    HOT = 3
    SHUTDEL = 4
    SHUTIMM = 5
    SHUTSIG = 6


SV_STATE_IDLE = _ServerState.IDLE
SV_STATE_ACTIVE = _ServerState.ACTIVE
SV_STATE_HOT = _ServerState.HOT
SV_STATE_SHUTDEL = _ServerState.SHUTDEL
SV_STATE_SHUTIMM = _ServerState.SHUTIMM
SV_STATE_SHUTSIG = _ServerState.SHUTSIG


class _ResvState(Enum):
    NONE = 1
    UNCONFIRMED = 2
    CONFIRMED = 3
    WAIT = 4
    TIME_TO_RUN = 5
    RUNNING = 6
    FINISHED = 7
    BEING_ALTERED = 8
    BEING_DELETED = 9
    DELETED = 10
    DELETING_JOBS = 11
    DEGRADED = 12
    IN_CONFLICT = 13


RESV_STATE_NONE = _ResvState.NONE
RESV_STATE_UNCONFIRMED = _ResvState.UNCONFIRMED
RESV_STATE_CONFIRMED = _ResvState.CONFIRMED
RESV_STATE_WAIT = _ResvState.WAIT
RESV_STATE_TIME_TO_RUN = _ResvState.TIME_TO_RUN
RESV_STATE_RUNNING = _ResvState.RUNNING
RESV_STATE_FINISHED = _ResvState.FINISHED
RESV_STATE_BEING_ALTERD = _ResvState.BEING_ALTERED
RESV_STATE_BEING_DELETED = _ResvState.BEING_DELETED
RESV_STATE_DELETED = _ResvState.DELETED
RESV_STATE_DELETING_JOBS = _ResvState.DELETING_JOBS
RESV_STATE_DEGRADED = _ResvState.DEGRADED
RESV_STATE_IN_CONFLICT = _ResvState.IN_CONFLICT


class _LogLevel(Enum):
    DEBUG = 1
    WARNING = 2
    ERROR = 3


LOG_DEBUG = _LogLevel.DEBUG
LOG_WARNING = _LogLevel.WARNING
LOG_ERROR = _LogLevel.ERROR


class _Duration:

    def __init__(self):
        pass

    def __add__(self, other: _Duration | int | float) -> _Duration: ...

    def __radd__(self, other: _Duration | int | float) -> _Duration: ...


def duration(t: int | float | str | _Duration) -> _Duration: ...


class _CheckpointType:
    pass


def checkpoint(cp: str) -> _CheckpointType: ...


class _DependType:
    pass


def depend(dp: str) -> _DependType: ...


class _EmailList:
    pass


def email_list(emails: str) -> _EmailList: ...


class _ExecHost:
    pass


def exec_host(host: str) -> _ExecHost: ...


class _GroupList:
    pass


def group_list(groups: str) -> _GroupList: ...


class _HoldTypes:
    pass


def hold_types(htypes: str) -> _HoldTypes: ...


class _JoinPath:
    pass


def join_path(path: str) -> _JoinPath: ...


class _KeepFiles:
    pass


def keep_files(option: str) -> _KeepFiles: ...


class _LicenseCount:
    pass


def license_count(lic: str) -> _LicenseCount: ...


class _MailPoints:
    pass


def mail_points(mpts: str) -> _MailPoints: ...


class _NodeGroupKey:
    pass


def node_group_key(resources: str) -> _NodeGroupKey: ...


class _PathList:
    pass


def path_list(paths: str) -> _PathList: ...


class _Env:
    pass


def pbs_env() -> _Env: ...


def pbs_resource(res_list_name: str) -> Dict[str, Any]: ...


class _StagingList:
    pass


def staging_list(filespecs: str) -> _StagingList: ...


class _UserList:
    pass


def user_list(users: str) -> _UserList: ...


class _Job:

    def __init__(self):
        self.__id: str = ...
        self.array_indices_submitted: range = ...
        self.Checkpoint: _CheckpointType = ...
        self.depend: _DependType = ...
        self.Execution_Time: _Duration = ...
        self.Exit_status: int = ...
        self.exec_host: _ExecHost = ...
        self.exec_vnode: _ExecVnode = ...
        self.group_list: _GroupList = ...
        self.Hold_Types: _HoldTypes = ...
        self.job_state: _JobState = ...
        self.Join_Path: _JoinPath = ...
        self.Keep_Files: _KeepFiles = ...
        self.Mail_Points: _MailPoints = ...
        self.Mail_Users: _EmailList = ...
        self.queue: _Queue = ...
        self.Resource_List: Dict[str, Any] = ...
        self.resources_used: Dict[str, Any] = ...
        self.run_count: int = ...
        self.stagein: _StagingList = ...
        self.sgateout: _StagingList = ...
        self.User_List: _UserList = ...
        self.Variable_List: Dict[str, Any] = ...
        self.Join_Path: _JoinPath = ...
        self.Shell_Path_List: _PathList = ...
        self.interactive: bool = ...

    @property
    def id(self) -> str:
        pass

    def is_checkpointed(self) -> bool: ...

    def is_ms_mom(self) -> bool: ...

    def delete(self) -> None: ...

    def release_nodes(self, keep_select) -> None: ...

    def rerun(self) -> None: ...


class _ExecVnode:

    def __init__(self):
        self.__chunks: List[_Chunk] = ...

    @property
    def chunks(self) -> List:
        pass


class _Chunk:

    def __init__(self):
        self.vnode_name: str = ...
        self.chunk_resources: Dict[str, Any] = ...



def exec_vnode(node: str) -> _ExecVnode: ...


class _Queue:

    def __init__(self):
        self.__name: str = ...
        self.Priority = ...
        self.queue_type: _QueueType = ...

    def job(self, id: int) -> _Job: ...

    def jobs(self) -> Iterable[_Job]: ...

    @property
    def name(self) -> str:
        pass


class _Vnode:

    def __init__(self):
        self.topology_info: str = ...
        self.state: _VnodeState = ...
        self.sharing: _VnodeSharingType = ...
        self.ntype: _VnodeType = ...


class _Event:

    def __init__(self):
        self.alarm: int = ...
        self.argv: List[str] = ...
        self.debug: bool = ...
        self.enabled: bool = ...
        self.env: Dict[str, Any] = ...
        self.fail_action = ...
        self.freq = ...
        self.hook_name: str = ...
        self.hook_type: str = ...
        self.job: _Job = ...
        self.job_list: Dict[str, _Job] = ...
        self.job_o: _Job = ...
        self.order = ...
        self.pid: int = ...
        self.progname: str = ...
        self.requestor: str = ...
        self.requestor_host: str = ...
        self.resv: _Resv = ...
        self.src_queue: _Queue = ...
        self.type: _EventType = ...
        self.user: str = ...
        self.vnode_list: Dict[str, _Vnode] = ...
        self.vnode_list_fail: Dict[str, _Vnode] = ...

    def accept(self, msg: str) -> None: ...

    def reject(self, error_msg: str = "", error_code: int = None) -> None: ...


class _Resv:

    def __init__(self):
        self.__resvid: str = ...
        self.Reserve_Owner = ...
        self.Reserve_Name: str = ...
        self.reserve_state: _ResvState = ...

    @property
    def resvid(self) -> str:
        pass


class _Server:

    def __init__(self):
        self.__name: str = ...
        self.server_state: _ServerState = ...
        self.pbs_license_min: Any = ...
        self.default_queue: str = ...

    @property
    def name(self) -> str:
        pass

    def job(self, id: int) -> _Job: ...

    def jobs(self) -> Iterable[_Job]: ...

    def queue(self, name: str) -> _Queue: ...

    def queues(self) -> Iterable[_Queue]: ...

    def resv(self, id: int) -> _Resv: ...

    def resvs(self) -> Iterable[_Resv]: ...

    def scheduler_restart_cycle(self) -> None: ...

    def vnode(self, name: str) -> _Vnode: ...

    def vnodes(self) -> List[_Vnode]: ...


def logmsg(level: _LogLevel, msg: str) -> None: ...


def event() -> _Event: ...


def server() -> _Server: ...


hook_config_filename: str | None

pbs_conf: Dict[str, Any]
