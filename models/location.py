class Location:

    def __init__(self, name):
        self._name = name
        self._storage = []

    @property
    def name(self):
        return self._name

    @property
    def storage(self):
        return self._storage

    def __str__(self):
        return f'{self.name} | Stored items: {len(self.storage)} | Total weight: {0+[package.weight for package in self.storage]}'

