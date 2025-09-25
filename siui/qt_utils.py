# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2022/5/21 20:57
# Author    : huang kai
# Usage     :
# Version   :
# Comment   :
"""实现功能介绍"""

# Import built-in modules
import sys
import contextlib
# Import third-party modules
from Qt import Qt
from Qt.QtWidgets import QApplication

try:
    from Qt import QDesktopWidget
except:
    pass

# Import local modules

def get_screen_resolution():
    """
    获取屏幕分辨率
    """
    app = QApplication.instance()
    if not app:
        app = QApplication([])

    screen_rect = QDesktopWidget().screenGeometry() if Qt.IsPySide2 else app.primaryScreen().geometry()
    screen_width = screen_rect.width()
    screen_height = screen_rect.height()
    return screen_width, screen_height


@contextlib.contextmanager
def render_ui():
    """
    show a Qt leguo_widget
    :return:
    """
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    yield app
    try:
        sys.exit(app.exec_())
    except:
        pass