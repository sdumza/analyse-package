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

def dictionary_of_metrics(items):
    def mean(items):
        mean = np.mean(items)
        return mean
        maximum = lambda items : max(items)
        minimum = lambda items : min(items)
    def mid(items):
        median = np.median(items)
        return median
    def stdv(items):
        std = np.std(items, ddof=1)
        return std

    def var(items):
        var = np.var(items, ddof=1)
        return var

    met_dic = {'mean':round(mean(items), 2), 'median':round(mid(items), 2), 'var':round(var(items), 2),
               'std':round(stdv(items), 2), 'min':round(minimum(items), 2), 'max':round(maximum(items), 2)}
    return met_dic
