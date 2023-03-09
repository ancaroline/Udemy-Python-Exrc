"""
Introdução ao módulo Unittest
Unittest -> testes unitários
O que são testes unitários?
É a forma de se testar unidades individuais de código fonte.
Unidades individuais podem ser: funções, métodos, classes, módulos.
Objetivo: Se cada unidade atende especificamente a sua especificação.

OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest. TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos -> unittest.main()

TestCase -> Casos de teste para a sua unidade

— > Conhecendo os assertions:
https://docs.python.org/3/library/unittest.html

assertEqual
assertNotEqual
assertTrue
assertFalse
assertIs
assertIsNot
assertIsNone
assertIsNotNone
assertIn
assertNotIn
assertIsIstance
assertNotInstance

Por convenção, todos os testes em um test case, devem ter seu nome iniciado com test_

Para executar os testes com unittest:
python nome_do_modulo.py

Para executar os testes com unittest no modo verboso:
python nome_do_modulo.py -v

# Docstrings nos testes
Podemos acrescentar (e é recomendado) docstrings nos nossos testes.
"""

# Prática - Utilizando a abordagem TDD
