'''
Set of functions that interface with the Ruckus SmartZone API

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
    """
    Login to Ruckus Virtual SmartZone and return service ticket
    
    ### Returns
    API Service Ticket

    ### Parameters
    username: str
        Username to login to the controller with
    password: str
        Password to login to the controller with
    controller: str
        IP Address of the controller to login to
    """
    # Login to controller
    logon = requests.post(
        'https://' + controller + ':8443/wsg/api/public/v10_0/serviceTicket',
        verify=False,
        json = {
            "username": username,
            "password": password
        }
    )
    # Get service ticket value from login and return it
    logonText = json.loads(logon.text)
    serviceTicket = logonText['serviceTicket']
    return(serviceTicket)

def getZones(serviceTicket, controller):
    """
    Get list of zones from the controller, returns JSON text
    
    ### Returns
    List of Zones

    ### Depends on
    login()

    ### Parameters
     - serviceTicket: str
       - Service ticket retreived from login()
     - controller: str
       - IP Address of the controller to login to
    """
    getZones = requests.get(
        'https://' + controller + ':8443/wsg/api/public/v10_0/rkszones?serviceTicket=' + serviceTicket,
        verify=False,
        params = {
            'serviceTicket':serviceTicket
        },
        headers = {
            'Content-Type':'application/json;charset=UTF-8'
        }
    )
    return(getZones.text)

def getWlans(serviceTicket, controller, zones, searchText):
    """
    Get list of WLANS in each zone from the controller, returns JSON text

    ### Returns
    Dictionary of zoneID : wlanID : wlanName
    
    ### Depends on
    getZones()

    ### Parameters
     - serviceTicket: str
       - Service ticket retreived from login()
     - controller: str
       - IP Address of the controller to login to
     - zones: str
       - List of zones retreived from getZones()
     - searchText: str
       - String to search WLANs for, to return desired similar WLANs
    """
    zoneList = []
    zoneInfo = json.loads(zones)
    zoneNames = json.loads(zones)['list']
    for zone in range(zoneInfo['totalCount']):
        zoneList.append(zoneInfo['list'][zone]['id'])
    
    # Initialize dictionary to store zoneID:wlanName relationships
    wlanZones = {}
    # Initialize iterable number to create list indicies
    wlanZonesID = 1
    for zone in zoneList:
        # Retreives WLAN information from controller, stored in a variable
        gZWlans = requests.get(
            'https://' + controller + ':8443/wsg/api/public/v10_0/rkszones/' + zone + '/wlans?serviceTicket=' + serviceTicket,
            verify=False,
            params={
                'serviceTicket':serviceTicket
            },
            headers={
                'Content-Type':'application/json;charset=UTF-8'
            }
        )

        #Load lsit of WLANS to be read
        wlans = json.loads(gZWlans.text)['list']

        #Creates zoneID:wlanName dictionary
        for wlan in wlans:
            if searchText in wlan['name']:
                wlanZones[wlanZonesID] = {'zoneID': zone, 'wlanID': wlan['id'], 'wlanName': wlan['name']}
                wlanZonesID += 1
    
    return(wlanZones)

def setGuestPass(serviceTicket, controller, wlans, guestKey):
    """
    Changes encryption passphrases for all WLANS that contain 'searchText' from arguments

    ### Returns
    None
    
    ### Depends on
    getWlans()

    ### Parameters
     - serviceTicket: str
       - Service ticket retreived from login()
     - controller: str
       - IP Address of the controller to login to
     - wlans: str
       - List of WLANS retreived from getWlans()
     - guestKey: str
       - Key to set for WLANS
    """
    for wlan in wlans:
        requests.patch(
            'https://' + controller + ":8443/v10_0/rkszones/" + wlans['zoneID'] + "/wlans/" + wlans['id'] + "?serviceTicket=" + serviceTicket,
            verify=False,
            params = {
                'serviceTicket': serviceTicket
            },
            headers = {
                'Content-Type':'application/json;charset=UTF-8'
            },
            json = {
                "encryption": {
                    "method": "WPA2",
                    "algorithm": "AES",
                    "passphrase": guestKey,
                    "mfp": "disabled",
                    "support802.11rEnabled": False,
                }

            }
        )