"""
Módulos Externos
Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package
Todos os pacotes oficiais externos: https://pypi.org

colorama -> utilizado para permitir impressão de textos coloridos no terminal

Instalando um módulo:
pip install nome_do_modulo
exemplo: pip install python-pdf
"""
"""
# Utilizando o pacote: Colorama
from colorama import init, Fore
init()

print(Fore.MAGENTA + 'Geek')
"""
# utilizando o pacote: python-pdf
import pydf

pdf = pydf.generate_pdf('<h1>geek</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
