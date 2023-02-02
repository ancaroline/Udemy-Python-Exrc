"""
Módulos customizados
Como módulos nada mais são do que arquivos Python, então todos os arquivos criados aqui
são módulos Python prontos para serem utilizados.
"""

# Importando uma função específica
from funcao_import import soma_impares

print(soma_impares([1, 2, 3]))
# Em um módulo não pode ter execução de código, como daquela forma na 'funcao_import'

# Importando todo o módulo (Temos acesso a TODOS os elementos do módulo)
import funcao_import as fcp

# acessando e imprimindo uma variável contida no módulo
print(fcp.lista)

print(fcp.soma_impares(fcp.lista))





