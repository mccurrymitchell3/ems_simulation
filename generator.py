import callcenter
import globals
import random

class Generator:

    def __init__(self):
        #self.callRate = 1 #this will eventually be a curve
        self.intervalMax = 15


    def generateAndAdd(self, cc):
        # get num events for each to be generated
        print("generating events")
        numEvents = random.randint(0, 5) #this is hardcoded. need to fix based on curve
        print("numEvents:", numEvents)
        # for each event, pick a time, pick a type, assign
        for event in range(numEvents):
            timeOfEvent = globals.now + random.randint(0, self.intervalMax)
            eventType = random.choice(list(globals.severities.keys()))
            location = 0 #need to fix

            print((timeOfEvent, eventType, location))

            cc.cc_log.put((timeOfEvent, eventType, location))





