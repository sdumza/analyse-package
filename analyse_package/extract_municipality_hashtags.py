"""
    Takes in a pandas dataframe and returns the same dataframe which is modified
    The function does the following:
         1. Extract the municipality from a tweet using the given dictonary
          into a new column in the same dataframe.
         2. Extract the hashtag from a tweet into a new column in the
          same data frame.
         3. The column headers should be "municipality" & "hashtags"
          respectively.
         4. For those tweets which don't have the either a municipality
          nor a hashtag, fill it with np.nan.

"""
import numpy as np
import pandas as pd
def extract_municipality_hashtags(df):

    municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}
    hashes = [list(filter(lambda x: x.startswith("#"), df['Tweets']
                [i].lower().split())) for i in range(len(df.index.values))]
    hashtags = pd.DataFrame([np.nan if x == [] else x for x in hashes ],
                columns=['hashtags'])

    m1 = [list(filter(lambda x: x.startswith("@"), df['Tweets'][i].split()))
            for i in range(len(df.index.values))]
    flat_m1 = []
    for sublist in m1:
        for item in sublist:
            flat_m1.append(item)

    municipality = pd.DataFrame([x if x in municipality_dict else np.nan
                    for x in flat_m1], columns=['municipality'])
    extracted_municipality = df.join(municipality, lsuffix='Date',
                                rsuffix='municipality')
    extracted_municipality_hashtags = extracted_municipality.join(hashtags,
                                    lsuffix='municipality', rsuffix='hashtags')

    return extracted_municipality_hashtags
