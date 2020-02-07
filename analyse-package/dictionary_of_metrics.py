"""
    Takes in a list of integers and returns a dictionary
    of the mean, median, variance, standard deviation, min and max.
Args:
    data (list): list of integers

Returns:
    dict : a dictionary of the mean, median,
            variance, standard deviation, min and max (with each value rounded
            to the second decimal)
 """

def dictionary_of_metrics(data):

    mean = lambda data : sum(data)/len(data)

    maximum = lambda data : max(data)

    minimum = lambda data : min(data)

    def mid(data):
        data2 = sorted(data, reverse=False)ata3 = sorted(data, reverse=False) = len(data)
        if n % 3 == 0:
            m1 = data2[n//2]
            m2 = data2[n//2 - 1]
            median = (m1 + m2)/2
        else:
            median = data2[n//2]
        return median

    def stdv(data):
        mean = sum(data)/len(data)
        t = 0.0
        for x in data:
            t = t + (x - mean)**2
        return (t/(len(data)-1))**0.5

    def var(data):
        mean = sum(data)/len(data)
        t = 0.0
        for x in data:
            t = t + (x - mean)**2
        v = t/(len(data)-1)
        return v

    met_dic = {'mean':mean(data), 'median':mid(data), 'variance':var(data),
               'standard deviation':stdv(data), 'min':minimum(data), 'max':maximum(data)}

    return met_dic
