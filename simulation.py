import station
import globals
import callcenter
import generator

globals.init()

s1 = station.Station(3, 15)
cc = callcenter.CallCenter()
gen = generator.Generator()

#gen.generateAndAdd(cc)

# events = [(10, 'call', 10), (10, 'call', 9), (5, 'call', 5), (9, 'call', 3)]
# calls = [(10, 'DUMMY', 12), (9, 'DIFFBR', 1), (5, 'DUMMY', 9), (3, 'INJURY', 9)]

#for event in events:
#    s1.stationQueue.put(event)

# for call in calls:
#     print("call", call)
#     cc.cc_log.put(call)

#cc.assign_call(s1)

while globals.now < 100:
    gen.generateAndAdd(cc)
    cc.assign_call(s1)
    startTime = globals.now
    while (not s1.stationQueue.empty() or not s1.waitingQueue.empty()) and globals.now < startTime + 15:
        s1.process_next_elem()
    globals.now = startTime + 15
avgWaitingTime = s1.totalWaitingTime / s1.callEventsProcessed
print("Average Waiting Time: ", avgWaitingTime)