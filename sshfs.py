"""
============================================================================
Name        : sshfsmount.py
Author      : Derek Bixler
Version     : 0.1
Description : Simple interface for mounting a remote drive using FuseSSHFS
============================================================================
"""

import time
import getpass
import os
import pexpect


def mount(user, host, password):
    """ Mounts a remote drive <user>@<host>:/ to ~/Desktop/RemoteHome 
        on localhost
    """
    mount = os.path.expanduser("~/Desktop/sshfs")
    if os.path.isdir(mount) == False:
        os.makedirs(mount)
    cmd = str("/usr/local/bin/sshfs -p 22 {}@{}:/ {} -oauto_cache,reconnect," +
              "defer_permissions,negative_vncache,volname=RemoteHome"
                ).format(user, host, mount)
    prompt = str("{}@{}'s password: ").format(user, host)
    try:
        sshfs = pexpect.spawn(cmd)
        sshfs.expect(prompt)
        time.sleep(0.1)
        sshfs.sendline(password)
        time.sleep(5)
        sshfs.expect(pexpect.EOF)
    except Exception, e:
        print("Unable to mount remote drive. Double-check your input and" +
              " that the host is online.")
        return 1
    del (user, host, password)
    return 0


def main():
    user = raw_input("username: ")
    host = raw_input("hostname: ")
    pawd = getpass.getpass("password: ")
    mount(user, host, pawd)


if __name__ == "__main__":
    main()
