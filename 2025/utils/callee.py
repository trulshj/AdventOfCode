import inspect
import os
import re
from pathlib import Path

DAY_RE = re.compile(r"^day(\d{2})\.py$")


def get_caller_info(max_depth: int = 5):
    frame = inspect.currentframe()
    if frame is None:
        raise RuntimeError("Could not get frame")

    try:
        frame = frame.f_back

        for _ in range(max_depth):
            if frame is None:
                break

            filename_full = frame.f_code.co_filename
            filename_only = os.path.basename(filename_full)

            match = DAY_RE.match(filename_only)
            if match:
                return filename_full, match.group(1)

            frame = frame.f_back

    finally:
        del frame

    raise RuntimeError(
        "Could not figure out which AoC day to read. "
        "Is the file following the naming scheme 'dayXX.py'?"
    )


def get_input_path():
    fname_full, day = get_caller_info()
    return Path(fname_full).parent / f"input{day}.txt"
