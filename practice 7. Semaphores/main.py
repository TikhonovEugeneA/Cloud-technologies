from collections import deque
from threading import Semaphore, Thread
from time import sleep

from numpy import arange, array_split, maximum, zeros
from numpy.random import randint


def worker(thread_id, P, C, indices, sem_queue, sem_limit, queue):
    n = len(P)
    with sem_limit:
        print(f"Поток {thread_id} вошёл")
        for i in indices:
            C[i] = P[max(0, i - 1) : min(n, i + 2)].sum()
            sleep(0.01)
            with sem_queue:
                queue.append((thread_id, int(i), int(C[i])))
        print(f"Поток {thread_id} вышел")


def build_c_thread(A, B, num_threads, L):

    P = maximum(A, 0) + maximum(B, 0)
    C = zeros(len(P), dtype=int)

    sem_queue = Semaphore(1)
    sem_limit = Semaphore(L)
    queue = deque()

    parts = array_split(arange(len(P)), num_threads)
    threads = [
        Thread(
            target=worker,
            args=(t + 1, P, C, parts[t], sem_queue, sem_limit, queue),
        )
        for t in range(num_threads)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return C, queue


if __name__ == "__main__":
    A = randint(-10, 10, 10)
    B = randint(-10, 10, 10)
    L = 2

    C, queue = build_c_thread(A, B, num_threads=5, L=L)

    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("Очередь результатов (поток, индекс, значение)")
    while queue:
        print(queue.popleft())
