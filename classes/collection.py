from classes import image
class Collection:
    def __init__(self, tot_points):
        self.tot_points = tot_points
        self.possible_times = set()
        self.images = []
        self.lowest_time = float('INF')
        self.higest_time = 0

    def add_image(self, image):
        self.images.append(image)

    def add_time(self, lb, ub):
        self.lowest_time = min(lb, self.lowest_time)
        self.higest_time = max(ub, self.higest_time)
        self.possible_times.add((lb, ub))