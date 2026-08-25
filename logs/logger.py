import logging
import traceback
from collections import OrderedDict

from src.file_utilities.file_navigator import FileNavigator


class ChessLogger:

    def __init__(self, filename="debug.log", level=logging.DEBUG):
        self.log_path = FileNavigator.find_folder("logs") / filename
        self.level = level

        # Keeps areas in the order they were first created.
        self.areas = OrderedDict()

        self.formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s"
        )

    def log(
        self,
        area: str,
        message: str,
        level=logging.INFO,
        exception: Exception | None = None
    ):
        area = area.upper()

        if area not in self.areas:
            self.areas[area] = []

        record = logging.LogRecord(
            name="chess",
            level=level,
            pathname="",
            lineno=0,
            msg=message,
            args=(),
            exc_info=None
        )

        formatter_message = self.formatter.format(record)

        entry = (
            f"{formatter_message}\n"
            f"{message}"
        )

        if exception is not None:
            entry += self._format_exception(exception)

        self.areas[area].append(entry)

        self._write()

    def _format_exception(self, exception):
        tb = exception.__traceback__

        if tb is not None:
            final_tb = tb

            while final_tb.tb_next is not None:
                final_tb = final_tb.tb_next

            filename = final_tb.tb_frame.f_code.co_filename
            line_number = final_tb.tb_lineno

        else:
            filename = "unknown"
            line_number = "unknown"

        traceback_message = "".join(
            traceback.format_exception(
                type(exception),
                exception,
                exception.__traceback__
            )
        )

        return (
            f"\nEXCEPTION: {type(exception).__name__}"
            f"\nEXCEPTION STRING: {exception}"
            f"\nFILENAME: {filename}"
            f"\nFILE LINE: {line_number}"
            f"\nEXCEPTION TRACEBACK MESSAGE:\n"
            f"{traceback_message}"
        )

    def _write(self):
        with open(self.log_path, "w", encoding="utf-8") as file:

            for area, entries in self.areas.items():
                file.write(
                    f"AREA: {area} | chess\n"
                )

                for entry in entries:
                    file.write(
                        f"{entry}\n"
                    )

                file.write("\n")

if __name__ == "__main__":
    logs = ChessLogger()

    logs.log(
        "initialization",
        "created game board"
    )

    logs.log(
        "initialization",
        "created team 0's pieces"
    )

    logs.log(
        "movement",
        "pawn moved to (1, 3)"
    )

    logs.log(
        "initialization",
        "created team 1's pieces"
    )

    import time
    time.sleep(2)
    logs.log(
        "movement",
        "pawn moved to (1, 4)"
    )

    try:
        raise TypeError("An exception occured")
    except TypeError as e:
        logs.log(
            "movement",
            "pawn moved to (1, 5)",
            level=logging.ERROR,
            exception=e
        )