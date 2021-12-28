import time
from IMP.GraphAlgo import GraphAlgo

''' Testing the algorithms performance and comparing to previous work'''
head = "C:/Users/S/PycharmProjects/OOP_Ex3/"
Path1 = head + "Data/1000NODES.json"
Path2 = head + "Data/10000NODES.json"
Path3 = head + "Data/100000NODES.json"

Our_Algorithm = GraphAlgo()


def load_time(path):
    start = time.perf_counter()
    Our_Algorithm.load_from_json(path)
    end = time.perf_counter()
    print('loading: ' + str(end - start) + 'seconds')


def shortest_path_time():
    start = time.perf_counter()
    Our_Algorithm.shortest_path(3, 777)
    end = time.perf_counter()
    print('shortestPath: ' + str(end - start) + 'seconds')


def TSP_time():
    start = time.perf_counter()
    Our_Algorithm.TSP([1, 5, 100, 200])
    end = time.perf_counter()
    print('TSP: ' + str(end - start) + 'seconds')


def center_time():
    start = time.perf_counter()
    Our_Algorithm.centerPoint()
    end = time.perf_counter()
    print('center: ' + str(end - start) + 'seconds')


if __name__ == '__main__':
    timed_load = False
    print('1000NODES\n')
    if timed_load:
        load_time(Path1)
    else:
        Our_Algorithm.load_from_json(Path1)
    shortest_path_time()
    TSP_time()
    center_time()

    print('10000NODES\n')
    if timed_load:
        load_time(Path2)
    else:
        Our_Algorithm.load_from_json(Path2)
    shortest_path_time()
    TSP_time()
    center_time()

    print('100000NODES\n')
    if timed_load:
        load_time(Path3)
    else:
        Our_Algorithm.load_from_json(Path3)
    shortest_path_time()
    TSP_time()
    center_time()
