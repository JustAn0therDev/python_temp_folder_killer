#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

import sys, os, traceback, types

def isUserAdmin():

    if os.name == 'nt':
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getpid() == 0
    else:
        raise RuntimeError("Unsupported operating system for this module: %s" % (os.name))

def runAsAdmin(cmdLine=None, wait=True):

    if os.name != 'nt':
        raise RuntimeError("This function is only implemented on Windows.")

    import win32api, win32con, win32event, win32process

    python_exe = sys.executable

    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (isinstance(cmdLine, list), isinstance(cmdLine, tuple)):
        raise ValueError("cmdLine is not a sequence.")
    cmd = '"%s"' % (cmdLine[0],)
    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    showCmd = win32con.SW_SHOWNORMAL
    lpVerb = 'runas' 

    procInfo = win32api.shell.ShellExecuteEx(nShow=showCmd,
                              fMask=win32api.shell.shell.shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmd,
                              lpParameters=params)

    if wait:
        procHandle = procInfo['hProcess']    
        win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
    else:
        rc = None

    return rc

def test():
    rc = 0
    if not isUserAdmin():
        print("You're not an admin.", os.getpid(), "params: ", sys.argv)
        rc = runAsAdmin()
    else:
        print("You are an admin!", os.getpid(), "params: ", sys.argv)
        rc = 0
    input('Press Enter to exit.')
    return rc


if __name__ == "__main__":
    sys.exit(test())