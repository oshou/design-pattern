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


MESSAGE = """This is a very short paragraph just so that we can see two paragraphs in action."""


def main():
    paragraph1 = MESSAGE.format("plain-text", "TextRenderer")
    paragraph2 = """This is another short paragraph just so that web can see two paragraphs in action."""
    title = "Plain Text"
    textPage = Page(title, TextRenderer(22))
    textPage.add_paragraph(paragraph1)
    textPage.add_paragraph(paragraph2)
    textPage.render()

    print()

    paragraph1 = MESSAGE.format("HTML", "HtmlRenderer")
    title = "HTML"
    file = sys.stdout
    htmlPage = Page(title, HtmlRenderer(HtmlWriter(file)))
    htmlPage.add_paragraph(paragraph1)
    htmlPage.add_paragraph(paragraph2)
    htmlPage.render()

    try:
        page = Page(title, HtmlWriter())
        page.render()
        print("ERROR! rendering with an invalid renderer")
    except TypeError as err:
        print(err)


class Page:
    def __init__(self, title, renderer):
        if not isinstance(renderer, Renderer):
            raise TypeError("Expected object of type Renderer, got {}".format(
                type(renderer).__name__))
        self.title = title
