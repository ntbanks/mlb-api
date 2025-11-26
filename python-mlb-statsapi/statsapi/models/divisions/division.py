from dataclasses import dataclass
from typing import Optional, Union

from statsapi.models.leagues import League
from statsapi.models.sports import Sport

@dataclass(repr=False)
class Division:
    id: int
    link: str
    name: Optional[str] = None
    season: Optional[str] = None
    nameshort: Optional[str] = None
    abbreviation: Optional[str] = None
    league: Optional[Union[League, dict]] = None
    sport: Optional[Union[Sport, dict]] = None
    haswildcard: Optional[bool] = None
    sortorder: Optional[int] = None
    numplayoffteams: Optional[int] = None
    active: Optional[bool] = None

    def __post_init__(self):
        self.league = League(**self.league) if self.league else self.league
        self.sport = Sport(**self.sport) if self.sport else self.sport

    def __repr__(self) -> str:
        kws = [f'{key}={value}' for key, value in self.__dict__.items() if value is not None and value]
        return "{}({})".format(type(self).__name__, ", ".join(kws))