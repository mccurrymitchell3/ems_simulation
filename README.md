# ems_simulation

## Background

This repository is meant to simulate EMS calls in Brooklyn, NY by randomly generating common emergency calls in various locations. The calls are collected by the call center and assigned a level of severity before being sent to a station. Once at the station, the requests are added to a priority queue based on the time the call is received and the severity of the call. Our simulation tracks the average wait time a caller is waiting before an ambulance is dispatched to their location. We manipulate this outcome by varying the number of ambulances available at each station.

## Running the code

To run our simulation, clone/download our repository and run ```py simulation.py```.

The number of ambulances available at a station can be changed in the ```simulation.py``` file.