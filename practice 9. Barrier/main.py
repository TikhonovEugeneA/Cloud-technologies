from threading import Thread, Barrier
from numpy.random import randint


def generate_random_numerical_array(low, high, size):
    return randint(low, high, size)


def condition(A, B):
    return set(A) == set(B)


def worker(idx, size, arrays, barrier, state):
    while True:
        arrays[idx] = generate_random_numerical_array(0, 10, size)
        barrier.wait()
        if state["done"]:
            break


def same_assert(size):
    arrays = [None, None]
    state = {"done": False}

    def check():
        state["done"] = condition(arrays[0], arrays[1])

    barrier = Barrier(2, action=check)

    threads = [
        Thread(target=worker, args=(t, size, arrays, barrier, state)) for t in range(2)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    with open("practice_9.txt", "w") as file:
        print(arrays[0], arrays[1], sep="\n", file=file)


if __name__ == "__main__":
    same_assert(5)
