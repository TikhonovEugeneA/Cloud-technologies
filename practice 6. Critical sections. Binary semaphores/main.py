from threading import Thread, Lock, Semaphore
from time import sleep
from numpy import maximum, zeros
from numpy.random import randint
from collections import deque


def worker(thread_id, P, C, state, mutex, semaphore: Semaphore, queue: deque):
    n = len(P)
    while True:
        with mutex:
            i = state["step"]
            state["step"] += 1
        if i >= n:
            break

        C[i] = P[max(0, i - 1) : min(n, i + 2)].sum()
        sleep(0.01)
        with semaphore:
            queue.append((thread_id, i, int(C[i])))


def build_c_thread(A, B, num_threads):
    P = maximum(A, 0) + maximum(B, 0)
    C = zeros(len(P), dtype=int)

    state = {"step": 0}
    mutex = Lock()
    semaphore = Semaphore(1)
    queue = deque()

    threads = [
        Thread(target=worker, args=(t + 1, P, C, state, mutex, semaphore, queue))
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
    C, queue = build_c_thread(A, B, 5)

    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("Очередь результатов (поток, индекс, значение)")
    while queue:
        print(queue.popleft())
