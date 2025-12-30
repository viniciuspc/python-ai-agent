import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
  try:
    working_dir_abs = os.path.abspath(working_directory)
    absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

    # Will be True or False
    valid_file_path = os.path.commonpath([working_dir_abs, absolute_file_path]) == working_dir_abs

    if not valid_file_path:
      return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
      
    if not os.path.isfile(absolute_file_path):
      return f'Error: "{file_path}" does not exist or is not a regular file'
      
    if not absolute_file_path.endswith(".py"):
      return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", absolute_file_path]
    
    if args:
      command.extend(args)
      
    completed_process = subprocess.run(command, capture_output=True, text=True)
    
    if completed_process.returncode != 0:
      return f"Process exited with code {completed_process.returncode}"
    
    if not completed_process.stdout and not completed_process.stderr:
      return "No output produced"
    
    return f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"

  except Exception as e:
    return f"Error: executing Python file: {e}"
  
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run the python file with the optional args in a specified file path relative to the working directory, providing STDOUT and STDERR of the command executed",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the python script to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="A list or arguments to be send to the python file",
                items=types.Schema(
                  type=types.Type.STRING,
                  description="An specific argument to be send to the python file"
                )
            ),
        },
        required=["file_path"]
    ),
)