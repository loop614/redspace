from __future__ import annotations

reddebugflag: bool = False


def turnLoggerOn():
    global reddebugflag
    reddebugflag = True


def redlog(*args, force: bool = False):
    if reddebugflag or force:
        print(*args)
