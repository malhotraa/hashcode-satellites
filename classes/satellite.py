from classes import position

DEGREE_TO_ARCSEC = 3600
MIN_LON_ARCSEC = -648000
MAX_LON_ARCSEC = 647999

class Satellite:
    def __init__(self, lat, lon, vel, max_delta_orientation_per_turn, max_orientation):
        self._lat = int(lat)
        self._lon = int(lon)
        self._vel = int(vel)
        self._max_delta_orientation_per_turn = int(max_delta_orientation_per_turn)
        self._max_orientation = int(max_orientation)
        self._orientation_lat = 0
        self._orientation_lon = 0
        self._t = 0

    def __str__(self):
        return f"Satellite (lat={self._lat}, lon={self._lon}, vel={self._vel}, orient_lat={self._orientation_lat}, orient_lon={self._orientation_lon})"

    def current_position(self):
        return position.Position(self._lat, self._lon, self._t)

    def next_position(self):
        new_lat = self._lat + self._vel
        new_lon = self._lon - 15
        new_vel = self._vel
        if new_lat > 90 * DEGREE_TO_ARCSEC: # Satellite flew over north pole
            new_lat = (180 * DEGREE_TO_ARCSEC) - new_lat
            new_lon = (-180 * DEGREE_TO_ARCSEC) + new_lon
            new_vel = -1 * new_vel
        elif new_lat < -90 * DEGREE_TO_ARCSEC: # Satellite flew over south pole
            new_lat = (-180 * DEGREE_TO_ARCSEC) - new_lat
            new_lon = (-180 * DEGREE_TO_ARCSEC) + new_lon
            new_vel = -1 * new_vel

        if new_lon < MIN_LON_ARCSEC:
            new_lon = 648000 + (new_lon - MIN_LON_ARCSEC)
        elif new_lon > MAX_LON_ARCSEC:
            new_lon = MIN_LON_ARCSEC + (new_lon - 648000)

        self._lat, self._lon, self._vel, self._t = new_lat, new_lon, new_vel, self._t + 1

        return position.Position(self._lat, self._lon, self._t)
