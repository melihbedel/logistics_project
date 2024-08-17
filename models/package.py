from models.constants.package_status import PackageStatus


class Package:
    def __init__(self, id, start_location, destination, weight, contact_info):
        self._id = id
        self._start_location = start_location
        self._destination = destination
        self._weight = weight
        self._contact_info = contact_info
        self._status = PackageStatus.PENDING

    @property
    def id(self):
        return self._id

    @property
    def start_location(self):
        return self._start_location


    @property
    def destination(self):
        return self._destination


    @property
    def weight(self):
        return self._weight


    @property
    def contact_info(self):
        return self._contact_info
    
    @contact_info.setter
    def contact_info(self, input):
        self._contact_info = input

    @property
    def status(self):
        return self._status

    def advance_status_to_assigned(self):
        self._status = PackageStatus.ASSIGNED

    def advance_status_to_on_track(self):
        self._status = PackageStatus.ON_TRACK

    def advance_status_to_delivered(self):
        self._status = PackageStatus.DELIVERED

    def __str__(self):
        return "\n".join([
            f'Package #{self.id}',
            f'Weight: {self.weight}kg',
            f'Start location: {self.start_location}',
            f'Destination: {self.destination}'
            ])

