"""
Módulos Collections — Deque
Podemos dizer que o deque é uma lista de alto desempenho
"""
# Import
from collections import deque

# Criando deque

deq = deque('geek')
print(deq)

# Adicionando elementos no deque
deq.append('y')  # adiciona no final
deq.appendleft('k')  # adiciona no início
print(deq)

# Remover elementos
print(deq.pop())  # remove e retorna o último elemento
print(deq.popleft())  # remove e retorna o primeiro elemento
