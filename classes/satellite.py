class Satellite:
    def __init__(self, lat, long, vel, max_orient_per_turn, max_orientation):
        self.lat = lat
        self.long = long
        self.vel = vel
        self.orient = 0
        self.max_orient_per_turn = max_orient_per_turn
        self.max_orientation = max_orientation

    def get_new_dims_per_turn(self, new_orient):
        # get new lat and long (see table)
        # change orient
        # check if orientation is withing self.max_orient
        pass