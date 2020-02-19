from analyse_package import analyse_package
import pandas as pd
import numpy as np

ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()

mun_dict = { '@CityofCTAlerts' : 'Cape Town',
        '@CityPowerJhb' : 'Johannesburg',
        '@eThekwiniM' : 'eThekwini' ,
        '@EMMInfo' : 'Ekurhuleni',
        '@centlecutility' : 'Mangaung',
        '@NMBmunicipality' : 'Nelson Mandela Bay',
        '@CityTshwane' : 'Tshwane'}

stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon',
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former',
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through',
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to',
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still',
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose',
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take',
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind',
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next',
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor',
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least',
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call',
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all',
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves',
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others',
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody',
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten',
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty',
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine',
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too',
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our',
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon',
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me',
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}



def dictionary_of_metrics():
    """
    Testing function 1
    """
    assert dictionary_of_metrics(gauteng) == {'mean': 26244.42,
                                   'median': 24403.5,
                                   'var': 108160153.17,
                                   'std': 10400.01,
                                   'min': 8842.0,
                                   'max': 39660.0}, 'correct'
def five_num_summ():
    """
    Testing function 2
    """
    assert five_num_summary(gauteng) == {'max': 39660.0,
                            'median': 24403.5,
                            'min': 8842.0,
                            'q1': 18653.0,
                            'q3': 36372.0}, 'correct'

def date_parser():
    """
Testing function 3
    """
    assert date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']
                                        , 'correct'
    assert date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20']
                                        , 'correct'

def extract_municipality_hashtags():
    """
    Testing function 4
    """
    municipality1=[]
    for i in range(0, len(twitter_df)):
        found=""
        cityFound=""
        for handle, city in mun_dict.items():
            value=twitter_df.iloc[i][0].find(handle)
            if value is not -1:
                cityFound=city
            else:
                cityFound=np.nan
        municipality1.append(cityFound)
    municipality = pd.DataFrame(municipality1, columns=['municipality'])
    assert extract_municipality_hashtags(twitter_df)['municipality']==municipality,
                                                                        'correct'
    hashes = [list(filter(lambda x: x.startswith("#"), twitter_df['Tweets'][i].lower().split())) for i in range(len(df.index.values))]
    hashtags = pd.DataFrame([np.nan if x == [] else x for x in hashes ], columns=['hashtags'])
    assert extract_municipality_hashtags(twitter_df)['hashtags'] == hashtags,
                                                                    'correct'

def number_of_tweets_per_day():
    """
    Testing function 5
    """
    assert number_of_tweets_per_day(twitter_df).index == Index(['2019-11-20', '2019-11-21', '2019-11-22', '2019-11-23', '2019-11-24',
       '2019-11-25', '2019-11-26', '2019-11-27', '2019-11-28', '2019-11-29'],
      dtype='object', name='Date'), 'correct'

def word_spliter():
    """
    Testing function 6
    """
    Split_tweets = [x.lower().split() for x in df['Tweets']]
    d = pd.DataFrame(np.array(Split_tweets), columns=['Split Tweets'])
    assert word_spliter(twitter_df)['Split Tweets'] == d, 'correct'

def stop_words_remover():
    """
    Testing function 7
    """
    date_list = [dates[i].split()[0] for i in range(len(dates))]
    tweets_list = list(df['Tweets'])
    z = list(zip(date_list,tweets_list))
    k = [y.lower() for x,y in z]
    stop_words = tuple(stop_words_dict['stopwords'])
    no_swords_list = [list(filter(lambda x: x not in stop_words, k[i].split()))
               for i in range(len(twitter_df.index.values))]
    no_swords_df = pd.DataFrame(np.array(no_swords_list), columns=['Without Stop Words'])
    assert stop_words_remover(twitter_df)['Without Stop Words'] == no_swords_df,
                                                                    'correct'
