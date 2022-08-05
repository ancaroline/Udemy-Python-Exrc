"""
Estruturas lógicas

AND - ambos os valores precisam ser true
OR - um ou outro valor precisa ser true
NOT - valor booleano invertido
IS - valor comparado com um segundo
"""
ativo = True
logado = True
logado1 = False
# AND
if ativo and logado:
    print('logado')
else:
    print('aive a sua conta')
# OR
if ativo or logado1:
    print('logado')
else:
    print('aive a sua conta')
# NOT
login = True
if not login:
    print("ok")
else:
    print("not okay")
# IS
if ativo is True:
    print('Bem-vindo')
else:
    print('Ative')

# ativo é True?
print(ativo is True)
