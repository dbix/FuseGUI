"""
============================================================================
Name        : sshfsmount.py
Author      : Derek Bixler
Version     : 0.1
Description : Simple interface for mounting a remote drive using FuseSSHFS
============================================================================
"""

from Tkinter import Frame, Label, Entry, Button
from sys import exit
from sshfs import mount


class SSHFSApplication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.fld_user = self.fld_host = self.fld_pawd = None
        self.lbl_user = self.lbl_host = self.lbl_pawd = None
        self.btn_quit = self.btn_mount = None
        self.create_widgets()

    def create_widgets(self):
        """ Creates labels and text fields for username, hostname, and password.
            The password field replaces the visible entry with *'s
        """
        # Labels
        self.lbl_user = Label(self, text="Username:")
        self.lbl_host = Label(self, text="Hostname:")
        self.lbl_pawd = Label(self, text="Password:")

        # Fields
        self.fld_user = Entry(self)
        self.fld_host = Entry(self)
        self.fld_pawd = Entry(self, show='*')

        # Buttons
        self.btn_quit = Button(self, text="Quit", command=self.quit,
                               takefocus=0)
        self.btn_mount = Button(self, text="Mount", command=self.mount_drive,
                                takefocus=1)

        # Arrange
        self.lbl_user.grid(column=0, row=0)
        self.lbl_host.grid(column=0, row=1)
        self.lbl_pawd.grid(column=0, row=2)
        self.fld_user.grid(column=1, row=0)
        self.fld_host.grid(column=1, row=1)
        self.fld_pawd.grid(column=1, row=2)
        self.btn_quit.grid(column=0, row=3)
        self.btn_mount.grid(column=1, row=3)

    def mount_drive(self):
        """ The function assigned to the "Mount" button. Retrieves user entries
            as strings and plugs them into sshfs.mount(user, host, password).
        """
        user = self.fld_user.get()
        host = self.fld_host.get()
        pawd = self.fld_pawd.get()
        if mount(user, host, pawd) == 0:
            del (self.fld_pawd, pawd)
            exit()
        else:
            return


if __name__ == "__main__":
    app = SSHFSApplication()
    app.master.title("sshfs-mount")
    app.mainloop()





