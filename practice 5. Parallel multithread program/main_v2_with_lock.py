from threading import Thread, Lock
from numpy import maximum, zeros
from numpy.random import randint


# эта функция считает окно и записывает результат в массив C
# и имеет блокировку ячейки этого массива, то есть когда поток закончит считать
# он освободит блокировку и работу начнет другой поток
def worker(P, C, state, i_locker):
    n = len(P)
    while True:
        with i_locker:
            i = state["step"]
            state["step"] += 1
        if i >= n:
            break

        C[i] = P[max(0, i - 1) : min(n, i + 2)].sum()


def build_c_thread(A, B, num_threads):
    P = maximum(A, 0) + maximum(B, 0)
    C = zeros(len(P), dtype=int)

    state = {"step": 0}
    i_locker = Lock()

    threads = [
        Thread(target=worker, args=(P, C, state, i_locker)) for _ in range(num_threads)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return C


if __name__ == "__main__":
    A = randint(-10, 10, 10)
    B = randint(-10, 10, 10)
    print(A, B, build_c_thread(A, B, 5), sep="\n")
