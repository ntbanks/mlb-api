from dataclasses import dataclass
from typing import Optional

@dataclass(repr=False)
class Season:
    seasonid: str
    haswildcard: Optional[bool] = None
    preseasonstartdate: Optional[str] = None
    preseasonenddate: Optional[str] = None
    seasonstartdate: Optional[str] = None
    springstartdate: Optional[str] = None
    springenddate: Optional[str] = None
    regularseasonstartdate: Optional[str] = None
    lastdate1sthalf: Optional[str] = None
    allstardate: Optional[str] = None
    firstdate2ndhalf: Optional[str] = None
    regularseasonenddate: Optional[str] = None
    postseasonstartdate: Optional[str] = None
    postseasonenddate: Optional[str] = None
    seasonenddate: Optional[str] = None
    offseasonstartdate: Optional[str] = None
    offseasonenddate: Optional[str] = None
    seasonlevelgamedaytype: Optional[str] = None
    gamelevelgamedaytype: Optional[str] = None
    qualifierplateappearances: Optional[float] = None
    qualifieroutspitched: Optional[int] = None

    def __repr__(self) -> str:
        kws = [f'{key}={value}' for key, value in self.__dict__.items() if value is not None and value]
        return "{}({})".format(type(self).__name__, ", ".join(kws))