class MlbStatsApiException(Exception):
    def __init__(self):
        message='custom exception boiiiii'
        super().__init__(message)