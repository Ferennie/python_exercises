import anytree
from anytree import Node, RenderTree


class FamilyTree:
    def parent.Node == 'Lucille'
    def __init__(self):
        self.lucille = parent.Node("")
        self.george_oscar = child.Node("")
        self.michael = anytree.Node("")
        self.lindsay = anytree.Node("")
        self.buster = anytree.Node("")
        self.george_michael = anytree.Node("")
        self.maeby = anytree.Node("")

    def populate_family_tree(self):
        self.lucille = anytree.Node('Lucille')
        self.george_oscar = anytree.Node("George Oscar", parent='Lucille')
        self.michael = anytree.Node("Michael", parent='Lucille')
        self.lindsay = anytree.Node("Lindsay", parent='Lucille')
        self.buster = anytree.Node("Buster", parent='Lucille')
        self.george_michael = anytree.Node("George Michael", parent='Michael')
        self.maeby = anytree.Node("Maeby", parent='Lindsay')

        # ex: child = Node('Child Name', parent = parent_node)

        self.lucille = anytree.Node("Lucille")
        self.george_oscar = anytree.Node("George Oscar", parent=self.lucille)
        self.michael = anytree.Node("Michael", parent=self.lucille)
        self.lindsay = anytree.Node("Lindsay", parent=self.lucille)
        self.buster = anytree.Node("Buster", parent=self.lucille)
        self.george_michael = anytree.Node("George Michael", parent=self.michael)
        self.maeby = anytree.Node("Maeby", parent=self.lindsay)

        return

    class Familytree:
        def __init__(self, 'lucille', 'george_oscar', ):