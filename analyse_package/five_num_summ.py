"""
Takes in a list of integers and returns a dictionary of the five number summary.

Args:
    data (list): list of integers

Returns:
    dict : a dictionary of the five number summary (with each value rounded
            to the second decimal)
"""

def five_num_summ(data):
    def q1(data):
        data2 = sorted(data, reverse=False)
        n = len(data2)
        if n % 2 == 0:
            l_data = data2[0:n//2]
        else:
            l_data = data2[0:n//2+1]
        n2 = len(l_data)
        if n2 % 2 == 0:
            m1 = data2[n2//2]
            m2 = data2[n2//2 - 1]
            q1 = (m1 + m2)/2
        else:
            q1 = data2[n2//2]
        return round(q1, 2)

    def q3(data):
        data3 = sorted(data, reverse=False)
        n = len(data3)
        l_data3 = data3[n//2:]
        n3 = len(l_data3)
        if n3 % 2 == 0:
            m1 = l_data3[n3//2]
            m2 = l_data3[n3//2 - 1]
            q3 = (m1 + m2)/2
        else:
            q3 = l_data3[n3//2]
        return round(q3, 2)

    def mid(data):
        data2 = sorted(data, reverse=False)
        n = len(data)
        if n % 2 == 0:
            m1 = data2[n//2]
            m2 = data2[n//2 - 1]
            median = (m1 + m2)/2
        else:
            median = data2[n//2]
        return round(median, 2)

    maximum = lambda data : round(max(data), 2)

    minimum = lambda data : round(min(data), 2)
    fns = {'max': maximum(data), 'median': mid(data),
     'min': minimum(data), 'q1': q1(data), 'q3': q3(data)}
    return fns
