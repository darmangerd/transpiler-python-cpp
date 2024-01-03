"""
Petit module utilitaire pour la construction, la manipulation et la 
représentation d'arbres syntaxiques abstraits.

Sûrement plein de bugs et autres surprises. À prendre comme un 
"work in progress"...
Notamment, l'utilisation de pydot pour représenter un arbre syntaxique cousu
est une utilisation un peu "limite" de graphviz. Ca marche, mais le layout n'est
pas toujours optimal...
"""

import pydot


class Node:
    count = 0
    type = "Node (unspecified)"
    shape = "ellipse"

    def __init__(self, children=None):
        self.ID = str(Node.count)
        Node.count += 1
        if not children:
            self.children = []
        elif hasattr(children, "__len__"):
            self.children = children
        else:
            self.children = [children]
        self.next = []

    def add_next(self, next):
        self.next.append(next)

    def ascii_tree(self, prefix=""):
        result = "%s%s\n" % (prefix, repr(self))
        prefix += "|  "
        for c in self.children:
            if not isinstance(c, Node):
                result += "%s*** Error: Child of type %r: %r\n" % (
                    prefix, type(c), c)
                continue
            result += c.ascii_tree(prefix)
        return result

    def __str__(self):
        return self.ascii_tree()

    def __repr__(self):
        return self.type

    def make_graphical_tree(self, dot=None, edgeLabels=True):
        if not dot:
            dot = pydot.Dot()
        dot.add_node(pydot.Node(self.ID, label=repr(self), shape=self.shape))
        label = edgeLabels and len(self.children) - 1
        for i, c in enumerate(self.children):
            c.make_graphical_tree(dot, edgeLabels)
            edge = pydot.Edge(self.ID, c.ID)
            if label:
                edge.set_label(str(i))
            dot.add_edge(edge)
            # Workaround for a bug in pydot 1.0.2 on Windows:
            # dot.set_graphviz_executables({'dot': r'C:\Program Files\Graphviz2.38\bin\dot.exe'})
        return dot

    def thread_tree(self, graph, seen=None, col=0):
        colors = ("red", "green", "blue", "yellow", "magenta", "cyan")
        if not seen:
            seen = []
        if self in seen:
            return
        seen.append(self)
        new = not graph.get_node(self.ID)
        if new:
            graphnode = pydot.Node(self.ID, label=repr(self), shape=self.shape)
            graphnode.set_style("dotted")
            graph.add_node(graphnode)
        label = len(self.next) - 1
        for i, c in enumerate(self.next):
            if not c:
                return
            col = (col + 1) % len(colors)
            col = 0  # FRT pour tout afficher en rouge
            color = colors[col]
            c.threadTree(graph, seen, col)
            edge = pydot.Edge(self.ID, c.ID)
            edge.set_color(color)
            edge.set_arrowsize(".5")
            # Les arr�tes correspondant aux coutures ne sont pas prises en compte
            # pour le layout du graphe. Ceci permet de garder l'arbre dans sa repr�sentation
            # "standard", mais peut provoquer des surprises pour le trajet parfois un peu
            # tarabiscot� des coutures...
            # En commantant cette ligne, le layout sera bien meilleur, mais l'arbre nettement
            # moins reconnaissable.
            edge.set_constraint("false")
            if label:
                edge.set_taillabel(str(i))
                edge.set_labelfontcolor(color)
            graph.add_edge(edge)
        return graph


class ValueNode(Node):
    type = "value"
    value_type = "any"

    def __init__(self, tok, type):
        Node.__init__(self)
        self.tok = tok
        self.value_type = type

    def __repr__(self):
        return repr(f"{self.tok} ({self.value_type})")


class ProgramNode(Node):
    type = "program"


class TokenNode(Node):
    type = "token"
    value_type = "any"

    def __init__(self, tok, type="any"):
        Node.__init__(self)
        self.tok = tok
        self.value_type = type

    def __repr__(self):
        return repr(self.tok)


class ArgNode(Node):
    type = "arg"

    def __init__(self, tok, type):
        Node.__init__(self)
        self.value_type = type
        self.tok = tok

    def __repr__(self):
        return f"{self.type} {self.tok}"


class TypeNode(Node):
    type = "type"

    def __init__(self, tok):
        Node.__init__(self)
        self.tok = tok

    def __repr__(self):
        return f"{self.tok}"


class ArgumentsNode(Node):
    type = "arguments"

    def __init__(self, args):
        Node.__init__(self, args)

    def __repr__(self):
        return f"({', '.join([repr(arg) for arg in self.children])})"


class ReturnNode(Node):
    type = "return"

    def __init__(self, expr):
        Node.__init__(self, [expr])

    def __repr__(self):
        return f"return"


class DefNode(Node):
    type = "def"

    def __init__(self, tok, args, return_type, body):
        Node.__init__(self, [body])
        self.return_type = return_type
        self.tok = tok
        self.args = args

    def __repr__(self):
        return f"{self.return_type} {self.tok} ({', '.join([repr(arg) for arg in self.args.children])})"


class CallNode(Node):
    type = "call"

    def __init__(self, tok, args):
        Node.__init__(self, args)
        self.tok = tok

    def __repr__(self):
        return f"{self.tok}({', '.join([repr(arg) for arg in self.children])})"


class IfNode(Node):
    type = "if"

    def __init__(self, cond, then, els=None):
        Node.__init__(self, [cond, then, els] if els else [cond, then])

    def __repr__(self):
        return f"if"


class OpNode(Node):
    type = "op"

    def __init__(self, op, children):
        Node.__init__(self, children)
        self.op = op
        self.value_type = children[0].value_type

        try:
            self.nbargs = len(children)
        except AttributeError:
            self.nbargs = 1

    def __repr__(self):
        return f"{self.op}"


class AssignNode(Node):
    type = "assign"

    def __init__(self, children, init_type=None):
        Node.__init__(self, children)
        self.init_type = init_type

    def __repr__(self):
        if not self.init_type:
            return f"assign"
        else:
            return "declare"


class WhileNode(Node):
    type = "while"


class EntryNode(Node):
    type = "ENTRY"

    def __init__(self):
        Node.__init__(self, None)


def add_to_class(cls):
    """ Décorateur permettant d'ajouter la fonction décorée en tant que méthode
    à une classe.

    Permet d'implémenter une forme élémentaire de programmation orient�e
    aspects en regroupant les méthodes de différentes classes impl�mentant
    une même fonctionnalité en un seul endroit.

    Attention, après utilisation de ce décorateur, la fonction décorée reste dans
    le namespace courant. Si cela dérange, on peut utiliser del pour la détruire.
    Je ne sais pas s'il existe un moyen d'éviter ce phénomène.
    """

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator
