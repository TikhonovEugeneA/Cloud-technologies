from numpy import maximum, zeros, array_split, arange
from numpy.random import randint
from threading import Thread


def compute(P, C, start, end):
    n = len(P)
    for i in range(start, end):
        C[i] = P[max(0, i - 1) : min(n, i + 2)].sum()


def build_c_thread(A, B, num_threads):

    P = maximum(A, 0) + maximum(B, 0)
    C = zeros(len(P), dtype=int)

    threads = []
    for chunk in array_split(arange(len(P)), num_threads):
        if len(chunk):
            t = Thread(target=compute, args=(P, C, chunk[0], chunk[-1] + 1))
            t.start()
            threads.append(t)

    for t in threads:
        t.join()
    return C


if __name__ == "__main__":
    A = randint(-10, 10, 10)
    B = randint(-10, 10, 10)
    print(A, B, build_c_thread(A, B, num_threads=5), sep="\n")
