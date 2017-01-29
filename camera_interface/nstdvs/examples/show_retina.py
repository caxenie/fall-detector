import numpy as np
import time
import math
import csv
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

def calculateSin(x1, y1, x2, y2):
    numerator = abs(y2 - y1)
    nominator = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    sin_alpha = numerator / nominator

    if sin_alpha > math.sqrt(2)/2:
        return 'NF'
    
    return 'F'

spamwriter = csv.writer(open('sensor_results_data.csv', 'a') , delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter.writerow( ('xt', 'yt', 'xb', 'yb' , 'state') )

while True:
    # get the position of the tracked stimulus
    target_stim = np.array(tracker())
    result = calculateSin(target_stim[0], target_stim[1], target_stim[2], target_stim[3])
    spamwriter.writerow([target_stim[0], target_stim[1], target_stim[2], target_stim[3]] + [result])
    # processing delay
    time.sleep(0.5)
