# Analyse Package
Analyse Package is a Python module which deals with producing summary statistics
specific to the ESKOM energy crisis. The anticipated use of the functions is
to aid in the elimination of ESKOM's unreliable energy distribution in South Africa,
by building a set of dashboards which will provide key insights about stabilizing
energy generation and distribution.


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the
Analyse Package.
```bash
pip install git+https://github.com/kopano-m/analyse-package.git
```
## Update
```bash
pip install --upgrade git+https://github.com/kopano-m/analyse-package.git
```
## Usage
### Function 1
```python
from analyse_package import analyse_functions as af

af.dictionary_of_metrics(list_of_integers) # returns a dictionary

"""  Takes in a list of integers and returns a dictionary of the five number summary.
  The function returns numerical values rounded to two decimal places.
  Args:
      items: list of integers

  Returns:
      dict (dictionary): a dict with keys 'max','median','min','q1', and 'q3' corresponding to the maximum, median, minimum, first quartile and third quartile, respectively.
"""
```
### Function 2
```python
af.five_num_summ(list_of_integers) # returns a dictionary
"""
  Takes in a list of integers and returns a dictionary of the five number summary.
  The function returns numerical values rounded to two decimal places.
  Args:
      data (list): list of integers

  Returns:
      dict (dictionary): a dict with keys 'max', 'median', 'min', 'q1',
                          and 'q3' corresponding to the maximum, median, minimum, first quartile and third quartile, respectively.
  """
  ```
### Function 3
  ```python
af.date_parser(list_of_strings) # returns a list_of_strings
"""
  Takes in a list of strings as input and returns a list of strings
  Args:
      items (list): a list of strings with each string formatted
                      as 'yyyy-mm-dd hh:mm:ss'

  Returns:
      list : a list of strings with each string formatted as 'yyyy-mm-dd'
  """
  ```
### Function 4
  ```python
af.extract_municipality_hashtags(DataFrame) # returns a modified DataFrame
"""
  Takes in a pandas dataframe.
  Extract municipality from a tweet using dictionaries.
  Extract hashtags from a tweet using dictionaries.

  Args:
      df (DataFrame): pandas data DataFrame

  Returns:
      DataFrame: with information about municipality and hashtags from each tweet.

  """
  ```
### Function 5
  ```python
af.number_of_tweets_per_day(DataFrame) # returns modified DataFrame
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
```
### Function 6
```python
af.word_splitter(DataFrame) # returns a modified DataFrame
"""
  Splits the sentences in a dataframe's column into a list of the separate words.

  Args:
      df (DataFrame): a twitter DataFrame

  Returns:
      DataFrame: The original twitter DataFrame with a columns "Tweets"
  """
```
### Function 7
```python
af.stop_words_remover(DataFrame) # returns a modified DataFrame
"""
  Removes English stop words from a tweet, tokenises the tweet and places in
  them in a column named "Without Stop Words". The stopwords are defined in
  the stop_words_dict variable given.
  Args:
      df (DataFrame): a twitter DataFrame

  Returns:
      DataFrame: The original twitter DataFrame with a columns "Without Stop Words"
  """
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)

## Authors

Dumisani Shabalala dumisan@protonmail.com<br/>
Kopano Monyobo kopanomonyobo@gmail.com<br/>
Nkopane Guada labonneguada@gmail.com<br/>
Lehlohonolo Monareng lehlohonolomonareng@yahoo.com<br/>
Lucas Sithole lucas317sithole@gmail.com
