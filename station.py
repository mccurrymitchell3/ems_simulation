import queue
import globals

class Station:

    def __init__(self, numAmbulances, transitTime):
        self.ambulancesAtStation = numAmbulances
        self.transitTime = transitTime # 15 minutes
        self.totalWaitingTime = 0.0
        self.avgWaitTime = 0.0
        self.callEventsProcessed = 0
        self.stationQueue = queue.PriorityQueue() # Queue of ambulances to depart
        self.waitingQueue = queue.PriorityQueue() # Queue of calls waiting for an ambulance to return

    def process_next_elem(self):
        event = self.stationQueue.get()
        eventToProcess = event

        if eventToProcess[1] == 'arrival':
            self.process_arrival_event(eventToProcess)
        elif eventToProcess[1] == 'call':
            if not self.waitingQueue.empty():
                waitingEvent = self.waitingQueue.get()
                eventToProcess = min(event, waitingEvent)
                print("event", event)
                print("waitingEvent", waitingEvent)
                print("eventToProcess", eventToProcess)
                if eventToProcess == event:
                    self.waitingQueue.put(waitingEvent)
                else:
                    self.stationQueue.put(event)

            self.process_call_event(eventToProcess)
            
        

    def process_arrival_event(self, event):
        self.ambulancesAtStation += 1
        globals.now = event[0]
        print('proccessed arrival')
        print("now", globals.now)
        print("numAmb", self.ambulancesAtStation)
        print()

    def process_call_event(self, event):
        self.callEventsProcessed += 1

        if self.ambulancesAtStation > 0:
            globals.now = max(globals.now, event[2])
            self.stationQueue.put((globals.now + self.transitTime, 'arrival'))
            self.totalWaitingTime += (globals.now - event[2])
            print("processed waiting event")

            self.ambulancesAtStation -= 1
        else: 
            print("no ambulances at station")
            self.waitingQueue.put(event)
            print(self.waitingQueue.empty())

        print("now", globals.now)
        print("numAmb", self.ambulancesAtStation)
        print("total waiting time", self.totalWaitingTime)
        print()
