from cx_Freeze import setup, Executable

setup(name="Morpyon",
      version="1.0",
      description="Mor Py On",
      executables=[Executable(script="GUI.py", base = "Win32GUI",)])