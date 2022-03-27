import hubspot
import os
import json
from hubspot.crm.contacts import SimplePublicObjectInput, ApiException
import requests
from pytz import timezone, utc
from datetime import datetime


def create_new_contact(email, first_name, last_name):

    client = hubspot.Client.create(api_key=os.environ.get("HUBSPOT_API_KEY"))

    properties = {
        "email": email,
        "firstname": first_name,
        "lastname": last_name,
        "hubspot_owner_id":os.environ.get("HUBSPOT_OWNER_ID"),
    }

    simple_public_object_input = SimplePublicObjectInput(properties=properties)

    try:
        api_response = client.crm.contacts.basic_api.create(simple_public_object_input=simple_public_object_input)
        return api_response.id
    except ApiException as e:
        id_split_one = str(e).split('{"status":"error","message":"Contact already exists. Existing ID: ')
        id_split_two = id_split_one[1].split('"')
        existing_contact_id = id_split_two[0]
        return existing_contact_id


def create_new_note(message):

    url = "https://api.hubapi.com/crm/v3/objects/notes"

    querystring = {"hapikey":os.environ.get("HUBSPOT_API_KEY")}

    tz = timezone(os.environ.get("TZ"))

    utcdt = utc.localize(
        datetime(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
            hour=datetime.now().hour,
            minute=datetime.now().minute,
            second=datetime.now().second,
        )
    ).astimezone(tz)

    ts = int(utcdt.timestamp()*1000)

    payload = "{\"properties\":{\"hs_timestamp\":\"%s\",\"hs_note_body\":\"%s\",\"hubspot_owner_id\":\"%s\"}}" % (ts, message, os.environ.get("HUBSPOT_OWNER_ID"))

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    json = response.json()

    return json["id"]


def associate_note_with_contact(contact_id, note_id):

    url = f"https://api.hubapi.com/crm/v3/objects/notes/{note_id}/associations/contact/{contact_id}/202"

    querystring = {"hapikey":os.environ.get("HUBSPOT_API_KEY")}

    headers = {'accept': 'application/json'}

    requests.request("PUT", url, headers=headers, params=querystring)


def create_new_deal(contact_id, deal_amount):

    tz = timezone(os.environ.get("TZ"))

    utcdt = utc.localize(
        datetime(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
            hour=datetime.now().hour,
            minute=datetime.now().minute,
            second=datetime.now().second,
        )
    ).astimezone(tz)

    ts = int(utcdt.timestamp()*1000)

    url= f'https://api.hubapi.com/deals/v1/deal?hapikey={os.environ.get("HUBSPOT_API_KEY")}'
    
    headers={}
    
    headers["Content-Type"]="application/json"
    
    data = json.dumps({
    "associations": {
        "associatedVids": [
        contact_id
        ]
    },
    "properties": [
        {
        "value": f"Website Sale",
        "name": "dealname"
        },
        {
        "value": "closedwon",
        "name": "dealstage"
        },
        {
        "value": "default",
        "name": "pipeline"
        },
        {
        "value": os.environ.get("HUBSPOT_OWNER_ID"),
        "name": "hubspot_owner_id"
        },
        {
        "value": ts,
        "name": "closedate"
        },
        {
        "value": deal_amount,
        "name": "amount"
        },
        {
        "value": "newbusiness",
        "name": "dealtype"
        }
      ]
    })

    requests.post(url, headers = headers, data = data)