from pathlib import Path
from lupa import LuaRuntime
from src.file_utilities.file_navigator import FileNavigator

def resolve_lua(**global_vars):
    lua = LuaRuntime(unpack_returned_tuples=True)

    lua_root = FileNavigator.find_folder("lua")

    lua.execute(
        f'package.path = package.path .. ";{lua_root}/?.lua;{lua_root}/?/init.lua"'
    )

    for name, value in global_vars.items():
        lua.globals()[name] = value

    return lua