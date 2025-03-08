import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("div","Hello World",None,{"class": "greeting", "href": "yahoo.com"})
        self.assertEqual(node.props_to_html()," class: 'greeting' href: 'yahoo.com'")

    def test_values(self):
        node = HTMLNode("div","im so stupid")
        self.assertEqual(node.tag,"div")
        self.assertEqual(node.value,"im so stupid")
        self.assertEqual(node.children,None)
        self.assertEqual(node.props,None)

    def test_repr(self):
        node = HTMLNode("YO","YOYO",None,{"class": "primary"})
        self.assertEqual(node.__repr__(),"HTMLNode(YO, YOYO, children: None, {'class': 'primary'})")

