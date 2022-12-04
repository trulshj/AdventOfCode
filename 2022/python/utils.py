from time import time


def print_day(day, part1_func, part2_func, data):
    part1_time, part1_result = time_function(part1_func, data)
    part2_time, part2_result = time_function(part2_func, data)

    print(f"🎄 Day {day:02} 🎄")
    print("⭐ Part 1 ⭐")
    print(f"{part1_result} (elapsed {part1_time}μs)")
    print("⭐ Part 2 ⭐")
    print(f"{part2_result} (elapsed {part2_time}μs)")


def time_function(function, data):
    """Runs a function on the given data and returns the elapsed time"""
    start_time = time()
    result = function(data)
    return round((time() - start_time) * 1e6, 2), result
