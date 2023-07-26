from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from gen.XMLParserVisitor import XMLParserVisitor
import os
from ast import *

attr_dic = {
        'src': 'webview.load(QUrl',
        'name': 'webview.setWindowTitle',
        'width': 'webview.setFixedWidth',
        'height': 'webview.setFixedHeight',
        'srcdoc': 'webview.setHtml'
}
Qoute = ['src', 'name', 'srcdoc']
Paranthesis = ['src']

class WidgetNode:
    def __init__(self, widget_type, attrs, children):
        self.widget_type = widget_type
        self.attrs = attrs
        self.children = children

    def __repr__(self):
        attr_strs = [f"{name}={value}" for name, value in self.attrs.items()]
        attr_str = ' '.join(attr_strs)
        child_strs = [repr(child) for child in self.children]
        child_str = '\n'.join(child_strs)
        return f"<{self.widget_type} {attr_str}>{child_str}\n</{self.widget_type}>"

class ContentNode:
    def __init__(self, children):
        self.children = children

    def __repr__(self):
        child_strs = [repr(child) for child in self.children]
        child_str = '\n'.join(child_strs)
        return child_str


class TextNode:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text


class MyXMLVisitor(XMLParserVisitor):
    def __init__(self):
        self.widgets = set()
        self.valid_attributes = [
            'src' , 'name' , 'width' , 'height' , 'srcdoc', 'text'
        ]

    def visitWidget(self, ctx):
        children = []
        if(ctx.content() != None):
          for child in ctx.content().children:
              if isinstance(child, XMLParser.ChardataContext):
                  children.append(TextNode(child.getText()))
              elif isinstance(child, XMLParser.WidgetContext):
                  children.append(self.visit(child))
              # Add support for other types of content (reference, CDATA, PI, COMMENT) as needed
        widget_type = ctx.Name(0).getText()
        attrs = {}
        for attr in ctx.attribute():
            attr_name = attr.Name().getText()
            attr_value = attr.STRING().getText()[1:-1]
            attrs[attr_name] = attr_value
            if(attr_name not in self.valid_attributes):
                print(f"Error: Invalid attribute '{attr_name}' for widget type '{widget_type}'")
            if(attr_name in ["padx", "pady", "bd", "height", "width"]):
                if(not attr_value.isnumeric()):
                    print(f"Error: Invalid value '{attr_value}' for attribute '{attr_name}' in widget Frame")
            if(attr_name == "bg"):
                if(attr_value not in ["red", "blue", "green", "yellow", "alpha", "purple"]):
                    print(f"Error: Invalid value '{attr_value}' for attribute '{attr_name}' in widget Frame")
        return WidgetNode(widget_type, attrs, children)

    def visitContent(self, ctx):
        children = []
        for child in ctx.children:
            if isinstance(child, XMLParser.ChardataContext):
                children.append(TextNode(child.getText()))
            elif isinstance(child, XMLParser.WidgetContext):
                children.append(self.visit(child))
            # Add support for other types of content (reference, CDATA, PI, COMMENT) as needed
        return ContentNode(children)

########################################################### Phase 3

def convert_to_python_code(properties, output_stream):
    output_stream.write("from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QWidget\n")
    output_stream.write("from PyQt5.QtWebEngineWidgets import QWebEngineView\n")
    output_stream.write("from PyQt5.QtCore import QUrl\n\n")


    output_stream.write("app = QApplication([])\n")
    output_stream.write("window = QMainWindow()\n")
    output_stream.write("central_widget = QWidget()\n")
    output_stream.write("window.setCentralWidget(central_widget)\n")
    output_stream.write("layout = QHBoxLayout(central_widget)\n\n")
    output_stream.write("def PythonCode():\n")
    output_stream.write("\twebview = QWebEngineView()\n")
    output_stream.write("\tlayout.addWidget(webview)\n\n")


    for i, prop in enumerate(properties):
        text = properties[prop]
        if prop in Paranthesis:
            if prop in Qoute:
                output_stream.write(f"\t{attr_dic[prop]}('{text}'))\n")
            else:
                output_stream.write(f"\t{attr_dic[prop]}({text}))\n")
        else:
            if prop in Qoute:
                output_stream.write(f"\t{attr_dic[prop]}('{text}')\n")
            else:
                output_stream.write(f"\t{attr_dic[prop]}({text})\n")

    output_stream.write("\n\ndef Test(self):\n")
    output_stream.write("\tframe = self.sender()\n")
    output_stream.write("\t# to be completed\n\n")

    output_stream.write("if __name__ == '__main__':\n")
    output_stream.write("\tPythonCode()\n")
    output_stream.write("\twindow.show()\n")
    output_stream.write("\tapp.exec_()\n")



if __name__ == "__main__":    
  lexer = XMLLexer(InputStream('<iframe src="https://www.varzesh3.com" name="Classic" width="400"><iframe text="OK" /></iframe>'))
  stream = CommonTokenStream(lexer)
  parser = XMLParser(stream)
  tree = parser.widget()

  visitor = MyXMLVisitor()
  ast = visitor.visit(tree)

  output_address = "genereatedcode.py"
  if os.path.exists(output_address):
    os.remove(output_address)

  output_stream = open(r""+output_address, "a")
  convert_to_python_code(ast.attrs, output_stream)
  print(ast)
