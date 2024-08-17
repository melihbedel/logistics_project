from enum import Enum


class PackageStatus(Enum):
    PENDING = 'pending'
    ASSIGNED = 'assigned'
    ON_TRACK = 'on track'
    DELIVERED = 'delivered'
