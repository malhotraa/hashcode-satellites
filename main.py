import os






if __name__ == "__main__":
    f = open(os.path.join("./input", "given_sample.in"), "r")
    line = f.readline()
    while line:
        print(line)
        line = f.readline()