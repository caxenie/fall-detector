import numpy as np
import time
import nstdvs
# encode the values in the [-1 1]
def tracker():
    dvs = np.array(dvs_brd.get_frequency_info(0))
    dvs[np.isnan(dvs)]=np.zeros(len(dvs[np.isnan(dvs)]))
    xpos = dvs[0] # stimulus on x axis will be used in azimuth mapping
    ypos = dvs[1] # stimulus on y axis will be used in elevation mapping
    probability = dvs[2] # likelihood that it is the stimulus as a way to filter
    return [xpos, ypos, probability]

# initialize vision subsystem
dvs_brd = nstdvs.DVSBoard()
dvs_brd.connect(nstdvs.Serial('/dev/ttyUSB0', baud=12000000))
time.sleep(1)
# enable the tracker
dvs_brd.track_frequencies([50])
# enable the data acquisition
dvs_brd.retina(True)
dvs_brd.show_image()

while True:
    # get the position of the tracked stimulus
    target_stim = np.array(tracker())
    # processing delay
    time.sleep(0.5)
