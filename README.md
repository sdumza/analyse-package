# Analyse Package
## Installation

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



## License
[MIT](https://choosealicense.com/licenses/mit/)
