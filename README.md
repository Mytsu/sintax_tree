# Sintax Tree

Trabalho 2 de Compiladores I

## Descrição

Este script faz a leitura de uma expressão algébrica simples, com operandos de apenas um dígito e operadores comuns (+, -, *, /).

A expressão é armazenada em uma pilha, onde quando um operador é lido, este forma uma árvore com os 2 elementos anteriores como folhas. Ao fim da leitura, a árvore da expressão é removida da pilha, exibida, depois é exibido a expressão em formato infix, e a expressão é calculada.

## Execução

Execute o script usando o comando: ```python3 sintax_tree.py``` Desta forma você pode digitar expressões em formato posfix e pressionar enter onde ela será processada, após o resultado ser exibido, você pode continuar a digitar outras expressões ou digitar 0 para sair.