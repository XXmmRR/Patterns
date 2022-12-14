class HTMLElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)


class HTMLBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HTMLElement(name=root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HTMLElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)


builder = HTMLBuilder('ul')
builder.add_child('li', 'hello')\
       .add_child('li', 'world')
print('Ordinary builder:')
print(builder)
