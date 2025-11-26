from dataclasses import dataclass
from typing import Optional

@dataclass(repr=False)
class Sport:
    id: int
    link: str
    name: Optional[str] = None
    code: Optional[str] = None
    abbreviation: Optional[str] = None
    sortorder: Optional[int] = None
    activestatus: Optional[bool] = None

    def __repr__(self) -> str:
        kws = [f'{key}={value}' for key, value in self.__dict__.items() if value is not None and value]
        return "{}({})".format(type(self).__name__, ", ".join(kws))