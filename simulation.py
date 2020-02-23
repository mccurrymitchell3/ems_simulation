import station
import globals
import callcenter
import generator

globals.init()
output = []

# Generate 10 stations representing the 10 stations in Brooklyn and their average route times
def generateStations(numAmbulances):
    s1 = station.Station(numAmbulances, 15)
    s2 = station.Station(numAmbulances, 12)
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

    stations = generateStations(numAmbulances)

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
            while (not s.callQueue.empty() or not s.arrivalQueue.empty()) and globals.now < startTime + 15:
                s.process_next_elem(startTime)

            # Reset start time for station two, so that it technically is running
            # at the same time as station one but without multithreading
            globals.now = startTime

        # Update the current time and start the next interval
        globals.now = startTime + 15

    # reset time to 0 to simulate next number of ambulances
    globals.now = 0

    totalAvgWaitTime = 0
    totalAvgWaitTimeSevere = 0

    # Calculate the average waiting time for each call received
    print("numAmbulances", numAmbulances)
    for i in range(0, len(stations)):
        s = stations[i]
        stationNumber = i + 1
        if s.callEventsProcessed == 0:
            print("Station %s Average Waiting Time: " % stationNumber, 0)
            print("Station %s Maximum Waiting Time: " % stationNumber, 0)
        else:
            print("Station %s Average Waiting Time: " % stationNumber, s.totalWaitingTime / s.callEventsProcessed)
            print("Station %s Maximum Waiting Time: " % stationNumber, s.maxWaitTime)
            totalAvgWaitTime += s.totalWaitingTime / s.callEventsProcessed
        if s.severeCallEvents == 0:
            print("Station %s Average Waiting Time For Severe Cases: " % stationNumber, 0)
            print("Station %s Maximum Waiting Time For Severe Cases: " % stationNumber, 0)
        else:
            print("Station %s Average Waiting Time For Severe Cases: " % stationNumber, s.totalWaitingTimeSevere / s.severeCallEvents)
            print("Station %s Maximum Waiting Time For Severe Cases: " % stationNumber, s.maxWaitTimeSevere)
            totalAvgWaitTimeSevere += s.totalWaitingTimeSevere / s.severeCallEvents

    print("Average Wait Time Across All Stations: ", totalAvgWaitTime / len(stations))
    print("Average Wait Time Across All Stations: ", totalAvgWaitTimeSevere / len(stations))

    # Add average waiting times for each call received to output list.
    # These stats will be written to the 'output.txt'.
    output.append("Number of Ambulances: {}\n".format(numAmbulances))
    for i in range(0, len(stations)):
        s = stations[i]
        stationNumber = i + 1
        if s.callEventsProcessed == 0:
            output.append("Station %s Average Waiting Time: %s\n" % (stationNumber, 0))
            output.append("Station %s Maximum Waiting Time: %s\n" % (stationNumber, 0))
        else:
            output.append("Station %s Average Waiting Time: %s\n" % (stationNumber, s.totalWaitingTime / s.callEventsProcessed))
            output.append("Station %s Maximum Waiting Time: %s\n" % (stationNumber, s.maxWaitTime))
        if s.severeCallEvents == 0:
            output.append("Station %s Average Waiting Time For Severe Cases: %s\n" % (stationNumber, 0))
            output.append("Station %s Maximum Waiting Time For Severe Cases: %s\n" % (stationNumber, 0))
        else:
            output.append("Station %s Average Waiting Time For Severe Cases: %s\n" % (stationNumber, s.totalWaitingTimeSevere / s.severeCallEvents))
            output.append("Station %s Maximum Waiting Time For Severe Cases: %s\n" % (stationNumber, s.maxWaitTimeSevere))
    output.append("Average Wait Time Across All Stations: %s\n" % (totalAvgWaitTime / len(stations)))
    output.append("Average Wait Time For Severe Cases Across All Stations: %s\n" % (totalAvgWaitTimeSevere / len(stations)))
# Write the statistics calculated for each number of ambulances to 'output.txt'.
file = open("output.txt", "w")
file.writelines(output)
file.close()

