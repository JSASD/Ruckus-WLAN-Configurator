# Ruckus-WLAN-Configurator
Configuration script tool for configuration of Ruckus Wireless WLAN settings using the Virtual SmartZone REST API

<br>

# What is this?
Using Python and the requests,json modules, this set of scripts will configure WLAN settings on a Ruckus Virtual SmartZone controller to find all networks with the SSID 'JS-Guest' and set a randomly generated passphrase.

<br>

This random passphrase is generated using [/src/WordGen.py](/src/WordGen.py)].

<br>

# Requirements
 - Python requirements
   - ≥ Python 3.9
   - [requirements.txt](/requirements.txt)
     - ***Python3.9*** `python3 -m pip install -r requirements.txt`
     - ***Python3.10 or greater*** `py -m pip install -r requirements.txt`
 - Ruckus Virtual SmartZone version 6 or later
 - Administrative user in SmartZone with privileges to perform WLAN changes

<br>

# Email list

To send emails with [/src/SendEmail.py](/src/SendEmail.py), make sure to change [emailList.txt.example](/emailList.txt.example) to [emailList.txt](/emailList.txt) and add desired recipients accordingly.

<br>

# General Usage

Run `main.py` with the following arguments:
 - `-u`, `--username`, `str`
   - Username to authenticate to the API with
   - Must have proper permissons in web administration
 - `-p`, `--password`, `str`
   - Password to authenticate to the API with
 - `-c`, `--Controller`, `str`
   - DNS name of controller to log in to
 - `-o`, `--Port`, `str`
   - Controller port to connect with
 - `-e`, `--EmailAddress`, `str`
   - Email address to send email from
 - `-a`, `--EmailPassword`, `str`
   - Password for send from email
 - `-w`, `--WlanSearch`, `str`
   - String used to search for WLANS (contains)

<br>

# Side notes
HTML generated using the following HTML generator:
 - [https://html-online.com/editor/](https://html-online.com/editor/)