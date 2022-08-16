#!/usr/bin/env python3

import boto3
import requests
import getpass
import configparser
import base64
import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup
from os.path import expanduser
from urllib.parse import urlparse
import schedule
import time

renewTokenEvery = 200

def renewToken(renewTokenEvery):
    profileName = 'default'
    region = 'eu-west-1'
    roleArn = 'arn:aws:iam::<account_id>:role/<role_name>'
    principalArn = 'arn:aws:iam::<account_id>:saml-provider/<provider_name>'
    idpentryurl = '<identity_url>'

    # Programmatically get the SAML assertion
    session = requests.Session()
    formresponse = session.get(idpentryurl, verify=True)

    # Get form's input text
    payload = {}
    formsoup = BeautifulSoup(formresponse.text, 'html.parser')
    for inputtag in formsoup.find_all(re.compile('(INPUT|input)')):
        name = inputtag.get('name','').lower()
        value = inputtag.get('value','')
        payload[name] = value
        if "username" in name or "email" in name:
            payload[name] = username+'@domain.net'
        elif "password" in name:
            payload[name] = password
        elif "authmethod" in name:
            payload[name] = 'FormsAuthentication'

    # Get form's action
    action = formsoup.find('form', {'id': 'loginForm'}).get('action')
    parsedurl = urlparse(idpentryurl)
    idpFinalUrl = parsedurl.scheme + "://" + parsedurl.netloc + action

    # Request POST method with form and payload
    response = session.post(idpFinalUrl, data=payload, verify=True)

    # Decode the response and extract the SAML assertion
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        assertion = soup.find('input', {'name': 'SAMLResponse'}).get('value')
    except Exception as e:
        print('SAMLResponse field doesn\'t exists.')
        exit(1)

    # Parse the returned assertion and extract the authorized roles
    awsroles = []
    root = ET.fromstring(base64.b64decode(assertion))
    for saml2attribute in root.iter('{urn:oasis:names:tc:SAML:2.0:assertion}Attribute'):
        if (saml2attribute.get('Name') == 'https://aws.amazon.com/SAML/Attributes/Role'):
            for saml2attributevalue in saml2attribute.iter('{urn:oasis:names:tc:SAML:2.0:assertion}AttributeValue'):
                awsroles.append(saml2attributevalue.text)

    for awsrole in awsroles:
        chunks = awsrole.split(',')
        if 'saml-provider' in chunks[0]:
            newawsrole = chunks[1] + ',' + chunks[0]
            index = awsroles.index(awsrole)
            awsroles.insert(index, newawsrole)
            awsroles.remove(awsrole)

    # Print information for the user
    print("")
    print("Region:", region)
    print("Role ARN:", roleArn)
    print("Principal ARN:", principalArn)
    print("Profile name:", profileName)
    print("Available AWS roles:", awsroles)

    # Token validation time
    tokenTTL = 65 * renewTokenEvery

    # Use the assertion to get an AWS STS token using Assume Role with SAML
    conn = boto3.client('sts', region)
    token = conn.assume_role_with_saml(RoleArn=roleArn,PrincipalArn=principalArn,SAMLAssertion=assertion,DurationSeconds=tokenTTL)

    awsconfigfile = expanduser("~") + '/.aws/credentials'

    # Read in the existing config file
    config = configparser.RawConfigParser()
    config.read(awsconfigfile)

    if not config.has_section(profileName):
        config.add_section(profileName)

    config.set(profileName, 'output', 'json')
    config.set(profileName, 'region', region)
    config.set(profileName, 'aws_access_key_id', token['Credentials']['AccessKeyId'])
    config.set(profileName, 'aws_secret_access_key', token['Credentials']['SecretAccessKey'])
    config.set(profileName, 'aws_session_token', token['Credentials']['SessionToken'])

    # Write the updated config file
    with open(awsconfigfile, 'w+') as configfile:
        config.write(configfile)

    print("Token renewed")

# Main
# -----------------------------------------------------------------------------

username = input("Username:")
password = getpass.getpass()

renewToken(renewTokenEvery)
schedule.every(renewTokenEvery).minutes.do(renewToken, renewTokenEvery)
while True:
    schedule.run_pending()
    time.sleep(1)
