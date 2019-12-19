from sys import stderr
from utils import BinaryTreeNode as Node, display, infix

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operators = ['+', '-', '*', '/']

def read(expression: str):
    stack = list()
    expr = list(expression)
    while len(expr) != 0:
        value = expr.pop(0)
        if value in numbers:
            stack.append(Node(value))
        elif value in operators:
            tree = Node(value)
            tree.right = stack.pop()
            tree.left = stack.pop()
            stack.append(tree)
        else:
            print('Invalid input: ' + str(value), file=stderr)
    return stack.pop()

def calc(tree):
    if tree.value in numbers:
        return int(tree.value)
    elif tree.value == '+':
        return calc(tree.left) + calc(tree.right)
    elif tree.value == '*':
        return calc(tree.left) * calc(tree.right)
    elif tree.value == '-':
        return calc(tree.left) - calc(tree.right)
    elif tree.value == '/':
        right = calc(tree.right)
        if right == 0:
            return 0
        else:
            return calc(tree.left) / right


if __name__ == '__main__':
    exp_input = input()
    while exp_input != '0':
        sintax_tree = read(exp_input)
        print('Tree display:')
        display(sintax_tree)
        print('Infix expression: ', end='')
        infix(sintax_tree)
        print('Result: ' + str(calc(sintax_tree)))
        exp_input = input()