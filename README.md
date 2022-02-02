# Ruckus-WLAN-Configurator
Configuration script tool for configuration of Ruckus Wireless WLAN settings using the Virtual SmartZone REST API

<br>

# What is this?
Using Python and the requests,json modules, this set of scripts will configure WLAN settings on a Ruckus Virtual SmartZone controller to find all networks with the SSID 'JS-Guest' and set a randomly generated passphrase.

<br>

This random passphrase is generated using `WordGen.py` in [/src](/src).

<br>

# Requirements
 - Netmiko network automation
   - `python3 pip install netmiko`
 - JSON parser
   - `python3 pip install json`
 - Ruckus Virtual SmartZone version 6 or later
 - Administrative user in SmartZone with privileges to perform WLAN changes

<br>

# General Usage
The script requires the following 2 arguments:
 - `-u`, `--username`, str
   - Username to authenticate to the API with
   - Must have proper permissons in web administration
 - `-p`, `--password`, int
   - Password to authenticate to the API with

<br>

# Side notes
HTML generated using the following HTML generator:
 - [https://html-online.com/editor/](https://html-online.com/editor/)