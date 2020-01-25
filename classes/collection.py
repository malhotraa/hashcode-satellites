from classes import image
class Collection:
    def __init__(self, tot_points, images):
        self.tot_points = tot_points
        self.possible_times = set()
        self.images = []
        for i in images:
            self.images.append(i)
            self.possible_times.union(i.possible_times)
