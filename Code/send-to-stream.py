import boto3
import csv
import json
import time



def read_from_csv(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        row_json_data = []
        for row in reader:
            row_json_data.append(json.dumps(row))
        return row_json_data


data = read_from_csv('../data/Biometrics-Data_Set-24Hrs.csv')

print(data)


TIME_INTERVAL = 0.1

client = boto3.client('kinesis',
                      region_name='eu-west-1')
#
# try:
#     delete = client.delete_stream(
#         StreamName='aws-kinesis-dxc-7'
#     )
# except:
#     pass
#
response = client.create_stream(
    StreamName='aws-kinesis-dxc-7',
    ShardCount=1
)

print(response)

list = client.list_streams()

print(list)

for row in data:
    print(row)
    response = client.put_record(
        StreamName='aws-kinesis-dxc-7',
        Data=row,
        PartitionKey='test-partition'
    )
    print(response)
    time.sleep(0.1)


delete = client.delete_stream(
    StreamName='aws-kinesis-dxc-7'
)

print(delete)