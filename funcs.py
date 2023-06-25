import re

def nums_formatting(contacts_list):
    match = r"(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)"
    formatted_nums = r"+7(\4)\8-\11-\14\15\17\18\19\20"
    contacts_list_updated = list()
    for contact in contacts_list:
        contact_string = ','.join(contact)
        nums_formatted = re.sub(match, formatted_nums, contact_string)
        card_as_list = nums_formatted.split(',')
        print(card_as_list)
        contacts_list_updated.append(card_as_list)
    return contacts_list_updated

def names_formatting(contacts_list):
    match = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    formatted_names = r'\1\3\10\4\6\9\7\8'
    contacts_list_updated = list()
    for contact in contacts_list:
        contact_string = ','.join(contact)
        names_formatted = re.sub(match, formatted_names, contact_string)
        card_as_list = names_formatted.split(',')
        contacts_list_updated.append(card_as_list)
    return contacts_list_updated

def merge_duplicates(contacts_list):
    merged_contacts = {}
    for contact in contacts_list:
        key = (contact[0], contact[1])
        if key not in merged_contacts:
            merged_contacts[key] = contact
    merged_list = list(merged_contacts.values())
    return merged_list