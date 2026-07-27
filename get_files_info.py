import os
from functools import reduce
from unittest import result


def get_files_info(working_directory: str, directory: str = ".") -> str:

    working_dir_abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs_path, directory))
    validation = (
        os.path.commonpath((target_dir, working_dir_abs_path)) == working_dir_abs_path
    )

    if not validation:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    else:
        print(f'Success: "{directory}" is within the working directory')
    file_list = os.listdir(target_dir)
    result_dict = {}
    for elem in file_list:
        elem_fullpath = os.path.join(target_dir, elem)
        result_dict[elem] = (
            f"\n - {elem}: file_size={os.path.getsize(elem_fullpath)} bytes, is_dir={os.path.isdir(elem_fullpath)}"
        )
    final_string = "Result for current directory:"
    for v in result_dict.values():
        final_string += v
    return final_string
