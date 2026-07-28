import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "run a python file in a specific directory relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file path to list files from, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "list of strings or None",
                    "description": "extra arguments for de command line run python [optional args]",
                },
            },
        },
    },
}


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    if file_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file'
    # 30 second timeout
    #
    working_dir_abs_path = os.path.abspath(f"{working_directory}")
    target_file = os.path.normpath(os.path.join(working_dir_abs_path, file_path))
    validation = (
        os.path.commonpath((target_file, working_dir_abs_path)) == working_dir_abs_path
    )
    if not validation:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error:"{file_path}" does not exist'
    command = ["python", target_file]
    if args != None:
        command.extend(args)
    try:
        process = subprocess.run(command, capture_output=True, check=True, timeout=31)
    except Exception as e:
        return f"f exception:{e}"
    if process.returncode != 0:
        return f"Process exited with code{process.returncode}"
    if process.stderr != "" or process.stdout != "":
        return f"STDOUT: {process.stdout} STDERR: {process.stderr}"
    return "No output produced"
