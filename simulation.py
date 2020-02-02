import station
import globals

globals.init()

s1 = station.Station(3, 15)

events = [(10, 'call', 10), (10, 'call', 9), (5, 'call', 5), (9, 'call', 3)]

for event in events:
    s1.stationQueue.put(event)

while not s1.stationQueue.empty() or not s1.waitingQueue.empty():
    s1.process_next_elem()
