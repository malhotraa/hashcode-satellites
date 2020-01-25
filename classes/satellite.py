class Satellite:
    def __init__(self, lat, lon, vel, max_delta_orientation_per_turn, max_orientation):
        self._lat = lat
        self._lon = lon
        self._vel = vel
        self._max_delta_orientation_per_turn = max_delta_orientation_per_turn
        self._max_orientation = max_orientation
        self._orientation_lat = 0
        self._orientation_lon = 0

    def __str__(self):
        return f"Satellite (lat={self._lat}, lon={self._lon}, vel={self._vel}, orient_lat={self._orientation_lat}, orient_lon={self._orientation_lon})"
