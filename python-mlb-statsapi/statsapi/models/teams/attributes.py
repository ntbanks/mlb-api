from dataclasses import dataclass
from typing import Optional, Union, List

from statsapi.models.divisions import Division
from statsapi.models.leagues import League

@dataclass
class Record:
    wins: int
    losses: int
    pct: str

@dataclass
class OverallLeagueRecord(Record):
    """
    attributes
    wins: int
    losses: int
    pct: str
    ties: int
    """
    ties: int

@dataclass
class TypeRecords(Record):
    """
    attributes
    wins: int
    losses: int
    pct: str
    type: str
    """
    type: str

@dataclass
class DivisionRecords(Record):
    """
    attributes
    wins: int
    losses: int
    pct: str
    division: Division
    """
    division: Union[Division, dict]

@dataclass
class LeagueRecords(Record):
    """
    attributes
    wins: int
    losses: int
    pct: str
    league: League
    """
    league: Union[League, dict]

@dataclass(repr=False)
class Records:
    splitrecords: Optional[List[Union[TypeRecords, dict]]] = None
    divisionrecords: Optional[List[Union[DivisionRecords, dict]]] = None
    overallrecords: Optional[List[Union[TypeRecords, dict]]] = None
    leaguerecords: Optional[List[Union[LeagueRecords, dict]]] = None
    expectedrecords: Optional[List[Union[TypeRecords, dict]]] = None

    def __post_init__(self):
        self.splitrecords = [TypeRecords(**splitrecord) for splitrecord in self.splitrecords] if self.splitrecords else None
        self.divisionrecords = [DivisionRecords(**divisionrecord) for divisionrecord in self.divisionrecords] if self.divisionrecords else None
        self.overallrecords = [TypeRecords(**overallrecord) for overallrecord in self.overallrecords] if self.overallrecords else None
        self.leaguerecords = [LeagueRecords(**leaguerecord) for leaguerecord in self.leaguerecords] if self.leaguerecords else None
        self.expectedrecords = [TypeRecords(**expectedrecord) for expectedrecord in self.expectedrecords] if self.expectedrecords else None

    def __repr__(self) -> str:
        kws = [f'{key}={value}' for key, value in self.__dict__.items() if value is not None]
        return "{}({})".format(type(self).__name__, ", ".join(kws))
    
@dataclass(repr=False)
class TeamRecord:
    gamesplayed: int
    wildcardgamesback: str
    leaguegamesback: str
    springleaguegamesback: str
    sportgamesback: str
    divisiongamesback: str
    conferencegamesback: str
    leaguerecord: Union[OverallLeagueRecord, dict]
    records: Union[Records, dict]
    divisionleader: bool
    wins: int
    losses: int
    winningpercentage: str
    
    def __post_init__(self):
        self.leaguerecord = OverallLeagueRecord(**self.leaguerecord)
        self.records = Records(**self.records)

    def __repr__(self) -> str:
        kws = [f'{key}={value}' for key, value in self.__dict__.items() if value is not None]
        return "{}({})".format(type(self).__name__, ", ".join(kws))