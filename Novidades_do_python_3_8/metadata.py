"""
Metadata
dados internos
"""
from importlib import metadata
print(metadata.version('pip'))
metadados_pip = metadata.metadata('pip')
print(list(metadados_pip))
print(metadados_pip['Project-URL'])

# quantos arquivos tem no pacote pip
print(len(metadata.files('pip')))

# o que o pip requer?
print(metadata.requires('pip'))