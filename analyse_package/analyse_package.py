def dictionary_of_metrics(items):
    """
    The function should allow list as input.
    The function will return dictionary_of_metrics as a dict.
    Standard deviation and variance must be unbiased.
    All the values of dictionary_of_metrics must be rounded to 2 decimals.
    """
    import numpy as np
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

def five_num_summ(data):
    """
    function should take a list as input
The function should return a dict with keys 'max', 'median', 'min', 'q1', and 'q3' corresponding to the maximum, median, minimum, first quartile and third quartile, respectively. You may use numpy functions to aid in your calculations.
functions should return numerical values should be rounded to two decimal places
    """
    import numpy as np
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
    fns = {'max': maximum(data), 'median': mid(data), 'min': minimum(data), 'q1': q1(data), 'q3': q3(data)}
    return fns

def date_parser(items):
    """
    function should take a list of strings as input.
Each string in the input list is formatted as 'yyyy-mm-dd hh:mm:ss'.
The function should return a list of strings where each element in the
returned list contains only the date in the 'yyyy-mm-dd' format.
    """
       just_dates = [i[0:10] for i in dates ]
    return just_dates



def extract_municipality_hashtags(df):
    import numpy as np
    import pandas as pd
"""
    The function should take pandas as a dataframe.
    Extract municipality from a tweet using dictionaries.
    Extract hashtags from a tweet using dictionaries.

    Args:
        df (DataFrame): pandas data DataFrame



    Return:
        DataFrame: with information about municipality and hashtags from each tweet.

"""
    mun_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}

    municipality1=[]
    for i in range(0, len(df)):
        found=""
        cityFound=""
        for handle, city in mun_dict.items():
            value=df.iloc[i][0].find(handle)
            if value is not -1:
                cityFound=city
            else:
                cityFound=np.nan
        municipality1.append(cityFound)

    municipality = pd.DataFrame(municipality1, columns=['municipality'])
    municipality2 = df.join(municipality, lsuffix='Date', rsuffix='municipality')
    hashes = [list(filter(lambda x: x.startswith("#"), df['Tweets'][i].lower().split())) for i in range(len(df.index.values))]
    hashtags = pd.DataFrame([np.nan if x == [] else x for x in hashes ], columns=['hashtags'])
    extracted_municipality_hashtags = municipality2.join(hashtags, lsuffix='municipality', rsuffix='hashtags')

    return extracted_municipality_hashtags


def number_of_tweets_per_day(df):

   """ The function takes a pandas dataframe as inpit
        The function returns a new dataframe , grouped by day, with the numbers of tweets for that day
        Get index of the new dataframe should be named "Date", and the column of the new dataframe should be 'tweets', corresponding to the date and number of 'Tweets, corresponding to the date and number of tweets, respectively.
        The date and number be formated as yyyy-mm-dd, and should be a datetime object """
    df1=df['Date'].str.split(expand = True)
    df['Date'] = df1[0]
    df=df.groupby('Date').count()
    return df

def word_spliter(df):


    Split_tweets = [x.lower().split() for x in df['Tweets']]
    d = pd.DataFrame(np.array(Split_tweets), columns=['Split Tweets'])
    df_split = df.join(d, lsuffix='Date', rsuffix='Split Tweets')

    return df_split


def stop_words_remover(df):
    """
    function removes english stop words from a tweet.with the Specifications
    It should take a pandas dataframe as input.
    Should tokenise the sentences according to the definition in function 6. Note that function 6 cannot be called within this function.
    Should remove all stop words in the tokenised list. The stopwords are defined in the stop_words_dict variable defined at the top of this notebook.
    The resulting tokenised list should be placed in a column named "Without Stop Words".
    The function should modify the input dataframe it should also return the modified dataframe.

    """
    import numpy as np
    import pandas as pd

    date_list = [dates[i].split()[0] for i in range(len(dates))]
    tweets_list = list(df['Tweets'])
    z = list(zip(date_list,tweets_list))
    k = [y.lower() for x,y in z]
    stop_words = tuple(stop_words_dict['stopwords'])
    no_swords_list = [list(filter(lambda x: x not in stop_words, k[i].split()))
               for i in range(len(twitter_df.index.values))]
    no_swords_df = pd.DataFrame(np.array(no_swords_list), columns=['Without Stop Words'])
    stop_words_remover_df = df.join(no_swords_df, lsuffix=['Date'], rsuffix=['Without Stop Words'])
    return stop_words_remover_df
