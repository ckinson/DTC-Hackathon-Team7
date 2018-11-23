import csv
import json
import sys

csvfile = open(sys.argv[1], 'r')
jsonfile = open(sys.argv[2], 'w')

fieldnames = ("COL_time", "device", "flow", "temp", "humidity")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    data = {
        "DeliveryStreamName": "bstack-RawMetricsDeliveryStream-6E8MKENXEFDM",
	"Record": {
           "Data": row
	}
    }
    json.dump(data, jsonfile)
    jsonfile.write('\n')
