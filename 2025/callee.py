import inspect
import os.path
from pathlib import Path


def get_caller_info(frame=3):
    caller_frame = inspect.stack()[frame]
    caller_filename_full = caller_frame.filename

    caller_filename_only = os.path.splitext(
        os.path.basename(caller_filename_full))[0]

    return caller_filename_full, caller_filename_only


def get_input_path():
    fname_full, fname = get_caller_info()
    day = fname[-2:]
    return Path(fname_full).parent / f"input{day}.txt"
