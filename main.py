import os
from classes import image, collection, satellite




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
    setup()
