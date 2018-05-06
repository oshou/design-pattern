#!/usr/bin/env python

import abc
import sys
import textwrap
if sys.version_info[:2] < (3, 2):
    from xml.sax.saxutils import escape
else:
    from html import escape
import Qtrac


@Qtrac.has_methods("header", "paragraph", "footer")
class Renderer(metaclass=abc.ABCMeta):
    pass

MESSAGE = """This"""
