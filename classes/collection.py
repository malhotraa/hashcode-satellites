class Collection:
    def __init__(self, tot_points, images):
        self.tot_points = tot_points
        self.possible_times = set()
        self.images = []
        for i in images:
            self.images.append(images)
            self.possible_times.union(image.possible_times)
