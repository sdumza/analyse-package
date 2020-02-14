#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
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
    fns = {'max': maximum(data), 'median': mid(data), 'min': minimum(data), 'q1': q1(data), 'q3': q3(data)}
    return fns

def date_parser(items):
    dates=[]
    for i in range(len(items)):
        datesOnly=items[i].split()[0]
        dates.append(datesOnly)
    return dates


def extract_municipality_hashtags(df):

    mun_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}
    hashes = [list(filter(lambda x: x.startswith("#"), df['Tweets'][i].split())) for i in range(len(df.index.values))]
    hashtags = pd.DataFrame([np.nan if x == [] else x for x in hashes ], columns=['hashtags']) 
            
    municipality=[]
for i in range(0, len(df)):
    found=""
    cityFound=""
    for handle, city in mun_dict.items():
        value=df.iloc[i][0].find(handle)
        if value is not -1:
            cityFound=city
        else:
            cityFound=np.nan
    municipality.append(cityFound)
    extracted_municipality = df.join(hashtags, lsuffix='municipality', rsuffix='hashtags')
    extracted_municipality_hashtags = extracted_municipality.join(hashtags, lsuffix='municipality', rsuffix='hashtags')

    return extracted_municipality_hashtags


def number_of_tweets_per_day(df):
    #import pandas as pd
    # Insert calculations section
    #new_dataframe = (DatetimeIndex.date, col_name = 'Tweets')
    #return new_dataframe
  pass

def word_spliter(df):

  ### Code Here

  pass


def stop_words_remover(df):
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

