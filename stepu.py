from cx_Freeze import setup, Executable

import os

asset_list_completa = [
    ("asset", "asset")
]

executable = [Executable("main.py")]

files = {
    "include_files": asset_list_completa,
    "packages": ["pygame"]
}

setup(
    name="Everest",
    version="1.0",
    description="Everest app game",
    options={"build_exe": files},
    executables=executable
)