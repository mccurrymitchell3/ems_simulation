import station
import globals
import callcenter
import generator

globals.init()

s1 = station.Station(3, 15) # Number of ambulances available at the station,
                            # average time en route for each ambulance from this station
cc = callcenter.CallCenter()
gen = generator.Generator()
duration = 100 # minutes to run

# Run for duration minutes
while globals.now < duration:

    # Generate events and pass in the call center
    gen.generateAndAdd(cc)

    # Assign the calls to a station
    cc.assign_call(s1)

    startTime = globals.now

    # While there are elements in the priority queue, process the next element
    while (not s1.stationQueue.empty() or not s1.waitingQueue.empty()) and globals.now < startTime + 15:
        s1.process_next_elem()

    # Update the current time and start the next interval
    globals.now = startTime + 15

# Calculate the average waiting time for each call received
avgWaitingTime = s1.totalWaitingTime / s1.callEventsProcessed
print("Average Waiting Time: ", avgWaitingTime)