import numpy as np
import time
import math
import csv
import nstdvs
import sys
import requests
import json
import message

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

fall_ctr = 0
notif_threshold = 15
time_moving = 500
spamwriter = csv.writer(open('sensor_results_data.csv', 'a') , delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter.writerow( ('xt', 'yt', 'xb', 'yb' , 'state') )
mode = sys.argv[1]
while True:
    if mode == 'train':
	# get the position of the tracked stimulus
	target_stim = np.array(tracker())
	result = calculateSin(target_stim[0], target_stim[1], target_stim[2], target_stim[3])
	spamwriter.writerow([target_stim[0], target_stim[1], target_stim[2], target_stim[3]] + [result])
	# processing delay
	time_moving = time_moving - 1
	if time_moving <= 0:
		sys.exit()
	time.sleep(0.2)
    else:
	# get the position of the tracked stimulus
	target_stim = np.array(tracker())
	payload = {'xt':target_stim[0], 'yt':target_stim[1], 'xb':target_stim[2], 'yb':target_stim[3]}
	import urllib2
        data =  {
        	"Inputs": {
	
                	"input1":
                	{
                    	"ColumnNames": ["xt", "yt", "xb", "yb", "state"],
                    	"Values": [ [ target_stim[0], target_stim[1], target_stim[2], target_stim[3], "value" ], ]
                	},        },
            	"GlobalParameters": {
		}
    	}

	body = str.encode(json.dumps(data))

	url = 'https://ussouthcentral.services.azureml.net/workspaces/851727c782774391b56a9623919d8981/services/db290b779d0447f690e806daddc8bf01/execute?api-version=2.0&details=true'
	api_key = 'vy2A7yQJ+oISq5/GK05tu8tDmHbXJDUy1EzC1hzd+OZs8BiOq1wWA9x+M/GtbDxN3lOcJOjqZUDIo+JE8s1TpQ==' # Replace this with the API key for the web service
	headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
	req = urllib2.Request(url, body, headers) 
	response = urllib2.urlopen(req)
	the_page = json.loads(response.read())
	status = the_page["Results"]["output1"]["value"]["Values"][0][5]
	if status == 'F':
	   fall_ctr = fall_ctr + 1
	if fall_ctr == notif_threshold:
	   # send notification
	   message.notify("+4407599463432", "cristian.axenie@gmail.com", "Cambridge")		
	   sys.exit()
	time.sleep(0.5)
