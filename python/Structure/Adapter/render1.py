#!/usr/bin/env python

import abc
import collections
import sys
import textwrap

if sys.version_info[:2] < (3, 2):
    from xml.sax.saxutils import escape
else:
    from html import escape

if sys.version_info[:2] >= (3, 3):
    class Renderer(metaclass=abc.ABCMeta):

        @classmethod
        def __subclasshook__(Class, Subclass):
            if Class is Renderer:
                attributes = collection.ChainMap(
                    *(Superclass.__dict__ for Superclass in Subclass.__mro__))
                methods = ("header", "paragraph", "footer")
                if all(method in attributes for method in methods):
                    return True
            return NotImplemented
else:
    class Renderer(metaclass=abc.ABCMeta):
        @classmethod
        def __subclasshook__(Class, Subclass):
            if Class is Renderer:
                needed = {"header", "paragraph", "footer"}
                for Superclass in Subclass.__mro__:
                    for meth in needed.copy():
                        if meth in Superclass.__dict__:
                            needed.discard(meth)
                        if not needed:
                            return True
            return NotImplemented

MESSAGE = """This is a very short {} paragraph that demonstrates
the simple {} class."""


def main():
    paragraph1 = MESSAGE.format("plain-text", "TextRenderer")
    paragraph2 = """This is another short paragraph just so that we can see two paragraphs in action."""
    title = "Plain Text"
