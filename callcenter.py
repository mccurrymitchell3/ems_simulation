import globals
import queue
import station

class CallCenter:
    def __init__(self):
        self.cc_log = queue.PriorityQueue()

    def assign_call(self, stations): #this will eventually be a list of stations,
        # and calls will be assigned to FEL's based on location
        while not self.cc_log.empty():
            # call format: (call_time, type, location)
            call = self.cc_log.get()
            call_type = call[1]
            severity = globals.severities[call_type]
            adjusted_calltime = call[0] + severity
            stations[call[2]].stationQueue.put((adjusted_calltime, 'call', call[0]))