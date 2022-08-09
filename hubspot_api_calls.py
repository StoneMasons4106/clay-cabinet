import hubspot
import os
import json
from hubspot.crm.contacts import SimplePublicObjectInput, ApiException
import requests
from pytz import timezone, utc
from datetime import datetime


def create_new_contact(email, first_name, last_name):

    client = hubspot.Client.create(access_token=os.environ.get("HUBSPOT_API_KEY"))

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


def add_phone_number_to_contact(contact_id, phone_number):
    
    client = hubspot.Client.create(access_token=os.environ.get("HUBSPOT_API_KEY"))

    properties = {
        "phone": phone_number,
    }
    
    simple_public_object_input = SimplePublicObjectInput(properties=properties)
    
    client.crm.contacts.basic_api.update(contact_id=contact_id, simple_public_object_input=simple_public_object_input)


def create_new_note(message):

    url = "https://api.hubapi.com/crm/v3/objects/notes"

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
        'authorization': f'Bearer {os.environ.get("HUBSPOT_API_KEY")}',
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    json = response.json()
    return json["id"]


def associate_note_with_contact(contact_id, note_id):

    url = f"https://api.hubapi.com/crm/v3/objects/notes/{note_id}/associations/contact/{contact_id}/202"

    headers = {
        'accept': 'application/json',
        'authorization': f'Bearer {os.environ.get("HUBSPOT_API_KEY")}',
    }

    requests.request("PUT", url, headers=headers)


def create_new_deal(deal_amount, full_name, order_no):

    client = hubspot.Client.create(access_token=os.environ.get("HUBSPOT_API_KEY"))

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

    properties = {
        "dealname": f"{full_name} - {order_no}",
        "dealstage": "closedwon",
        "pipeline": "default",
        "hubspot_owner_id": os.environ.get("HUBSPOT_OWNER_ID"),
        "closedate": ts,
        "amount": deal_amount,
        "dealtype":"newbusiness",
    }

    simple_public_object_input = SimplePublicObjectInput(properties=properties)
    
    try:
        api_response = client.crm.deals.basic_api.create(simple_public_object_input=simple_public_object_input)
        return api_response.id
    except ApiException as e:
        print("Exception when calling basic_api->create: %s\n" % e)


def associate_deal_with_contact(contact_id, deal_id):

    client = hubspot.Client.create(access_token=os.environ.get("HUBSPOT_API_KEY"))

    try:
        client.crm.deals.associations_api.create(deal_id=deal_id, to_object_type="contact", to_object_id=contact_id, association_type="3")
    except ApiException as e:
        print("Exception when calling associations_api->create: %s\n" % e)


def associate_note_with_deal(deal_id, note_id):

    url = f"https://api.hubapi.com/crm/v4/objects/notes/{note_id}/associations/deal/{deal_id}"

    payload = "[{\"associationCategory\":\"HUBSPOT_DEFINED\",\"associationTypeId\":214}]"

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'authorization': f'Bearer {os.environ.get("HUBSPOT_API_KEY")}',
    }

    requests.request("PUT", url, data=payload, headers=headers)