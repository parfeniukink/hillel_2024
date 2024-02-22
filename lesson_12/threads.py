import string
import random
import time
from threading import Thread

# from multiprocessing import Process


def cpu_bound(n):
    items: list[str] = []
    for i in range(n):
        word = "".join([random.choice(string.ascii_letters) for _ in range(3)])

        items.append(word)

    del items


def io_bound(n):
    time.sleep(n)


def sequential():
    cpu_bound(1_000_000)
    cpu_bound(2_000_000)


def using_threads():
    threads: list[Thread] = [
        Thread(target=cpu_bound, args=(1_000_000,)),
        Thread(target=cpu_bound, args=(2_000_000,)),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start = time.perf_counter()

    # sequential()
    using_threads()

    print(f"Total: {time.perf_counter() - start}")
