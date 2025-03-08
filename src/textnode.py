from enum import Enum


class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:

    def __init__(self, text,text_type,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self,newTextNode):
        if self.text == newTextNode.self and self.text_type == newTextNode.text_type and self.url == newTextNode.url:
            return True
        return False
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"     


    
