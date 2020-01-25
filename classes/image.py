class Images:
    def __init__(self, lat, long, times):
        self.lat = lat
        self.long = long
        self.possible_times = set()
        for time in times:
            lb, ub = time
            for i in range(lb, ub+1):
                self.possible_times.add(i)