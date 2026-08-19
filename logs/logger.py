from typing import Any

from src.file_utilities.file_navigator import *
class Logger:
    @staticmethod
    def write_to_logs(e : Exception, extra_message : Any) -> None:
        message = [box_text(["EXCEPTION OCCURED", str(type(e))])]
        message.append(traceback.format_exc())

        if isinstance(extra_message, (list, tuple)):
            resolved_contents = extra_message
        elif isinstance(extra_message, str):
            resolved_contents = extra_message.split("\n")
        else:
            resolved_contents = []
        message.extend(resolved_contents)
        message.append(box_text(["END EXCEPTION"]))
        FileNavigator.append("logs", "output.txt", message)

if __name__ == "__main__":
    a = ()
    try:
        a += "1"
    except Exception as e:
        Logger.write_to_logs(e, "extra message")