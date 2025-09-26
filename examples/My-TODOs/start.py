#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2025-09-27 14:04
# Author    : huang kai
# Usage     :
# Version   :
# Comment   :


# Import built-in modules


# Import third-party modules

# Import local modules
import sys
from ui import MySiliconApp


if __name__ == "__main__":
    from siui.qt_utils import render_ui
    with render_ui():
        window = MySiliconApp()
        window.show()

