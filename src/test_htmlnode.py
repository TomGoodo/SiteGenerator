import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        html_node = HTMLNode("div","Hellow world!", None,{"class": "greeting", "href": "https://yahoo.com"})
        self.assertEqual(html_node.props_to_html(), ' class="greeting" href="https://yahoo.com"')

    def test_values(self):
        node = HTMLNode("div","I am using Nvim")
        
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I am using Nvim")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props,None)

    def test_repr(self):
        node = HTMLNode("p","Did I do it", None, {"class": "test"})
        self.assertEqual(node.__repr__(), "HTMLNode(p, Did I do it, children : None, {'class': 'test'})")
