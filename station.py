import queue
import globals

class Station:

    # initialize station with number of abulances, using constant transit time
    # for how long the ambulance will be unavailable when going to incident
    def __init__(self, numAmbulances, transitTime):
        self.ambulancesAtStation = numAmbulances
        self.transitTime = transitTime # hardcoded for now, needs to be changed to fit the data

        # initialize values
        self.totalWaitingTime = 0.0
        self.avgWaitTime = 0.0
        self.maxWaitTime = 0.0
        self.callEventsProcessed = 0

        self.callQueue = queue.PriorityQueue()
        self.arrivalQueue = queue.PriorityQueue()

    # processes the next element either in the stationQueue or the waitingQueue,
    # depending on the time of the event and whether or not there is an ambulance
    # available to be dispatched
    def process_next_elem(self, startTime):

        eventToProcess = None

        # If there are ambulances available, we can process the next call in the CallQueue.
        if self.ambulancesAtStation > 0:
            if not self.callQueue.empty():
                event = self.callQueue.queue[0]
                if event[0] <= startTime + 15:
                    # Grab the next call event to process
                    eventToProcess = self.callQueue.get()
                else:
                    # Process the next arrival event
                    if not self.arrivalQueue.empty():
                        event = self.arrivalQueue.queue[0]
                        if event[0] <= startTime + 15:
                            eventToProcess = self.arrivalQueue.get()
                        else:
                            globals.now = event[0]
                    else:
                        globals.now = event[0]
            else:
                # Process the next arrival event
                if not self.arrivalQueue.empty():
                    event = self.arrivalQueue.queue[0]
                    if event[0] <= startTime + 15:
                        eventToProcess = self.arrivalQueue.get()
                    else:
                        globals.now = event[0]
                else:
                    globals.now = startTime + 15

        # If there are no ambulances available, we must process the next arrival event
        else:
            if not self.arrivalQueue.empty():
                event = self.arrivalQueue.queue[0]
                if event[0] <= startTime + 15:
                    eventToProcess = self.arrivalQueue.get()
                else:
                    globals.now = event[0]
            else:
                globals.now = startTime + 15
        
        # Process the event based on the type (call or arrival)
        if eventToProcess is not None:
            if eventToProcess[1] == 'arrival':
                self.process_arrival_event(eventToProcess)
            elif eventToProcess[1] == 'call':
                self.process_call_event(eventToProcess)


    # takes in an arrival event, and handles the arrival of the ambulance.
    # number of ambulances in the station increases,
    # the current time (now) is set to be the arrival time of the ambulance.
    def process_arrival_event(self, event):
        self.ambulancesAtStation += 1
        globals.now = event[0]
        print('proccessed arrival')
        print("now", globals.now)
        print("numAmb", self.ambulancesAtStation)
        print()


    # takes in a call event, dispatches an ambulance, and schedules that
    # ambulance's arrive event
    def process_call_event(self, event):
        # updated to reflect number of calls in order to determine accurate
        # average wait time

        # time must be updated to the later of the current time and the
        # time the call was placed, as an ambulance cannot be dispatched
        # prior to a call being received.
        globals.now = max(globals.now, event[2])

        # create an arrival event and add it to the queue
        self.arrivalQueue.put((globals.now + self.transitTime, 'arrival'))

        # update total waiting time for this station
        # waiting time is the amount of time between when the call was placed,
        # and when an ambulance was dispatched.
        waitTime = (globals.now - event[2])
        self.totalWaitingTime += waitTime

        if waitTime > self.maxWaitTime:
            self.maxWaitTime = waitTime

        # mark that an ambulance has left and there is now 1 less ambulance
        # available for dispatch
        self.ambulancesAtStation -= 1
        
        # increment indicdents processed counter
        self.callEventsProcessed += 1

        print("now", globals.now)
        print("numAmb", self.ambulancesAtStation)
        print("total waiting time", self.totalWaitingTime)
        print("max wait time", self.maxWaitTime)
        print()
