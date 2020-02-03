import queue
import globals

class Station:

    def __init__(self, numAmbulances, transitTime):
        self.ambulancesAtStation = numAmbulances
        self.transitTime = transitTime # 15 minutes, hardcoded for now until more stations
        #   are added and different locations are supported

        # initialize values
        self.totalWaitingTime = 0.0
        self.avgWaitTime = 0.0
        self.callEventsProcessed = 0

        self.stationQueue = queue.PriorityQueue() # Queue of ambulances to depart
        self.waitingQueue = queue.PriorityQueue() # Queue of calls waiting for an ambulance to return

    # processes the next element either in the stationQueue or the waitingQueue,
    # depending on the time of the event and whether or not there is an ambulance
    # available to be dispatched
    def process_next_elem(self, startTime):
        # if there are ambulances available, we can process either a call or an arrival.
        # In this case, we just grab whichever event happens sooner in the queue
        if self.ambulancesAtStation > 0:
            eventToProcess = None
            # if there are elements in both the stationQueue and the waitingQueue, we
            # need to pick the sooner one, and re-add the event we did not use back to
            # its original queue
            if not self.stationQueue.empty() and not self.waitingQueue.empty():
                event = self.stationQueue.queue[0]
                waitEvent = self.waitingQueue.queue[0]
                eventToProcess = min(event, waitEvent)

                if eventToProcess[0] <= startTime + 15:
                    if eventToProcess == event:
                        eventToProcess = self.stationQueue.get()
                    else:
                        eventToProcess = self.waitingQueue.get()
                else:
                    globals.now = eventToProcess[2]
                    eventToProcess = None

            # if there are only elements in the stationQueue, we use the next
            # element in the stationQueue
            elif not self.stationQueue.empty():
                if self.stationQueue.queue[0][0] <= startTime + 15:
                    eventToProcess = self.stationQueue.get()
                else:
                    eventToProcess = None
                    globals.now = self.stationQueue.queue[0][0]
            # if there are only elements in the waitingQueue, we use the next
            # element in the waitingQueue
            elif not self.waitingQueue.empty():
                if self.waitingQueue.queue[0][0] <= startTime + 15:
                    eventToProcess = self.waitingQueue.get()
                else:
                    eventToProcess = None
                    globals.now = self.waitingQueue.queue[0][0]

        # if there are no more ambulances, we cannot process any calls of the
        # waiting queue. We must pull from the stationQueue, and if that
        # event happens to be a call, it will later have to get added to the
        # waiting queue, and this process will continue until an arrival event
        # is processed and ambulances are available to handle the waiting queue.
        else:
            eventToProcess = self.stationQueue.get()

        # send the event object to the correct method based on event type or end the simulation
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
        self.callEventsProcessed += 1

        # if there are ambulances at the station, an ambulance may be dispatched
        if self.ambulancesAtStation > 0:

            # time must be updated to the later of the current time and the
            # time the call was placed, as an ambulance cannot be dispatched
            # prior to a call being received.
            globals.now = max(globals.now, event[2])

            # create an arrival event and add it to the queue
            self.stationQueue.put((globals.now + self.transitTime, 'arrival'))

            # update total waiting time for this station
            # waiting time is the amount of time between when the call was placed,
            # and when an ambulance was dispatched.
            self.totalWaitingTime += (globals.now - event[2])

            # mark that an ambulance has left and there is now 1 less ambulance
            # available for dispatch
            self.ambulancesAtStation -= 1
        else:
            # if there are no ambulances available, move the call to the waiting
            # queue to be processed once an ambulance is available
            print("no ambulances at station")
            self.waitingQueue.put(event)
            #print(self.waitingQueue.empty())

        print("now", globals.now)
        print("numAmb", self.ambulancesAtStation)
        print("total waiting time", self.totalWaitingTime)
        print()
