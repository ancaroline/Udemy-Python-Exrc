import math

# math.prod - retorna o produto de um container numérico
nuns_v1 = [2, 3, 6, 8]
nuns_v2 = (2, 3, 6, 8)
nuns_v3 = {2, 3, 6, 8}

# o .prod realiza o produto
print(math.prod(nuns_v1))
print(math.prod(nuns_v2))
print(math.prod(nuns_v3))

# math.isqrt
print(math.isqrt(9))  # a raiz quadrada inteira. Não arredonda valor, só devolve a parte inteira.
print(math.sqrt(9))  # número real

# math.dist - retorna a distância euclidiana entre dois pontos, seja esses pontos 3D ou 2D
# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D
p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

# math.hypot - retorna a hipotenusa
print(math.hypot(*p3d1))
# -> asterisco vai descompactar, ao invés de ficar (12, 50, 40) -> ficará: 12 50 40
print(math.hypot(*p2d1))

# --- Estatística ---
# statistics.fmean - calcula a média de números reais
import statistics

valores_reais = [1.2, 4.222, 9.9]
valores_inteiros = [1, 5, 6, 7]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))

# statistics.geometric_mean - calcula a média geométrica de números reais

print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))

# statistics.multimode - retorna o valor mais frequente em uma sequência
seq1 = 'geek'
seq2 = [3, 4, 5, 2, 3, 3, 2, 2]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))