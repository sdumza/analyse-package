#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd

def dictionary_of_metrics(data):

    mean = lambda data : sum(data)/len(data)
        
    maximum = lambda data : max(data)
    
    minimum = lambda data : min(data)
    
    def mid(data):
        data2 = sorted(data, reverse=False) 
        n = len(data)
        if n % 2 == 0: 
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

def date_parser(list_dates):
    return [list_dates[i].split()[0] for i in range(len(list_dates))]

def extract_municipality_hashtags(df):

    municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}
    hashes = [list(filter(lambda x: x.startswith("#"), df['Tweets'][i].split())) for i in range(len(df.index.values))]
    hashtags = pd.DataFrame([np.nan if x == [] else x for x in hashes ], columns=['hashtags']) 
    
    m1 = [list(filter(lambda x: x.startswith("@"), df['Tweets'][i].split())) for i in range(len(df.index.values))]
    flat_m1 = []
    for sublist in m1:
        for item in sublist:
            flat_m1.append(item)
            
    municipality = pd.DataFrame([x if x in municipality_dict else np.nan for x in flat_m1], columns=['municipality'])
    extracted_municipality = df.join(municipality, lsuffix='Date', rsuffix='municipality')
    extracted_municipality_hashtags = extracted_municipality.join(hashtags, lsuffix='municipality', rsuffix='hashtags')

    return extracted_municipality_hashtags


def number_of_tweets_per_day(df):

  ### Code Here

  pass

def word_spliter(df):

  ### Code Here

  pass


def stop_words_http_remover(df):

  # Code Here

  pass

