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
"""
## This module defines global shared types

Use Python's Type Hint syntax, reference:
- [`typing`](https://docs.python.org/3/library/typing.html)
- [`PEP 484`](https://www.python.org/dev/peps/pep-0484/)
- [`PEP 526`](https://www.python.org/dev/peps/pep-0526/)
"""

from typing import Optional, Union

from Qt.QtCore import QObject, Qt
from Qt.QtGui import QColor, QGradient, QPainter, QPen
from Qt.QtWidgets import QWidget
from typing_extensions import TypeAlias

T_WidgetParent: TypeAlias = Optional[QWidget]
"""Type of widget parent"""

T_ObjectParent: TypeAlias = Optional[QObject]
"""Type of object parent"""

T_PenStyle: TypeAlias = Union[QPen, Qt.PenStyle, QColor, Qt.GlobalColor]
"""Type of QPen style"""

T_Brush: TypeAlias = Optional[Union[QGradient, QColor, Qt.GlobalColor]]
"""Type of QBrush"""

T_RenderHint: TypeAlias = Optional[Union[QPainter.RenderHint, int]]
"""Type of QPainter.RenderHint"""