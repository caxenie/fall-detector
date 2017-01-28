import numpy as np
import time
import nstdvs
# encode the values in the [-1 1]
def tracker():
    dvs_top = np.array(dvs_brd.get_frequency_info(0))
    dvs_bot = np.array(dvs_brd.get_frequency_info(1))
    dvs_top[np.isnan(dvs_top)]=np.zeros(len(dvs_top[np.isnan(dvs_top)]))
    dvs_bot[np.isnan(dvs_bot)]=np.zeros(len(dvs_bot[np.isnan(dvs_bot)]))
    xpos_top = dvs_top[0]
    ypos_top = dvs_top[1]
    xpos_bot = dvs_bot[0]
    ypos_bot = dvs_bot[1]
    return [xpos_top, ypos_top, xpos_bot, ypos_bot]

# initialize vision subsystem
dvs_brd = nstdvs.DVSBoard()
dvs_brd.connect(nstdvs.Serial('/dev/ttyUSB0', baud=12000000))
time.sleep(1)
# enable the tracker and track the 2 markers for the trunk of the person
dvs_brd.track_frequencies([200, 1000])
# enable the data acquisition
dvs_brd.retina(True)
dvs_brd.show_image()

while True:
    # get the position of the tracked stimulus
    target_stim = np.array(tracker())
    print target_stim
    # processing delay
    time.sleep(0.2)
