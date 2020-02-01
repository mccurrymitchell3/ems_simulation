import queue
import time

class Station:

    self.ambulancesAtStation = 0
    self.ambulancesEnRoute = 0
    self.avgWaitTimeFromData = 15*60 # 15 minutes
    self.totalWaitingTime = 0.0
    self.avgWaitTimeFromSim = 0.0

    self.stationQueue = queue.PriorityQueue() # Queue of ambulances to depart

    def insertRequest(self, request):
        self.stationQueue.insert(request)

    def dispatch(self):
        # Keep track of time. All requests take the same amount of time.
        request = self.stationQueue.get() # Take the next EMS request from the queue
        self.ambulancesAtStation -= 1 # Update number of ambulances at the station and those already dispatched
        self.ambulancesEnRoute += 1
        # After avgWaitingTime call ambulance returned
        time.sleep(self.avgWaitTime)
        self.returned()

    # After ambulance returns
    def returned(self):
        self.ambulancesAtStation += 1
        self.ambulancesEnRoute -= 1

    # If there are ambulances available at the station, dispatch them
    if self.ambulancesAtStation > 0:
        self.dispatch()