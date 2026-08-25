import logging
import traceback
from collections import OrderedDict

from src.file_utilities.file_navigator import FileNavigator


class ChessLogger:

    call_counter = 0
    areas = OrderedDict()
    log_path = FileNavigator.find_folder("logs") / "debug.log"
    level=logging.DEBUG
    formatter = logging.Formatter("%(asctime)s | %(levelname)s")
    INFO = logging.INFO
    ERROR = logging.ERROR
    DEBUG = logging.DEBUG

    @staticmethod
    def log(
        area: str,
        message: str = "",
        level=logging.INFO,
        exception: Exception | None = None
    ):
        ChessLogger.call_counter += 1
        area = area.upper()

        if area not in ChessLogger.areas:
            ChessLogger.areas[area] = []

        record = logging.LogRecord(
            name="chess",
            level=level,
            pathname="",
            lineno=0,
            msg=message,
            args=(),
            exc_info=None
        )

        formatter_message = ChessLogger.formatter.format(record)

        entry = (
            f"{formatter_message} | CALL ({ChessLogger.call_counter})\n"
            f"{message}"
        )

        if exception is not None:
            entry += ChessLogger._format_exception(exception)

        ChessLogger.areas[area].append(entry)

        ChessLogger._write()

    @staticmethod
    def _format_exception(exception):
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

    @staticmethod
    def _write():
        with open(ChessLogger.log_path, "w", encoding="utf-8") as file:

            for area, entries in ChessLogger.areas.items():
                file.write(
                    f"AREA: {area} | chess\n"
                )

                for entry in entries:
                    file.write(
                        f"{entry}\n"
                    )

                file.write("\n")