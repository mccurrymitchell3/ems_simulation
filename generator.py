import callcenter
import globals
import random

class Generator:

    # generates incidents at 15 minute intervals
    def __init__(self):
        #self.callRate = 1 #this will eventually be a curve
        self.intervalMax = 15


    # generates a random number of events for the interval and generates random 
    # incident times, event times, and locations
    def generateAndAdd(self, cc):
        # get num events for each to be generated
        print("generating events")
        numEvents = random.randint(6, 18) # this range is based on the min and max number of calls averaged over a week from our data source.
        print("numEvents:", numEvents)
        # for each event, pick a time, pick a type, assign
        for event in range(numEvents):
            # assign a random time within the interval
            timeOfEvent = globals.now + random.randint(0, self.intervalMax)
            severity = random.choices([1, 2, 3, 4, 5, 6, 7, 8], globals.severity_weights_list)[0]
            eventType = random.choice(globals.severity_to_description[severity])
            location = random.randint(0, 9) #need to fix

            print((timeOfEvent, eventType, location))

            cc.cc_log.put((timeOfEvent, eventType, location))





