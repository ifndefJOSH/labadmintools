# Introduction

LabAdminTools (LAT) is supported on the following platforms:

| OS       | Status                                           |
+----------+--------------------------------------------------+
| Linux    | Tested, works well                               |
| Windows  | Should work in theory (except template commands) |
| MacOS    | Should work in theory (except some templates)    |

It just requires Python and Pip or Conda.

## Installation

First, install Python 3.10+ from [https://python.org/](https://python.org) for your target OS (or, better yet, from a package manager). Ensure that Pip has been installed via checking that `python -m pip` does not return a `ModuleNotFoundError`.

You may (and probably should) set up a venv.

Then install the required Python packages via `python -m pip -r requirements.txt`.

Finally, run either `src/main.py` (all OSs) OR the `xadmintools` symlink in the root directory of this repo (Linux and Mac only).
