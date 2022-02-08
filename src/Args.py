import argparse

def getArgs():
    # Initialize parser
    parser = argparse.ArgumentParser(description="Generates a random 2-word phrase, and modifies specified WLANS SSIDs for each zone")

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

    # Create dictionary of arguments
    argValues = {
        'username': args.Username,
        'password': args.Password,
        'controller': args.Controller
    }

    return argValues