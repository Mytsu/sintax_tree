from copy import deepcopy

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
operators = ['+', '-', '*', '/']

def read(expr: str):
    exp = deepcopy(expr)
    stack = []
    while(len(exp)):
        val = exp[:1]
        exp = exp[1:]
        if val in numbers:
            stack.append(Node(val))
        elif val in operators:
            aux = Node(val)
            aux.right = stack.pop()
            aux.left = stack.pop()
            stack.append(aux)
    return stack.pop()

def posfix(tree):
    if tree.left != None:
        posfix(tree.left)
    if tree.right != None:
        posfix(tree.right)
    posfix(tree.val)

def run(tree):
    return ''

if __name__ == '__main__':
    exp = input()
    while( exp != 0 ):
        sintax_tree = read(exp)
        posfix(sintax_tree)
        answer = run(sintax_tree)
        print(answer)