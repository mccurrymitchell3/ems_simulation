import globals
import queue
import station

class CallCenter:

    # Priority queue that holds the raw incident events based on time
    def __init__(self):
        self.cc_log = queue.PriorityQueue()

    # gives a weighted time and puts the calls in the relevant stations' stationqueue
    def assign_call(self, stations): # List of stations
        while not self.cc_log.empty():
            # call format: (call_time, type, location)
            call = self.cc_log.get()
            call_type = call[1]
            severity = globals.severities[call_type]
            adjusted_calltime = call[0] + severity
            stations[call[2]].stationQueue.put((adjusted_calltime, 'call', call[0]))