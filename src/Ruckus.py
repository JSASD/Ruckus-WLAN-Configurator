'''
Set of functions that interface with the Ruckus SmartZone API
-------
Supported Functions:
  - login()
    - Depends on:
      - none
    - Requires:
      - username
      - password
      - controller IP
  - getServiceTicket()
    - Depends on:
      - login()
    - Requires:
      - logon() returned value
  - getZones()
    - Depends on:
      - login()
      - getServiceTicket()
    - Requires:
      - getServiceTicket() returned value
      - controller IP
'''



# Import requests library for API calls
import requests
# Import json library to parse JSON from the controller
import json
# Import urllib3 library to suppress SSL warnings
import urllib3
# Suppress SSL warnings
urllib3.disable_warnings()


def login(username, password, controller):
    # Login to controller
    logon = requests.post(
        'https://' + controller + ':8443/wsg/api/public/v10_0/serviceTicket',
        verify=False,
        json = {
            "username": username,
            "password": password
        }
    )
    return(logon)

def getServiceTicket(logonText):
    logonText = json.loads(logonText.text)
    return(logonText['serviceTicket'])

def getZones(serviceTicket, controller):
    getZones = requests.get(
        'https://' + controller + ':8443/wsg/api/public/v10_0/rkszones?serviceTicket=' + serviceTicket,
        verify=False,
        params = {
            'serviceTicket': serviceTicket
        },
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
    )