import queue

class Station:

    self.ambulancesAtStation = 0
    self.ambulancesEnRoute = 0
    self.avgWaitTime = 0

    self.stationQueue = queue.PriorityQueue()

    def insertRequest(self, request):
        self.stationQueue.insert(request)

    def dispatch(self, request):
        # Keep track of time. All requests take the same amount of time.
        request = self.stationQueue.get()
        self.ambulancesAtStation -= 1
        self.ambulancesEnRoute += 1

        # After ambulance returns
        self.ambulancesAtStation += 1
        self.ambulancesEnRoute -= 1