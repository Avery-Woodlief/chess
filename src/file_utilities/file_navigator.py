import collections
from pathlib import Path
import platform
from types import NoneType
import json
import traceback

def _flatten(seq ) -> tuple:
    res = ()
    for item in seq:
        if isinstance(item, (tuple, list)):
            res = res + _flatten(item)
        else:
            res = res + (item,)

    return res

def box_text(text : str | tuple | list, box_char = "|", floor_char = "_", indent_lvl=0, max_width=None) -> str:
    if isinstance(text, str):
        text_length = len(text)
    elif isinstance(text, (tuple, list)):
        text = list(_flatten(text))
        text_length = max(len(item) for item in text)
    else:
        return f"ERROR: TEXT IN box_text failed because bad instance of text, got: {type(text)}"
    if max_width:
        text_length = max_width
    boxed_ = ""
    boxed_ += str("\t" * indent_lvl) + " " + str(floor_char * text_length) + " " + "\n"
    boxed_ += str("\t" * indent_lvl) + box_char + str(" " * text_length) + box_char + "\n"
    if isinstance(text, str):
        boxed_ += str("\t" * indent_lvl) + box_char + text + box_char + "\n"
    else:
        for item in text:
            boxed_ += str("\t" * indent_lvl) + box_char + str(item) + str(" " * (text_length-len(item))) + box_char + "\n"
    boxed_ += str("\t" * indent_lvl) + box_char + str(floor_char * text_length) + box_char
    return boxed_

def get_project_dir(project_name : str):
    this_file = Path(__file__).resolve()
    while this_file.parents[1].stem != project_name:
        #print(this_file.parents[1])
        this_file = this_file.parent
    return this_file.parents[1].resolve()

PROJECT_ROOT = get_project_dir("chess")
IGNORED_DIRS = [".venv",
                "build",
                "dist",
                "__pycache__/"]
IGNORED_FILES = ["__init__.py"]

class FileNavigator:
    def __init__(self, **kw):
        pass
    @staticmethod
    def find_folder(folder_name : str) -> Path | NoneType:
        """

        :param folder_name: name of folder relative to project root
        :return: Path instance of the folder
        """

        root = PROJECT_ROOT
        if folder_name == "PROJECT_DIR":
            return root
        folders_in_root = [directory.resolve() for directory in root.rglob(folder_name)
                           if directory.is_dir() and not any(part in IGNORED_DIRS for part in directory.parts)]
        hit = None
        for folder in folders_in_root:
            if folder.stem == folder_name:
                hit = folder
                break
        return hit

    @staticmethod
    def find_file(folder_name : str, file_name : str) -> Path:
        """

        :param folder_name: str
        :param file_name: str
        :return: Path instance of file location if exists, raises ValueError otherwise
        """
        using_suffix = "." in file_name and file_name.index(".") > 0

        hit = FileNavigator.find_folder(folder_name)
        if hit:
            contents = [f.resolve() for f in hit.rglob("*")
                        if f.is_file() and (not any(((part in IGNORED_DIRS) or (part in IGNORED_FILES)) for part in f.parts))]
            if not any(file_name == (f.stem + (f.suffix if using_suffix else "")) for f in contents):
                raise ValueError(f"{folder_name} is valid directory in {PROJECT_ROOT}, but {file_name} is not relative to it")
            for f in contents:
                if file_name == (f.stem + (f.suffix if using_suffix else "")):
                    return f
        else:
            if not (folder_name in IGNORED_DIRS):
                raise ValueError(f"{folder_name} does not exist in the scope of {PROJECT_ROOT}")
            else:
                raise ValueError(f"{folder_name} is explicitly ignored, c.f. 'IGNORED_DIRS' in {__file__}")

    @staticmethod
    def grab(folder_name : str, file_name : str) -> list | dict | NoneType:
        """

        :param folder_name:
        :param file_name:
        :return:
        """
        try:
            f = FileNavigator.find_file(folder_name, file_name)
            if not ".json" in file_name:
                return f.read_text(encoding="utf-8", errors="replace").split("\n")
            else:
                return json.load(f.open(mode="r", encoding="utf-8", errors="replace"))
        except ValueError as e:
            return None

    @staticmethod
    def write(folder_name : str, file_name : str, contents = None, join_str="\n") -> None:
        """

        :param folder_name:
        :param file_name:
        :param contents:
        :param join_str:
        :return:
        """
        try:
            f = FileNavigator.find_file(folder_name, file_name)
            extension = f.suffix
            if contents and extension==".json":
                with open(file=f, mode="w", encoding="utf-8", errors="replace") as _file:
                    json.dump(contents, _file, indent=4)
            elif contents and extension==".txt":
                resolved_contents = str(contents) if not isinstance(contents, (list, tuple)) else join_str.join(contents)
                f.write_text(resolved_contents, encoding="utf-8", errors="replace")
            else:
                print(__file__)
        except ValueError as e:
            message = [box_text(["EXCEPTION OCCURED", str(type(e))]), traceback.format_exc(),
                       box_text(["END EXCEPTION"])]
            FileNavigator.append("logs", "output.txt", message)
            return None

    @staticmethod
    def append(folder_name : str, file_name : str, contents = None, join_str="\n", newline=True) -> None:
        """

        :param folder_name:
        :param file_name:
        :param contents:
        :param join_str:
        :param newline:
        :return:
        """
        try:
            f = FileNavigator.find_file(folder_name, file_name)
            extension = f.suffix
            _file = f.open(mode="a", encoding="utf-8", errors="replace")
            if contents and extension==".json":
                json.dump(contents, _file, indent=4)
            elif contents and extension==".txt":
                resolved_contents = str(contents) if not isinstance(contents, (list, tuple)) else join_str.join(contents)
                if newline:
                    existing_content = FileNavigator.grab(folder_name, file_name)
                    existing_content.append(resolved_contents)
                    FileNavigator.write(folder_name, file_name, existing_content)
                else:
                    _file.write(resolved_contents)
            else:
                print(__file__)
        except Exception as e:
            message = [box_text(["EXCEPTION OCCURED", str(type(e))]), traceback.format_exc(), box_text(["END EXCEPTION"])]
            FileNavigator.append("logs", "output.txt", message)
            return None

if __name__ == "__main__":
    #FileNavigator.write("logs", "output.xlsx", ["hello", "world"])
    FileNavigator.append("logs", "output.xlsx", "test appended message")