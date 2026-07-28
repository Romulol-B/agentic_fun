import os

# from .. import config

schema_get_files_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Read the file content in a specific directory relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "file path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}


def get_file_content(working_directory: str, file_path: str) -> str:
    MAX_CHARS = 10_000  # config.MAX_CHARS
    try:
        working_dir_abs_path = os.path.abspath(f"{working_directory}")
        target_dir = os.path.normpath(os.path.join(working_dir_abs_path, file_path))
        validation = (
            os.path.commonpath((target_dir, working_dir_abs_path))
            == working_dir_abs_path
        )
        if not validation:
            raise Exception(
                f'Error: Cannot read"{target_dir}" as it is outside the permitted working directory'
            )
        if not os.path.isfile(target_dir):
            raise Exception(
                f'Error: File not found or is not a regular file: "{target_dir}"'
            )
        # reading the file

        with open(target_dir, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return content
    except Exception as e:
        print(e)
        return ""
