from random import randint
from time import time
from math import log10
from statistics import mean, median


def total_digits_str_conversion(numbers: list[int]):
    total_digits = 0
    for number in numbers:
        total_digits += len(str(number))
    return total_digits


def total_digits_logarithm(numbers: list[int]):
    total_digits = 0
    for number in numbers:
        total_digits += int(log10(number)) + 1
    return total_digits


def time_function(function, numbers):
    start_time = time()
    result = function(numbers)
    end_time = time() - start_time
    return result, end_time


def main():
    MIN_NUMBER = 1
    MAX_NUMBER = 1_000_000
    NUMBER_AMOUNT = 10_000_000
    RUN_AMOUNT = 10
    ROUNDING = 3

    number_start_time = time()
    print(f"Creating list of {NUMBER_AMOUNT} numbers...")
    numbers = [randint(MIN_NUMBER, MAX_NUMBER) for _ in range(NUMBER_AMOUNT)]
    number_end_time = time() - number_start_time
    print(f"Took {round(number_end_time, ROUNDING)} seconds\n")

    print("--- String Conversion Method ---")
    times = []
    for i in range(RUN_AMOUNT):
        result, end_time = time_function(total_digits_str_conversion, numbers)
        times.append(end_time)
        print(f"Run {i}: Found result {result} in {
              round(end_time, ROUNDING)} seconds")
    print(f"Mean: {round(mean(times), ROUNDING)}, Median: {
          round(median(times), ROUNDING)}")

    print("\n--- Logarithm Method ---")
    times = []
    for i in range(RUN_AMOUNT):
        result, end_time = time_function(total_digits_logarithm, numbers)
        times.append(end_time)
        print(f"Run {i}: Found result {result} in {
              round(end_time, ROUNDING)} seconds")
    print(f"Mean: {round(mean(times), ROUNDING)}, Median: {
          round(median(times), ROUNDING)}")
    print()


if __name__ == "__main__":
    main()
