# Lab Admin Tools

A graphical tool that makes use of `fabric` to execute commands, copy files, and administer networks of computers.

**Status**: Usable, but in &alpha;

This tool is written using Python, PyQt5, and `fabric`. It lets you store lists of "actions" to be executed on a "lab", a.k.a., a set of computers. These actions are executed all at once, on every computer in the lab, by making use of fabric's `ThreadedGroup` class. The following action types are supported:

1. Command: Write a one-line command to be executed on each machine
2. File copy: copy a file to the target machines
3. Script: execute an entire shell script on each machine

Action lists can also be exported as UNIX shell scripts, so this tool may be used to graphically build administrative scripts that can be run later without the tool itself.

## Screenshots

Note: UI uses default OS styling. These screenshots were taken on KDE plasma with global dark mode enabled. Some details were blurred for privacy/security.

![Lab editor](./screenshots/labEditor.png)

![Action editor](./screenshots/actionEditor.png)

![Execution options](./screenshots/executionDialog.png)

![Log Viewer](./screenshots/logsViewer.png)
