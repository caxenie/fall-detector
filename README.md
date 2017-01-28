
Hack Cambridge 2017

Real-time Event-based Monitoring System for Seniors and Elderly using Neural Networks

Team:
Cristian Axenie
Simeon Kostadinov
Mark Mathews

It has been estimated that 33% of people age 65 will fall. At around 80, that increases to 50%. In
case of a fall, seniors who receive help within an hour have a better rate of survival and, the faster
help arrives, the less likely an injury will lead to hospitalization or the need to move into a long-term
care facility. In such cases fast visual detection of abnormal motion patterns is crucial. 

In this project we propose the use of a novel embedded Dynamic Vision Sensor (eDVS) for the task of classifying falls. Opposite from
standard cameras which provide a time sequenced stream of frames, the eDVS provides only relative
changes in a scene, given by individual events at the pixel level. Using this different encoding scheme
the eDVS brings advantages over standard cameras. First, there is no redundancy in the data received
from the sensor, only changes are reported. Second, as only events are considered the eDVS data rate is
high. Third, the power consumption of the overall system is small, as just a low-end microcontroller is
used to fetch events from the sensor and can ultimately run for long time periods in a battery powered
setup. This project investigates how can we exploit the eDVS fast response time and low-redundancy
in making decisions about elderly motion. 

The computation backend will be realized with a neural network classificator to detect fall and filter outliers. The data will
be provided from 3 stimuli (blinking LEDs at different frequencies) and will represent the actual position of the person wearing them.
The changes in position of the stimuli will encode the possible positions corresponding to falls or normal cases. 

We will use Microsoft Azure ML Studio to implement a MLP binary classifier for the 6 (3 stimuli x 2 Cartesian coordinates - (x,y) in the field of view) dimensional input. We labelled the data with Fall (F) and No Fall (NF).


