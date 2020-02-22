import callcenter
import globals
import random
import datetime

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
        # numEvents = random.randint(6, 18) # this range is based on the min and max number of calls averaged over a week from our data source.

        hour = globals.now // 60
        mins = globals.now % 60
        if globals.day_type == 'weekend':
            freq_range = globals.callfreq_weekdays_range[datetime.time(hour, mins)]
        else:
            freq_range = globals.callfreq_weekends_range[datetime.time(hour, mins)]

        numEvents = random.randint(freq_range[0], freq_range[1])

        print("numEvents:", numEvents)
        # for each event, pick a time, pick a type, assign
        for event in range(numEvents):
            # assign a random time within the interval
            timeOfEvent = globals.now + random.randint(0, self.intervalMax)
            severity = random.choices([1, 2, 3, 4, 5, 6, 7, 8], globals.severity_weights_list)[0]
            eventType = random.choice(globals.severity_to_description[severity])
            # location = random.randint(0, 9) #need to fix
            location = random.choices(list(globals.zipcode_frequency.keys()), list(globals.zipcode_frequency.values()))[0]
            print('location', location)
            print((timeOfEvent, eventType, location))

            cc.cc_log.put((timeOfEvent, eventType, location))





