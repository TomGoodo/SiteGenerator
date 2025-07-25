import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://yahoo.com"})
        self.assertEqual(node.to_html(), '<a href="https://yahoo.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This is just a drill")
        self.assertEqual(node.to_html(), 'This is just a drill')
        

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ])
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ])
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>"
        )
