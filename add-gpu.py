#!/usr/bin/python3
##################################################################################################################
#
#   Name: add-gpu
#   File: add-gpu.py
#   Author: James Anderton & Jason George
#   Date: 8/2/2018
#   Purpose: To add a GPU unit to a Google Compute Engine Instance
#
##################################################################################################################
import os
import time
import argparse
from pprint import pprint
from googleapiclient import discovery


##################################################################################################################
#
##################################################################################################################
def main(project_id, zone, instance_name, key_file, gpu_type, gpu_count):
    
    ###Set Environment Var to point library to our key file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file

    #format GPU type into url with zone
    acceleratorType = "zones/%s/acceleratorTypes/%s" % (zone, gpu_type)

    ### Setup JSON Request Body
    body = {
        "guestAccelerators": [
          {
            "acceleratorType": acceleratorType,
            "acceleratorCount": str(gpu_count),
          }
        ]
      }

    ####Call setMachineResources API Function and save response for processing
    service = discovery.build('compute', 'v1')
    service_request = service.instances().setMachineResources(project=project_id, zone=zone, instance=instance_name, body=body)

    try:
        response = service_request.execute()
    except Exception as e:
        print("Error: ", e)
        raise

    pprint(response)

    name = response['name']

    service_request = service.zoneOperations().get(project=project_id, zone=zone, operation=name)

    #### Process response, find operation "name" and call zoneOperations.list to see when its done
    while True:
        print('Processing..')
        response = service_request.execute()
        time.sleep(1)
        if 'DONE' in response['status']:
            break

    print("Operation finished on GCE Instance: {}".format(response["targetLink"].split("/")[-1]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--project_id', help='Your Google Cloud project ID.')
    parser.add_argument('--zone', default='us-central1-f', help='Compute Engine zone to deploy to.')
    parser.add_argument('--instance_name', default='demo-instance', help='New instance name.')
    parser.add_argument('--key_file', default='service_account.json', help='JSON file with Service Account Key data.')
    parser.add_argument('--gpu_type', default='nvidia-tesla-k80', help='GPU Type.')
    parser.add_argument('--gpu_count', default='1', help='Number of GPUs to add.')

    args = parser.parse_args()

    main(args.project_id, args.zone, args.instance_name, args.key_file, args.gpu_type, args.gpu_count)
