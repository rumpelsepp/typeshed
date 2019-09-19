# Stubs for maxminddb.decoder (Python 3)

from typing import Any, Tuple

class Decoder:
    def __init__(self, database_buffer: bytes, pointer_base: int = ..., pointer_test: bool = ...) -> None: ...
    def decode(self, offset: int) -> Tuple[Any, int]: ...