import unittest
from block_md import markdown_to_blocks, block_to_block_type, BlockType, extract_title

class TestBlockMD(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("## TEST"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```TEST```"), BlockType.CODE)
        self.assertEqual(block_to_block_type(">To be or not to be"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- this is a list\n- this is another"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. This is a test\n2. this is another"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("testing for a normal - pagaraph"), BlockType.PARAGRAPH)

    def test_extract_title(self):
        self.assertEqual("Hello", extract_title('# Hello'))

    def test_extract_title_with_multiple_lines(self):
        markdown = ("Hello, I am testing how well the Heading feature \n works \n# TEST")
        self.assertEqual("TEST", extract_title(markdown))
