import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    """working directory"""
    working_dir_abs_path = os.path.abspath(working_directory)
    target = os.path.normpath(os.path.join(working_dir_abs_path, file_path))
    validation = (
        os.path.commonpath((target, working_dir_abs_path)) == working_dir_abs_path
    )

    if not validation:
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    else:
        print(f'Success: "{file_path}" is within the working directory')
    exist_ok = True
    os.makedirs(os.path.dirname(target), exist_ok=exist_ok)
    mode = "w" if os.path.isfile(target) else "x"
    with open(mode=mode, file=target) as f:
        try:
            f.write(content)
        except Exception as e:
            print("Error: trying to write file ", e)
            return ""
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
