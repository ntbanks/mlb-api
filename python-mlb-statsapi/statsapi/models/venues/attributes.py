from typing import Optional, Union
from dataclasses import dataclass, field

@dataclass
class VenueDefaultCoordinates:
    latitude: float
    longitude: float


@dataclass(repr=False)
class Location:
    city: str
    country: str
    stateabbrev: Optional[str] = None
    address1: Optional[str] = None
    state: Optional[str] = None
    postalcode: Optional[str] = None
    phone: Optional[str] = None
    address2: Optional[str] = None
    address3: Optional[str] = None
    azimuthangle: Optional[str] = None
    elevation: Optional[str] = None
    defaultcoordinates: Optional[Union[VenueDefaultCoordinates, dict]] = field(default_factory=dict)

    def __post_init__(self):
        self.defaultcoordinates = VenueDefaultCoordinates(**self.defaultcoordinates) if self.defaultcoordinates else self.defaultcoordinates
    
    def __repr__(self) -> str:
        kws = [f'{key}={value}' for key, value in self.__dict__.items() if value is not None and value]
        return "{}({})".format(type(self).__name__, ", ".join(kws))
    

@dataclass
class TimeZone:
    id: str
    offset: int
    tz: str
    offsetatgametime: Optional[int] = None


@dataclass(repr=False)
class FieldInfo:
    capacity: Optional[int] = None
    turftype: Optional[str] = None
    rooftype: Optional[str] = None
    leftline: Optional[int] = None
    left: Optional[int] = None
    leftcenter: Optional[int] = None
    center: Optional[int] = None
    rightcenter: Optional[int] = None
    right: Optional[int] = None
    rightline: Optional[int] = None


    def __repr__(self) -> str:
        kws = [f'{key}={value}' for key, value in self.__dict__.items() if value is not None and value]
        return "{}({})".format(type(self).__name__, ", ".join(kws))