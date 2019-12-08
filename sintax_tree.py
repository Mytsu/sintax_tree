from copy import deepcopy

# Basic Tree Leaf
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
operators = ['+', '-', '*', '/']

# read values from input, inserting them into a stack as
# node leafs, if an operator is found, insert the leafs
# to the right and lefts values of the operator's node
# at the end of the loop, the only element on the stack
# is the root of the tree
def read(expr: str):
    exp = deepcopy(expr)
    stack = list()
    while(len(exp)):
        val = exp[:1]
        exp = exp[1:]
        if val in operators:
            aux = Node(val)
            aux.right = stack.pop()
            aux.left = stack.pop()
            stack.append(aux)
        elif int(val) in numbers:
            stack.append(Node(int(val)))
    return stack.pop()

# posfix run of the tree, appending the leafs values
# to a list for printing
def posfix(tree):
    expr = list()
    _posfix(tree, expr)
    return expr

def _posfix(tree, expr):
    if tree.left != None:
        posfix(tree.left)
        if tree.left.value in numbers:
            expr.append(tree.left.value)
        expr.append(tree.value)
        if tree.right.value in numbers:
            expr.append(tree.right.value)
    if tree.right != None:
        posfix(tree.right)

# prints the expression
def print_exp_list(expr):
    for i in expr:
        print(i, end = " ")
    print("=", end = " ")

# calculates the result of the expression
def op(expr):
    if expr[1] == operators[0]:
        expr[0] = expr[0] + expr[2]
        expr[1:] = expr[3:]
    elif expr[1] == operators[1]:
        expr[0] = expr[0] - expr[2]
        expr[1:] = expr[3:]
    elif expr[1] == operators[2]:
        expr[0] = expr[0] * expr[2]
        expr[1:] = expr[3:]
    elif expr[1] == operators[3]:
        expr[0] = expr[0] / expr[2]
        expr[1:] = expr[3:]
    return expr

# loop through the values in the list to calculate
def result_exp(expr):
    while len(expr) > 1:
        expr = op(expr)
    return expr[0]

if __name__ == '__main__':
    exp_input = input()
    while len(exp_input) != '0':
        sintax_tree = read(exp_input)
        print()
        expr = posfix(sintax_tree)
        print_exp_list(expr)
        print(result_exp(expr))
        expr.clear()
        exp_input = input()
