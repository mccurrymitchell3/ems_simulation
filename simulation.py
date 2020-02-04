import station
import globals
import callcenter
import generator

globals.init()
output = []

# we run the simulation for a varying number of ambulances per station, documenting
# the average wait time depending on number of ambulances available
for numAmbulances in range(1, 10):

    s1 = station.Station(numAmbulances, 15) # (Number of ambulances available at the station,
                                # average time en route for each ambulance from this station)
    s2 = station.Station(numAmbulances, 12)

    stations = [s1, s2]

    cc = callcenter.CallCenter()
    gen = generator.Generator()
    duration = 300 # minutes to run simulation

    # Run for duration minutes
    while globals.now < duration:
        print("now ", globals.now)

        # Generate events and pass in the call center
        gen.generateAndAdd(cc)

        # Assign the calls to a station
        cc.assign_call(stations)

        startTime = globals.now
        print("STATION 1")
        # While there are elements in the priority queue, process the next element
        while (not s1.stationQueue.empty() or not s1.waitingQueue.empty()) and globals.now < startTime + 15:
            s1.process_next_elem(startTime)

        # Reset start time for station two, so that it technically is running
        # at the same time as station one but without multithreading
        globals.now = startTime
        print("STATION 2")
        while (not s2.stationQueue.empty() or not s2.waitingQueue.empty()) and globals.now < startTime + 15:
            s2.process_next_elem(startTime)

        # Update the current time and start the next interval
        globals.now = startTime + 15

    # reset time to 0 to simulate next number of ambulances
    globals.now = 0

    # Calculate the average waiting time for each call received
    print("numAmbulances", numAmbulances)
    print("Station One Average Waiting Time: ", s1.totalWaitingTime / s1.callEventsProcessed)
    print("Station Two Average Waiting Time: ", s2.totalWaitingTime / s2.callEventsProcessed)

    # Add average waiting times for each call received to output list.
    # These stats will be written to the 'output.txt'.
    output.append("Number of Ambulances: {}\n".format(numAmbulances))
    output.append("Station One Average Waiting Time: {}\n".format(s1.totalWaitingTime / s1.callEventsProcessed))
    output.append("Station Two Average Waiting Time: {}\n\n".format(s2.totalWaitingTime / s2.callEventsProcessed))

# Write the statistics calculated for each number of ambulances to 'output.txt'.
file = open("output.txt", "w")
file.writelines(output)
file.close()

