class Image:
    def __init__(self, lat, lon):
        self._lat = lat
        self._lon = lon
        self._t = set()

    def add_time(self, pos):
        self._t.add(pos)

    def get_times(self):
        for t in self._t:
            return self._t

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self._lat == other._lat and self._lon == other._lon

    def __hash__(self):
        return hash((self._lat, self._lon))