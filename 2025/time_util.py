import time


class Timer:
    def __init__(self):
        self.start_time = 0.0
        self.end_time = 0.0

    def start(self):
        self.start_time = time.perf_counter()
        return self

    def stop(self):
        self.end_time = time.perf_counter()
        return self

    def print(self):
        elapsed_time = self.end_time - self.start_time
        print(f"Execution time: {elapsed_time:.4f} seconds")
        return self


def start_timer():
    return Timer().start()
