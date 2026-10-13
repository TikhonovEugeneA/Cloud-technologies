from numpy import zeros
from numpy.random import randint
from threading import Thread, Lock


def generate_numeric_array(low: int, max: int, size: int):
    return randint(low, max, size)


def assert_same_length(*arrays):
    n = len(arrays[0])
    for a in arrays[1:]:
        if len(a) != n:
            raise ValueError(f"Массивы разной длины: {n} != {len(a)}")


def compute(A, B, C, start, end):
    n = len(A)
    for i in range(start, end):
        s = 0
        for j in (i - 1, i, i + 1):
            if 0 <= j < n:
                if A[j] > 0:
                    s += A[j]
                if B[j] > 0:
                    s += B[j]
        C[i] = s


def find_edges(num_threads: int, size: int):
    edges = []
    for i in range(num_threads + 1):
        edges.append((size * i) // num_threads)
    return edges


def build_c_thread(A, B, num_threads: int):

    assert_same_length(A, B)

    size = len(A)
    C = zeros(size, dtype=int)

    edges = find_edges(num_threads, size)

    threads = []
    for t in range(num_threads):
        start = edges[t]
        end = edges[t + 1]

        if start >= end:
            continue

        thread = Thread(target=compute, args=(A, B, C, start, end))
        threads.append(thread)
        thread.start()

        for thread in threads:
            thread.join()

    return C


if __name__ == "__main__":
    A = generate_numeric_array(-10, 10, 10)
    B = generate_numeric_array(-10, 10, 10)
    C = build_c_thread(A, B, num_threads=10)
    print(A, B, C, sep="\n")
