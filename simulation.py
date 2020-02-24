import station
import globals
import callcenter
import incidents

globals.init()
output = []
transitTime = 60 # average round trip transit time for an ambulance dispatch

# Generate 10 stations representing the 10 stations in Brooklyn and their average route times
def generateStations(numAmbulances, transitTime):
    s1 = station.Station(numAmbulances, transitTime)
    s2 = station.Station(numAmbulances, transitTime)
    s3 = station.Station(numAmbulances, transitTime)
    s4 = station.Station(numAmbulances, transitTime)
    s5 = station.Station(numAmbulances, transitTime)
    s6 = station.Station(numAmbulances, transitTime)
    s7 = station.Station(numAmbulances, transitTime)
    s8 = station.Station(numAmbulances, transitTime)
    s9 = station.Station(numAmbulances, transitTime)
    s10 = station.Station(numAmbulances, transitTime)

    stations = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

    return stations


# we run the simulation for a varying number of ambulances per station, documenting
# the average wait time depending on number of ambulances available
for numAmbulances in range(7, 8):

    stations = generateStations(numAmbulances, transitTime)

    cc = callcenter.CallCenter()
    gen = incidents.Incidents()
    duration = 1425 # minutes to run simulation

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

            previousTotalWaitTime = s.totalWaitingTime
            previousCallsProcessed = s.callEventsProcessed
            # While there are elements in the priority queue, process the next element
            while (not s.callQueue.empty() or not s.arrivalQueue.empty()) and globals.now < startTime + 15:
                s.process_next_elem(startTime)

            # Reset start time for station two, so that it technically is running
            # at the same time as station one but without multithreading
            globals.now = startTime

            totalWaitTimeInterval = s.totalWaitingTime - previousTotalWaitTime
            callsProcessedInterval = s.callEventsProcessed - previousCallsProcessed
            if callsProcessedInterval == 0:
                print("STATION %s Average Wait Time During Interval %s-%s: %s" % (stationNumber, startTime, globals.now, totalWaitTimeInterval))
                output.append("STATION {} Average Wait Time During Interval {}-{}: {}\n".format(stationNumber, startTime, globals.now, totalWaitTimeInterval))
            else:
                print("STATION %s Average Wait Time During Interval %s-%s: %s" % (stationNumber, startTime, globals.now, totalWaitTimeInterval/callsProcessedInterval))
                output.append("STATION {} Average Wait Time During Interval {}-{}: {}\n".format(stationNumber, startTime, globals.now, totalWaitTimeInterval/callsProcessedInterval))
        # Update the current time and start the next interval
        globals.now = startTime + 15

    # reset time to 0 to simulate next number of ambulances
    globals.now = 0

    totalAvgWaitTime = 0
    totalAvgWaitTimeSevere = 0
    totalMaxWaitTime = 0
    totalMaxWaitTimeSevere = 0

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
            if s.maxWaitTime > totalMaxWaitTime:
                totalMaxWaitTime = s.maxWaitTime
        if s.severeCallEvents == 0:
            print("Station %s Average Waiting Time For Severe Cases: " % stationNumber, 0)
            print("Station %s Maximum Waiting Time For Severe Cases: " % stationNumber, 0)
        else:
            print("Station %s Average Waiting Time For Severe Cases: " % stationNumber, s.totalWaitingTimeSevere / s.severeCallEvents)
            print("Station %s Maximum Waiting Time For Severe Cases: " % stationNumber, s.maxWaitTimeSevere)
            totalAvgWaitTimeSevere += s.totalWaitingTimeSevere / s.severeCallEvents
            if s.maxWaitTimeSevere > totalMaxWaitTimeSevere:
                totalMaxWaitTimeSevere = s.maxWaitTimeSevere

    print("Average Wait Time Across All Stations: ", totalAvgWaitTime / len(stations))
    print("Average Wait Time Across All Stations For Severe Cases: ", totalAvgWaitTimeSevere / len(stations))
    print("Maximum Wait Time Across All Stations: ", totalMaxWaitTime)
    print("Maximum Wait Time Across All Stations For Severe Cases: ", totalMaxWaitTimeSevere)

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
    output.append("Maximum Wait Time Across All Stations: %s\n" % totalMaxWaitTime)
    output.append("Maximum Wait Time For Severe Cases Across All Stations: %s\n" % totalMaxWaitTimeSevere)
# Write the statistics calculated for each number of ambulances to 'output.txt'.
file = open("output.txt", "w")
file.writelines(output)
file.close()

