from textnode import TextNode, TextType

def main():
    dummy = TextNode("this is some anchor text",TextType.LINK,"https://www.boot.dev")
    print("test")
    print(dummy)



if __name__ == "__main__":
    main()
