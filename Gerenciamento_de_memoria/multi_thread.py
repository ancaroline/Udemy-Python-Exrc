import time
from threading import Thread

CONTADOR = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


t1 = Thread(target=contagem_regressiva, args=(CONTADOR // 2,))
t2 = Thread(target=contagem_regressiva, args=(CONTADOR // 2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f'Tempo em segundos - {fim - inicio}')

"""
2 threads rodando como se fosse single thread, isto acontece por conta do GIL (Global Interpreter Lock).
Por isso, o tempo de execução entre o código single_thread e o multi_thread não terá tanta diferença.

Caso tenha problema com o GIL, podemos utilizar multi-processing ao invés de multi threading.
Assim, cada processo Python ganha seu próprio interpretador e espaço em memória.
"""