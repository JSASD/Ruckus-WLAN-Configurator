import argparse
import logging

def getArgs():
    # Initialize parser
    parser = argparse.ArgumentParser(description="Generates a random 2-word phrase, and modifies specified WLANS SSIDs for each zone")

    # Help Prompts
    userPrompt = "Set controller username to log in with"
    passPrompt = "Set controller password to log in with"
    controllerPrompt = "Set DNS name to log in to, best if use FQDN"
    portPrompt = "Set controller port to connect with"
    emailUserPrompt = "Set email address to send an email from"
    emailPassPrompt = "Set password for emailUserPrompt"
    wlanSearchPrompt = "String used to find WLANS (contains)"

    # Add arguments
    parser.add_argument("-u", "--Username", help = userPrompt, required=True)
    parser.add_argument("-p", "--Password", help = passPrompt, required=True)
    parser.add_argument("-c", "--Controller", help = controllerPrompt, required=True)
    parser.add_argument("-o", "--Port", help = portPrompt, required=False)
    parser.add_argument("-e", "--EmailAddress", help = emailUserPrompt, required=True)
    parser.add_argument("-a", "--EmailPassword", help = emailPassPrompt, required=True)
    parser.add_argument("-w", "--WlanSearch", help = wlanSearchPrompt, required=True)

    # Read arguments from command line
    args = parser.parse_args()

    # Use default controller port if not specified
    if args.Port is not None:
        port = args.Port
    else:
        port = "8443"

    # Create dictionary of arguments
    argValues = {
        'username': args.Username,
        'password': args.Password,
        'controller': args.Controller,
        'port': port,
        'emailUser': args.EmailAddress,
        'emailPass': args.EmailPassword,
        'wlanSearch': args.WlanSearch
    }

    logging.debug(argValues)
    return argValues