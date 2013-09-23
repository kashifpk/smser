#!/usr/bin/env python3

import android

droid = android.Android()


def get_smses(only_unread=True):
    res = droid.smsGetMessages(only_unread)
    if not res.error:
        return res.result

def get_contacts():

    contacts = {}
    rev_contacts = {}

    atts = ['contact_id', 'raw_contact_id', 'photo_uri', 'photo_file_id', 'has_phone_number', 'data1', 'data4',
            'display_name', 'photo_thumb_uri', 'photo_id', 'starred']
    raw_contacts = droid.queryContent("content://com.android.contacts/data/phones", atts).result
    for C in raw_contacts:
        if '1' == C['has_phone_number']:
            if 'data4' not in C:
                #print(C)
                continue

            number = C['data4']
            name = C['display_name']
            if number:
                rev_contacts[number] = name
                if name in contacts:
                    contacts[name].append(number)
                else:
                    contacts[name] = [number, ]

    return contacts, rev_contacts

def send_sms(number, msg):
    droid.smsSend(number, msg)

def mark_as_read(msgs):
    msg_ids = []
    for m in msgs:
        msg_ids.append(m['_id'])
    droid.smsMarkMessageRead(msg_ids, True)


if '__main__' == __name__:
    pass

