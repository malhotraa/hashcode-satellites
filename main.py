import os
from classes import image, satellite, collection, position
from typing import List

def readInput(filename: str) -> List:
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def parseLines(lines: List):
    T = int(lines[0])
    S = int(lines[1])
    satellites = []
    collections = []
    for i in range(S):
        satellites.append(satellite.Satellite(*lines[2 + i].split()))

    i = S+2
    num_collections = int(lines[i])
    curr_collection = 0
    collections = []
    i += 1
    while curr_collection < num_collections:
        points, num_images, num_times = list(map(int, lines[i].split()))
        i+=1
        col = collection.Collection(points)
        for img in range(num_images):
            lat, long = list(map(int, lines[i].split()))
            i += 1
            col.add_image(image.Image(lat, long))

        times = []
        for time in range(num_times):
            start, end = list(map(int, lines[i].split()))
            # times.append((start, end))
            col.add_time(start, end)
            i += 1

        col.add_image(image)
        collections.append(col)
        curr_collection+= 1
    return T, S, satellites, collections

# class Driver:
#     def __init__(self, tot_time, satellites, collections)
#         pass

#     def generate_all_satellite_paths(self):
#         pass

#     def
#     '''
#         1   1

#         2   2 or 3

#     '''

def setup():
    tot_time = 3600
    google_paris = image.Image(175958, 8387, [[0, 3599]])
    collection_1 = collection.Collection(100, [google_paris])

    eiffel = image.Image(175889, 8260, [[0, 900], [2700, 3599]])
    collection_2 = collection.Collection(100, [eiffel])

    google_paris = image.Image(175958, 8387, [[3300, 3599]])
    eiffel = image.Image(175889, 8260, [[0, 900], [3300, 3599]])
    collection_3 = collection.Collection(300, [google_paris, eiffel])


    '''
    0 - all posstible paths of a satellite and also all posible paths of all satt [malhot]

    1 - combine mutially exclusive collections [jsARDINHA]


    2 - remove impossible collections

    [ (1, 0, 10),
         (2, 1,  11)...(n, 0, 3600)]

              --
      .... [] --
              --


    1 - all possttible paths of Satellite()
    2 -


    '''



if __name__ == "__main__":
    lines = readInput('./input/given_sample.in')
    # lines = readInput('./input/constellation.in')
    T, S, satellites, collections = parseLines(lines)
    print("Calculating paths for {} satellites over {} timesteps.".format(S, T))

    positions = set()
    for s in range(S):
        positions.add(satellites[s].current_position())
        # print(f"Satellite {s} at time 0: {satellites[s].current_position()}")

        for t in range(1, T):
            position_t = satellites[s].next_position()
            positions.add(position_t)
            # print(f"Satellite {s} at time {t}: {position_t}")
        print(f"Done calculating positions for satellite {s}")

    print(f"Calculated {len(positions)} unique positions.")
    print(f"Sample position: {list(positions)[0]}")


    print("---------------")
    for collection in collections:
        print(collection.lowest_time, collection.higest_time)

