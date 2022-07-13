# main.py
# Generates a random 2-word phrase, and modifies specified WLANS SSIDs for each zone

# Import OS for directory usage
import os
# Import argument parser
import argparse
# Import local files
from src import Ruckus, SendEmail, WordGen, Args

# Set location of current directory for reliable file opening
__location__ = os.path.realpath(
    os.path.join(
        os.getcwd(),
        os.path.dirname(
            __file__)
        )
)

print('\n')

# Get args from console
args = Args.getArgs()

# Log into controller
serviceTicket = Ruckus.login(args['username'], args['password'], args['controller'], args['port'])

# Get list of Zones
zones = Ruckus.getZones(serviceTicket, args['controller'], args['port'])

# Get list of WLANS
wlans = Ruckus.getWlans(serviceTicket, args['controller'], args['port'], zones, args['wlanSearch'])

# Generate random 2-word phrase
psk = WordGen.createKey(__location__)

# Change PSK on guest WLANs
Ruckus.setGuestPass(serviceTicket, args['controller'], args['port'], wlans, psk)

# Send email to addresses in emailList.txt
SendEmail.sendEmail(__location__, psk, args['emailUser'], args['emailPass'])

# Log out of controller
Ruckus.logout(serviceTicket, args['controller'], args['port'])

print('\n')