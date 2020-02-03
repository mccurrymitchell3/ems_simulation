import station
import globals
import callcenter
import generator

globals.init()

s1 = station.Station(3, 15) # Number of ambulances available at the station,
                            # average time en route for each ambulance from this station
s2 = station.Station(3, 15)

stations = [s1, s2]

cc = callcenter.CallCenter()
gen = generator.Generator()
duration = 100 # minutes to run

# Run for duration minutes
while globals.now < duration:

    # Generate events and pass in the call center
    gen.generateAndAdd(cc)

    # Assign the calls to a station
    cc.assign_call(stations)

    startTime = globals.now
    print("STATION 1")
    # While there are elements in the priority queue, process the next element
    while (not s1.stationQueue.empty() or not s1.waitingQueue.empty()) and globals.now < startTime + 15:
        s1.process_next_elem(startTime)
    
    # Reset start time for station two
    globals.now = startTime
    print("STATION 2")
    while (not s2.stationQueue.empty() or not s2.waitingQueue.empty()) and globals.now < startTime + 15:
        s2.process_next_elem(startTime)

    # Update the current time and start the next interval
    globals.now = startTime + 15

# Calculate the average waiting time for each call received
print("Station One Average Waiting Time: ", s1.totalWaitingTime / s1.callEventsProcessed)
print("Station Two Average Waiting Time: ", s2.totalWaitingTime / s2.callEventsProcessed)