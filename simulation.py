import station
import globals
import callcenter
import generator

globals.init()
output = []

def generateStations():
    s1 = station.Station(numAmbulances, 15) # (Number of ambulances available at the station,
    s2 = station.Station(numAmbulances, 12) # average time en route for each ambulance from this station)
    s3 = station.Station(numAmbulances, 17)
    s4 = station.Station(numAmbulances, 10)
    s5 = station.Station(numAmbulances, 13)
    s6 = station.Station(numAmbulances, 14)
    s7 = station.Station(numAmbulances, 9)
    s8 = station.Station(numAmbulances, 11)
    s9 = station.Station(numAmbulances, 13)
    s10 = station.Station(numAmbulances, 15)

    stations = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

    return stations


# we run the simulation for a varying number of ambulances per station, documenting
# the average wait time depending on number of ambulances available
for numAmbulances in range(1, 10):

    stations = generateStations()

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

        for i in range(0, len(stations)):
            startTime = globals.now
            stationNumber = i + 1
            print("STATION %s" % stationNumber)
            s = stations[i]
            # While there are elements in the priority queue, process the next element
            while (not s.stationQueue.empty() or not s.waitingQueue.empty()) and globals.now < startTime + 15:
                s.process_next_elem(startTime)

            # Reset start time for station two, so that it technically is running
            # at the same time as station one but without multithreading
            globals.now = startTime

        # Update the current time and start the next interval
        globals.now = startTime + 15

    # reset time to 0 to simulate next number of ambulances
    globals.now = 0

    # Calculate the average waiting time for each call received
    print("numAmbulances", numAmbulances)
    for i in range(0, len(stations)):
        s = stations[i]
        stationNumber = i + 1
        if s.callEventsProcessed == 0:
            print("Station %s Average Waiting Time: " % stationNumber, 0)
        else:
            print("Station %s Average Waiting Time: " % stationNumber, s.totalWaitingTime / s.callEventsProcessed)

    # Add average waiting times for each call received to output list.
    # These stats will be written to the 'output.txt'.
    output.append("Number of Ambulances: {}\n".format(numAmbulances))
    for i in range(0, len(stations)):
        s = stations[i]
        stationNumber = i + 1
        if s.callEventsProcessed == 0:
            output.append("Station %s Average Waiting Time: %s\n" % (stationNumber, 0))
        else:
            output.append("Station %s Average Waiting Time: %s\n" % (stationNumber, s.totalWaitingTime / s.callEventsProcessed))

# Write the statistics calculated for each number of ambulances to 'output.txt'.
file = open("output.txt", "w")
file.writelines(output)
file.close()

