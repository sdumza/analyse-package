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

```python
from analyse_package import analyse_functions as af

af.dictionary_of_metrics(list_of_integers) # returns a dictionary
af.five_num_summ(list_of_integers) # returns a dictionary
af.date_parser(list_of_strings) # returns a list_of_strings
af.extract_municipality_hashtags(DataFrame) # returns a modified DataFrame
af.number_of_tweets_per_day(DataFrame) # returns modified DataFrame
af.word_splitter(DataFrame) # returns a modified DataFrame
af.stop_words_remover(DataFrame) # returns a modified DataFrame
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
