from dataclasses import dataclass
from typing import Optional, Union

from statsapi.models.seasons import Season
from statsapi.models.sports import Sport

@dataclass
class LeagueRecord:
    wins: int
    losses: int
    pct: str
    ties: Optional[int] = None


@dataclass(repr=False)
class League:
    id: int
    link: str
    name: Optional[str] = None
    abbreviation: Optional[str] = None
    nameshort: Optional[str] = None
    seasonstate: Optional[str] = None
    haswildcard: Optional[bool] = None
    hassplitseason: Optional[bool] = None
    numgames: Optional[int] = None
    hasplayoffpoints: Optional[bool] = None
    numteams: Optional[int] = None
    numwildcardteams: Optional[int] = None
    seasondateinfo: Optional[Union[Season,dict]] = None
    season: Optional[str] = None
    orgcode: Optional[str] = None
    conferencesinuse: Optional[bool] = None
    divisionsinuse: Optional[bool] = None
    sport: Optional[Union[Sport, dict]] = None
    sortorder: Optional[int] = None
    active: Optional[bool] = None

    def __post_init__(self):
        self.seasondateinfo = Season(**self.seasondateinfo) if self.seasondateinfo else self.seasondateinfo
        self.sport = Sport(**self.sport) if self.sport else self.sport

    def __repr__(self) -> str:
        kws = [f'{key}={value}' for key, value in self.__dict__.items() if value is not None and value]
        return "{}({})".format(type(self).__name__, ", ".join(kws))