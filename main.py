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

print("\n\n")

args = Args.getArgs()


serviceTicket = Ruckus.login(args['username'], args['password'], args['controller'])

zones = Ruckus.getZones(serviceTicket, args['controller'])
print(zones + "\n\n")

wlans = Ruckus.getWlans(serviceTicket, args['controller'], zones)
print(str(wlans) + "\n\n")

# Generate random 2-word phrase
psk = WordGen.createKey(__location__)
print(psk + "\n\n")


SendEmail.sendEmail(__location__, psk, args['emailUser'], args['emailPass'])