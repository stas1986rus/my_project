def filter_by_state(list_of_dictionaries, status='EXECUTED'):

    new_list = []
    for dictionaries in list_of_dictionaries:
        if dictionaries.get('state') == status:
            new_list.append(dictionaries)
    return new_list

def sort_by_date(list_of_dictionaries, reverse_list=True):
    sorted_list = sorted(list_of_dictionaries, key=lambda d: d['date'], reverse=reverse_list)
    return sorted_list