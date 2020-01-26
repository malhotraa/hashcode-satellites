class Position: # Represents a satellite location at time t
    def __init__(self, lat, lon, t):
        self._lat = lat
        self._lon = lon
        self._t = t

    def __str__(self):
        return f"Position (loc=({self._lat}, {self._lon}), time={self._t})"

    def __hash__(self):
        return hash((self._lat, self._lon, self._t))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self._lat == other._lat and self._lon == other._lon and self._t == other._t
