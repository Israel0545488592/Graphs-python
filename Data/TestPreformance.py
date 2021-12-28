import time
from IMP.GraphAlgo import GraphAlgo

''' Testing the algorithms performance and comparing to previous work'''

Path1 = "C:/Users/Israel/computer sience/OOP/Assignments/Ex3/Data/1000NODES.json"
Path2 = "C:/Users/Israel/computer sience/OOP/Assignments/Ex3/Data/10000NODES.json"
Path3 = "C:/Users/Israel/computer sience/OOP/Assignments/Ex3/Data/100000NODES.json"

Our_Algorithm = GraphAlgo()

print('1000NODES\n')
start = time.perf_counter()
Our_Algorithm.load_from_json(Path1)
end = time.perf_counter()
print('loading: ' + str(end - start) + 'seconds')
start = time.perf_counter()
Our_Algorithm.shortest_path(3, 777)
end = time.perf_counter()
print('shortestPath: ' + str(end - start) + 'seconds')
start = time.perf_counter()
Our_Algorithm.TSP([1,5,100,200])
end = time.perf_counter()
print('TSP: ' + str(end - start) + 'seconds')

print('10000NODES\n')
start = time.perf_counter()
Our_Algorithm.load_from_json(Path2)
end = time.perf_counter()
print('loading: ' + str(end - start) + 'seconds')
start = time.perf_counter()
Our_Algorithm.shortest_path(3, 777)
end = time.perf_counter()
print('shortestPath: ' + str(end - start) + 'seconds')
start = time.perf_counter()
Our_Algorithm.TSP([1,5,100,200])
end = time.perf_counter()
print('TSP: ' + str(end - start) + 'seconds')

print('100000NODES\n')
start = time.perf_counter()
Our_Algorithm.load_from_json(Path3)
end = time.perf_counter()
print('loading: ' + str(end - start) + 'seconds')

