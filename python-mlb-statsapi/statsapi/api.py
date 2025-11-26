import logging
from datetime import datetime

from typing import List, Union

from statsapi.models.seasons import Season
from statsapi.models.sports import Sport
from statsapi.models.leagues import League
from statsapi.models.divisions import Division
from statsapi.models.venues import Venue
from statsapi.models.teams import Team


from .resultwrapper import APIHelper
# from . import mlb_module # wil add this later, just helper functions

class Mlb:
    def __init__(self, host: str = 'statsapi.mlb.com', logger: logging.Logger = None):
        self._api_helper_v1 = APIHelper(host, 'v1', logger)
        self._logger = logger or logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)

    def get_division(self, division_id: int, **params) -> Union[Division, None]:
        """
        Params
        division_id : int

        Example
        >>> mlb.get_division(200)
        """

        mlb_data = self._api_helper_v1.get(endpoint=f"divisions/{division_id}", ep_params=params)
        if 400 <= mlb_data.status_code <= 499:
            return None
        
        if 'divisions' in mlb_data.data and mlb_data.data['divisions']:
            for division in mlb_data.data['divisions']:
                return Division(**division)
            
    def get_divisions(self, **params) -> List[Division]:
        """
        Params
        divisionId : int
        leagueId : int
        sportId : int

        Example
        >>> mlb.get_divisions()
        """
        
        mlb_data = self._api_helper_v1.get(endpoint="divisions", ep_params=params)
        if 400 <= mlb_data.status_code <= 499:
            return []
        
        divisions = []

        if 'divisions' in mlb_data.data and mlb_data.data['divisions']:
            divisions = [Division(**d) for d in mlb_data.data['divisions']]

        return divisions

    def get_leagues(self, **params):
        """
        params
        sportId : int
        season : int or [int]
        leagueIds : int or [int]

        example:
        leagues_params = {
            'sportId': 1,
            'season': 2025,
            'leagueIds': [103,104]
        }
        leagues = get_leagues(**leagues_params)
        """
        
        mlb_data = self._api_helper_v1.get(endpoint="leagues", ep_params=params)
        if 400 <= mlb_data.status_code <= 499:
            return []

        leagues = []

        if 'leagues' in mlb_data.data and mlb_data.data['leagues']:
            leagues = [League(**l) for l in mlb_data.data['leagues']]

        return leagues

    def get_sport(self, sport_id: int = 1, **params) -> Union[Sport, None]:
        """
        Params
        sport_id : int
        """
        mlb_data = self._api_helper_v1.get(endpoint=f"sports/{sport_id}", ep_params=params)

        if 400 <= mlb_data.status_code <= 499:
            return None
        
        if 'sports' in mlb_data.data and mlb_data.data['sports']:
            for sport in mlb_data.data['sports']:
                return Sport(**sport)


    def get_season(self, season_id: str = datetime.today().year, sport_id: int = 1, **params) -> Season:
        """
        Params
        sport_id : int
        season_id : str

        Other
        withGameTypeDates : bool

        Examples
        >>> mlb = Mlb()
        >>> mlb.get_season()
        >>> mlb.get_season(season_id="2021", sport_id=1)
        """
        if sport_id is not None:
            params['sportId'] = sport_id

        mlb_data = self._api_helper_v1.get(endpoint=f'seasons/{season_id}', ep_params=params)

        if 400 <= mlb_data.status_code <= 499:
            return None
        
        if 'seasons' in mlb_data.data and mlb_data.data['seasons']:
            for season in mlb_data.data['seasons']:
                return Season(**season)
            

    def get_venue(self, venue_id: int, **params) -> Union[Venue, None]:
        """
        params
        venue_id : int
        """
        params['hydrate'] = ['location', 'fieldInfo', 'timezone']

        mlb_data = self._api_helper_v1.get(endpoint=f'venues/{venue_id}', ep_params=params)
        if 400 <= mlb_data.status_code <= 499:
            return None
        
        if 'venues' in mlb_data.data and mlb_data.data['venues']:
            for venue in mlb_data.data['venues']:
                return Venue(**venue)
            

    def get_venues(self, **params) -> Union[Venue, None]:
        """
        params
        venueIds : int, List[int]
        sportIds : int, List[int]
        season : int
        """
        params['hydrate'] = ['location', 'fieldInfo', 'timezone']

        mlb_data = self._api_helper_v1.get(endpoint='venues', ep_params=params)
        if 400 <= mlb_data.status_code <= 499:
            return []
        
        venues = []

        if 'venues' in mlb_data.data and mlb_data.data['venues']:
            venues = [Venue(**venue) for venue in mlb_data.data['venues']]
                
        return venues
    
    # sox are 111 
    def get_team(self, team_id: int = 111, **params) -> Union[Team, None]:
        """
        params
        team_id : int

        other
        season : int
        sportId : int
        hydrate : str
            available hydrations
            -----
            previousSchedule
            nextSchedule
            venue
            social
            deviceProperties
            game(promotions)
            game(atBatPromotions)
            game(tickets)
            game(atBatTickets)
            game(sponsorships)
            league
            person
            sport
            division
        """

        mlb_data = self._api_helper_v1.get(endpoint=f'teams/{team_id}', ep_params=params)
        if 400 <= mlb_data.status_code <= 499:
            return None
        
        if 'teams' in mlb_data.data and mlb_data.data['teams']:
            for team in mlb_data.data['teams']:
                return Team(**team)
        

    def get_teams(self, sport_id: int = 1, **params) -> List[Team]:
        """
        params
        sport_id : int

        other
        season : int
        leagueIds : int or List[int]
        activeStatus : str (Y, N or B)
        allStarStatuses: str (Y or N)
        sportIds : int
        gameType : str
        hydrate : str
            available hydrations
            -----
            previousSchedule
            nextSchedule
            venue
            social
            deviceProperties
            game(promotions)
            game(atBatPromotions)
            game(tickets)
            game(atBatTickets)
            game(sponsorships)
            league
            person
            sport
            division
        """
        params['sportId'] = sport_id

        mlb_data = self._api_helper_v1.get(endpoint="teams", ep_params=params)
        if 400 <= mlb_data.status_code <= 499:
            return []
        
        teams = []

        if 'teams' in mlb_data.data and mlb_data.data['teams']:
            teams = [Team(**t) for t in mlb_data.data['teams']]

        return teams
    

    def get_team_id(self, search_term: str, **params) -> List[int]:
        """
        params
        search_term : str

        other
        sportId
        """
        mlb_data = self._api_helper_v1.get(endpoint="teams", ep_params=params)
        if 400 <= mlb_data.status_code <= 499:
            return []
        
        team_ids = []

        if 'teams' in mlb_data.data and mlb_data.data['teams']:
            for team in mlb_data.data['teams']:
                if team['name'].lower() == search_term.lower():
                    team_ids.append(team['id'])
        
        return team_ids