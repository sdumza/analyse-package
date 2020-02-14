"""
    Takes a list of datetime strings and converts it into a list
     of strings with only the date

Args:
    list_dates (list): a list of datetime strings

Returns:
    list: a list
            of strings with only the date

"""

def date_parser(list_dates):
    return [list_dates[i].split()[0] for i in range(len(list_dates))]
