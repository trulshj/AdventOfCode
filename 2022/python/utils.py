from time import time


def print_day(day, part1_func, part2_func, get_data_func):
    part1_time, part1_result = time_function(part1_func, get_data_func)
    part2_time, part2_result = time_function(part2_func, get_data_func)

    print(f"🎄 Day {day:02} 🎄")
    print("⭐ Part 1 ⭐")
    print(f"{part1_result} (elapsed {part1_time})")
    print("⭐ Part 2 ⭐")
    print(f"{part2_result} (elapsed {part2_time})")


def time_function(function, get_data_func):
    """Runs a function on the given data and returns the elapsed time"""
    data = get_data_func()
    start_time = time()
    result = function(data)
    return format_time(time() - start_time), result


def format_time(time):
    units = ["s", "ms", "μs", "ns", "ps", "fs", "as", "?", "???"]
    power = 0

    while time < 1 and power < len(units):
        time *= 1000
        power += 1

    return f"{round(time, 2)}{units[power]}"
