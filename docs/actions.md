# Actions

*Actions* (not to be confused with the `QActions` used in the UI) are things that are to be executed on the target machines. They can be:

- File copy actions
- Command actions
- Shell script actions

All actions are created, modified, and executed from the Actions tab, accessible on the left tab-bar.

Actions are executed in order, but lists of actions can be created in any order. To create an action, either press the **New Action** button, or the **Action > New Action** menu item. Actions are "selected" via the check box in the left-hand column in the action editor tab.

Template actions can be accessed by **Actions > Show Template Actions**. This causes a tree view to appear below the action editor table containing a number of template actions, primarily commands, which would be of interest for a sysadmin or a labadmin.

The table of selected actions is called an "action list", and can be executed in all or in part on the machines in the lab list, via the **Run Action List** button.

To load an action list, press **Action > Load Action List**. The `.actionlist` file is just a comma-separated list file in plaintext, so you can also edit it in a text editor. Similarly, to save an action list **Action > Save Action List** may be used. Action types may be changed after they are created, and data is attempted to be preserved. Comments may be assigned to actions. These do not affect the action as it is executed.

**Action > Export Action List as Shell Script** lets you export your action list as a shell script. These shell scripts take saved lab files as their first parameters.
