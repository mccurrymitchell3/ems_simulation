import queue
import time
from enum import Enum

class Station:

    self.ambulancesAtStation = 0
    self.ambulancesEnRoute = 0
    self.avgWaitTimeFromData = 15*60 # 15 minutes
    self.totalWaitingTime = 0.0
    self.avgWaitTimeFromSim = 0.0

    self.stationQueue = queue.PriorityQueue() # Queue of ambulances to depart

    # Insert a new call request to the priority queue
    def insertEvent(self, event):
        self.stationQueue.insert(event)

    def dispatch(self):
        # Keep track of time. All requests take the same amount of time.
        self.ambulancesAtStation -= 1 # Update number of ambulances at the station and those already dispatched
        self.ambulancesEnRoute += 1

        # After avgWaitTimeFromData call ambulance returned
        self.insertEvent((arrive, time.clock + self.avgWaitTimeFromData))

    # After ambulance returns
    def returned(self):
        self.ambulancesAtStation += 1
        self.ambulancesEnRoute -= 1

    request = self.stationQueue.get() # Take the next EMS request from the queue

    # If there are ambulances available at the station, dispatch them
    if self.ambulancesAtStation > 0:
        self.dispatch()

class Event(Enum):
    depart = 1 # Ambulance departs the station
    arrive = 2 # Ambulance completes its route and arrives back at the station
    newCall = 3 # New EMS Call