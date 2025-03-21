import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("div","Hello World",None,{"class": "greeting", "href": "yahoo.com"})
        self.assertEqual(node.props_to_html(),' class="greeting" href="yahoo.com"')

    def test_values(self):
        node = HTMLNode("div","im so stupid")
        self.assertEqual(node.tag,"div")
        self.assertEqual(node.value,"im so stupid")
        self.assertEqual(node.children,None)
        self.assertEqual(node.props,None)

    def test_repr(self):
        node = HTMLNode("YO","YOYO",None,{"class": "primary"})
        self.assertEqual(node.__repr__(),"HTMLNode(YO, YOYO, children: None, {'class': 'primary'})")

    # Leaf Node Testing

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "this is a link!", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">this is a link!</a>')

    def test_leaf_no_tag(self):
        node1 = LeafNode(None,"Test")
        self.assertEqual(node1.to_html(),"Test")

    # Parent Node Testing

    def test_parent_to_html(self):
        node = ParentNode("p",[LeafNode("b","Bold text"),LeafNode(None,"Normal text"),LeafNode("i","italic text"),LeafNode(None,"Normal text")])
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
