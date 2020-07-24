
import requests
from datetime import datetime 
# credentials
from local_settings import headers

#dry_run = True
dry_run = False

timestamp = datetime.now()

filestamp = "/home/webuser/src/adsb/adsb-quickie/%s_%s_%s_%s_%s.json" % (timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second)
print("Writing to file: %s" % filestamp )
fh = open(filestamp, 'w')

url = "https://adsbexchange-com1.p.rapidapi.com/json/lat/45.5051/lon/-122.6750/dist/25/"



if not dry_run:
	response = requests.request("GET", url, headers=headers)

	fh.write(response.text)
	fh.close()
print("Done")
