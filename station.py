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
        #if not self.waitingQueue.empty():
        #    waitingEvent = self.waitingQueue.get()
        #eventToProcess = min(event, waitingEvent)
        if event[1] == 'arrival':
            self.process_arrival_event(event)
        elif event[1] == 'call':
            self.process_call_event(event)

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

            if not self.waitingQueue.empty():
                waitingEvent = self.waitingQueue.get()
                print("we", waitingEvent)
                print("e", event)
                if waitingEvent[0] < event[0]:
                    globals.now = max(globals.now, waitingEvent[2])
                    self.stationQueue.put((globals.now + self.transitTime, 'arrival'))
                    self.stationQueue.put(event)
                    self.totalWaitingTime += (globals.now - waitingEvent[2])
                    print("processed waiting event")
                else:
                    globals.now = max(globals.now, event[2])
                    self.stationQueue.put((globals.now + self.transitTime, 'arrival'))
                    self.waitingQueue.put(waitingEvent)
                    self.totalWaitingTime += (globals.now - event[2])
                    print("proccessed station event")
            else:
                globals.now = max(globals.now, event[2])
                self.stationQueue.put((globals.now + self.transitTime, 'arrival'))
                self.totalWaitingTime
                self.totalWaitingTime += (globals.now - event[2])
                print("proccessed station event")

            self.ambulancesAtStation -= 1
        else: 
            print("no ambulances at station")
            self.waitingQueue.put(event)
            print(self.waitingQueue.empty())

        print("now", globals.now)
        print("numAmb", self.ambulancesAtStation)
        print("total waiting time", self.totalWaitingTime)
        print()
