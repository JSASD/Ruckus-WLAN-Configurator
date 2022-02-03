# guestPassCreation.py
# Generates a random 3-word phrase, and modifies specified WLANS SSIDs for each zone
# API Documentation can be found on the controller GUI, under "Administration" > "REST API"

# To be run on the following dates:
#   Oct 30
#       - End of MP1
#   Dec 30
#       - End of MP2
#   Feb 28
#       - End of MP3
#   June 15
#       - End of MP4
#   July 30
#       - Mid-End of Summer

# DEPENDENCIES NEEDED TO INSTALL FOR SCRIPT TO WORK
# python3 -m pip install requests
# python3 -m pip install json

# Import OS for directory usage
import os
# Import requests for API interfacing
import requests
# Import argument parser
import argparse
# Import local files
from src import Ruckus, ModifyGuestPassphrase, SendEmail, WordGen

# Set location of current directory for reliable file opening
__location__ = os.path.realpath(
    os.path.join(
        os.getcwd(),
        os.path.dirname(
            __file__)
        )
)

# Initialize parser
parser = argparse.ArgumentParser(description="Generates a random 3-word phrase, and modifies specified WLANS SSIDs for each zone")

# Help Prompts
userPrompt = "Set username to log in with"
passPrompt = "Set password to log in with"
controllerPrompt = "Set DNS name to log in to, best if use FQDN"

# Add arguments
parser.add_argument("-u", "--Username", help = userPrompt, required=True)
parser.add_argument("-p", "--Password", help = passPrompt, required=True)
parser.add_argument("-c", "--Controller", help = controllerPrompt, required=True)

# Read arguments from command line
args = parser.parse_args()

# Set given arguments to variables
username = args.Username
password = args.Password
controller = args.Controller


logon = Ruckus.login(username, password, controller)

serviceTicket = Ruckus.getServiceTicket(logon)

print(Ruckus.getZones(serviceTicket, controller))

# Generate random 2-word phrase
passphrase = WordGen.createKey(__location__)