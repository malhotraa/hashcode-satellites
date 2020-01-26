from classes import image, position

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


    def update_image_times(self):
        for t in self.possible_times:
            lb, ub = t
            for i in self.images:
                for t in range(lb, ub+1):
                    i.add_time(position.Position(i._lat, i._lon, t))
