# Import smtplib library to send SMTP mail
import smtplib
# Import HTML email libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def sendEmail(__location__, key, username, password):
    """
    Sends email to list of email addresses with guest key

    ### Returns
    None
    
    ### Depends on
     - Ruckus.getWlans()
     - Ruckus.setGuestPass()
     - WordGen.createKey()

    ### Parameters
     - __location__: str
       - Static location of main.py used for reliable file opening
     - key: str
       - Generated guest key from WordGen.createKey()
     - username: str
       - Email username to use for SMTP
     - password:
       - Email password to use for SMTP
    """
    # Open file 'emailList.txt'
    file = open(os.path.join(__location__, 'emailList.txt'), 'r')
    # Read file line by line
    emailList = file.readlines()
    # Initialize list of words
    emails = []
    # Add each word from emailList into 'emails' list
    for line in emailList:
        emails.append("{}".format(line.strip()))
    # Close the file
    file.close()

    # Iterate through each email in 'emailList' and send the email
    for email in emailList:
        # Set email contents
        message = MIMEMultipart('alternative')
        message['Subject'] = "Latest Guest Pass Generated"
        message['From'] = username
        message['To'] = email

        # Body of message in HTML
        htmlText = """
        <p>Hello!</p>
        <p>&nbsp;</p>
        <p>This email is to inform you that the latest guest pass for the Wi-Fi network&nbsp;<em><strong>JS-Guest</strong></em>&nbsp;has been generated.</p>
        <p><span style="text-decoration: underline;"><em>The guest pass is:</em></span></p>
        <h3><strong>""" + key + """</strong></h3>
        <h4>Instructions to get connected:</h4>
        <ol>
        <li>Open Wi-Fi settings on your device</li>
        <li>Select the network&nbsp;<strong>JS-Guest&nbsp;</strong>and connect to it</li>
        <li>Open any web browser and try to navigate to any website</li>
        <li>You will be prompted for a password, please enter the current guest pass&nbsp;<strong>""" + key + """</strong></li>
        </ol>
        <h4>Please keep the following in mind:</h4>
        <ul>
        <li>This guest pass is not to be given out except by office staff</li>
        <li>The guest Wi-Fi should only be used for district-related purposes, therefore care should be taken when dealing with sensitive information</li>
        <li>Guest Wi-Fi network traffic is not encrypted</li>
        <li>This pass will&nbsp;<em>expire in 45 days</em></li>
        </ul>
        """

        # Record HTML text
        htmlPartText = MIMEText(htmlText, 'html')

        # Attach parts into message container
        message.attach(htmlPartText)

        # Create variable for SMTP mail, send email with all configured settings
        mail = smtplib.SMTP('smtp.office365.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(username, password)
        mail.sendmail(username, email, message.as_string())
        mail.quit()