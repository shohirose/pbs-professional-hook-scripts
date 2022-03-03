import sys

if sys.platform == 'linux' and '/usr/lib64/python3.6' not in sys.path:
    sys.path.append('/usr/lib64/python3.6')

import pbs

try:
    """Main Hook Script"""
    pass

except SystemExit:
    pass

except Exception as err:
    event = pbs.event()
    try:
        from traceback import TracebackException
        msg = list(TracebackException.from_exception(err).format())
        event.reject(f'{event.hook_name} hook failed: {msg}')
    except ModuleNotFoundError:
        event.reject(f'{event.hook_name} hook failed: {err}')
