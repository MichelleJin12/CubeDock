# -*- coding: utf-8 -*-

"""
    Copyright (c) 2020, Gabriel Kim(Doohoon Kim).

    The "CubeDock" is distributed under the "3-clause BSD" license.
    See details COPYING.
"""

import sys
import subprocess

def main(*args, **kwargs):
    from .cli_parse import Cli_Parse
    Cli_Parse()

if __name__ == '__main__':
    sys.exit(main())