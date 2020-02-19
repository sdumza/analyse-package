def dictionary_of_metrics(items):
    """
    Takes in a list of integers and returns a dictionary of the five number summary.
    The function returns numerical values rounded to two decimal places.
    Args:
        items: list of integers

    Returns:
        dict (dictionary): a dict with keys 'max', 'median', 'min', 'q1',
                        and 'q3' corresponding to the maximum, median, minimum, first quartile and third quartile, respectively.
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
    Takes in a list of integers and returns a dictionary of the five number summary.
    The function returns numerical values rounded to two decimal places.
    Args:
        data (list): list of integers

    Returns:
        dict (dictionary): a dict with keys 'max', 'median', 'min', 'q1',
                            and 'q3' corresponding to the maximum, median, minimum, first quartile and third quartile, respectively.
    """
    import numpy as np
    def q1(items):
        q1 = np.percentile(items, 25)
        return round(q1, 2)

    def q3(items):
        q3 = np.percentile(items, 75)
        return round(q3, 2)

    def mid(items):
        median = np.median(items)
        return round(median, 2)

    maximum = lambda items : round(max(items), 2)

    minimum = lambda items : round(min(items), 2)

    fns = {'max': maximum(items), 'median': mid(items), 'min': minimum(items), 'q1': q1(items), 'q3': q3(items)}

    return fns

def date_parser(items):
    """
    Takes in a list of strings as input and returns a list of strings
    Args:
        items (list): a list of strings with each string formatted
                        as 'yyyy-mm-dd hh:mm:ss'

    Returns:
        list : a list of strings with each string formatted as 'yyyy-mm-dd'
    """

    just_dates = [i[0:10] for i in items]
    return just_dates

def extract_municipality_hashtags(df):
    """
    Takes in a pandas dataframe.
    Extract municipality from a tweet using dictionaries.
    Extract hashtags from a tweet using dictionaries.

    Args:
        df (DataFrame): pandas data DataFrame

    Returns:
        DataFrame: with information about municipality and hashtags from each tweet.

    """
    import numpy as np
    import pandas as pd

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
    """
   The function takes a pandas dataframe as inpit and returns a new dataframe,
   grouped by day, with the numbers of tweets for that day

        Args:
            df (DataFrame): a twitter DataFrame

        Returns:
            DataFrame: with index named "Date" and the column of the new
                        dataframe should be 'tweets', corresponding to the date and number
                        of 'Tweets, corresponding to the date and number of tweets, respectively.
                        The date and number be formated as yyyy-mm-dd

"""
    import numpy as np
    import pandas as pd
    df1=df['Date'].str.split(expand = True)
    df['Date'] = df1[0]
    df=df.groupby('Date').count()
    return df

def word_splitter(df):
    """
    Splits the sentences in a dataframe's column into a list of the separate words.

    Args:
        df (DataFrame): a twitter DataFrame

    Returns:
        DataFrame: The original twitter DataFrame with a columns "Tweets"
    """
    import numpy as np
    import pandas as pd

    Split_tweets = [x.lower().split() for x in df['Tweets']]
    d = pd.DataFrame(np.array(Split_tweets), columns=['Split Tweets'])
    df_split = df.join(d, lsuffix='Date', rsuffix='Split Tweets')

    return df_split

def stop_words_remover(df):
    """
    Removes English stop words from a tweet, tokenises the tweet and places in
    them in a column named "Without Stop Words". The stopwords are defined in
    the stop_words_dict variable given.
    Args:
        df (DataFrame): a twitter DataFrame

    Returns:
        DataFrame: The original twitter DataFrame with a columns "Without Stop Words"
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
