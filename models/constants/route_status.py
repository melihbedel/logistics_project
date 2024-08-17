from enum import Enum

class RouteStatus(Enum):
    PENDING = 'pending'
    DEPARTED = 'departed'
    COMPLETED = 'completed'
        