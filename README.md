# ling_feature_extractor
## Description
A linguistic feature extraction program that has `95 general lexico-grammatical features built in`. It is built to be `corpus-linguistic tool` to study langauge and gender macroscopically, but since all the built-in features are very general, it is possible to use it jsut a general tool to study textual variation of spoken or written texts. Besides, the program is also part of my thesis project. The thesis version contains three more built-in linguistic features, which are deleted in the main version because those features are not deemed as generally accessible in a normal corpus, i.e., words per utterance, number of utterances, and number of overlaps.  

`As for the linguistic features`: Over 2/3 of them come from Biber et al.(2006) with 42 features also present in Biber(1988). These features are generally known as part of the Multi-Dimensional (MD) analysis framework.

`As for the program`: the program can be very useful as a search engine to match desired pattern in a corpus. All it takes is a corpus and corresponding pattern of the deisred feature written in Regular Expression. 

`As for limitations`, The program is mainly tested on two online accessible corpora, namely [British Academic Spoken Corpus](http://www.reading.ac.uk/AcaDepts/ll/base_corpus/) and [Michigan Corpus of Academic Englush](https://quod.lib.umich.edu/cgi/c/corpus/corpus?page=home;c=micase;cc=micase), and since different corpora have different transcripting conventions, the current program cannot predict what kind of noisy information should be cleaned before tagging and feature extracting. Some problems might occur because of that. However, generally, the program is robust to deal with normal corpus. And it is also possible for some users to change the text cleaning rules in text_processor.py under LFE folder to make the program work speicifically for a taget corpus. Besides, the feature extraction is based on the assumption that the corpus is unpunctuated, but this can be also changed by removing the unpunctuation rule in text_processor.py.

## Prerequisites
The program is written in pure Python language, the release of which should be over 3.6 to make the program properly because of some Python packages it uses. However, Java 1.8+ is also required since StanfordCoreNLP is employed, which is written in pure Java. To use the functionalities of StanfordCoreNLP, a Python Wrapper called stanfordcorenlp is used here.

- `Computer Langauges`: 
   - Python 3.6+: check with cmd: `python --version` or `python3 --version` ([Download Page](https://www.python.org/downloads/)); 
   - Java 1.8+: check with cmd: 'java --version' ([Download Page](https://www.java.com/en/download/)). 
- `Python packages`

| Package | Description | Pip download | 
| :---: | :---: | :---: |
| [stanfordcorenlp](https://github.com/Lynten/stanford-corenlp) | A Python wrapper for StanforeCoreNLP | `pip/pip3 install stanfordcorenlp` |
| [pandas](https://pandas.pydata.org) | Used for storing extracted feature frequencies  | `pip/pip3 install pandas` |

Besides, built-in packages are heavily employed in the program, especially the built-in `re` package for Regular Expression.

## Installation
- Directly download from this page and cd to the project folder.
- By pip: `pip/pip3 install LFExtractor`

## Usage
### path to StanfordCoreNLP
**Please specify _the directory to StanfordCoreNLP_ in the text_processor.py under LFE folder when first using the program.**
- [X] `nlp = StanfordCoreNLP("/path/to/StanfordCoreNLP/")` 

Example: nlp = StanfordCoreNLP("/Users/wzx/p_package/stanford-corenlp-4.1.0")

### Dealing with a corpus of files
```
from LFE.extractor import CorpusLFE
lfe = CorpusLFE('/directory/to/the/corpus/under/analysis/')
# get frequency data and tagged corpus and extracted features by default
lfe.corpus_feature_fre_extraction() lfe.corpus_feature_fre_extraction()    # lfe.corpus_feature_fre_extraction(normalized_rate=100, save_tagged_corpus=True, save_extracted_features=True, left=0, right=0). 
# change the normalized_rate, trun off tagged text and leave extracted text with specified context to display
lfe.corpus_feature_fre_extraction(1000, False, True, 2, 3) # extract frequency data only, and the data are normalized at 1000 words.  

# get frequency data only
lfe.corpus_feature_fre_extraction(save_tagged_corpus=False, save_extracted_features=False)
# get tagged corpus only
lfe.save_tagged_corpus()
# get extracted feature only
lfe.save_corpus_extracted_features()   # lfe.save_corpus_extracted_features(left=0, right=0)
# set how many words to display besides the target pattern
lfe.save_corpus_extracted_features(2, 3)

# extract and save specific linguistic feature by feature name
# to see the built-in features' names, use `show_feature_names()`
from LFE.extractor import *
print(show_feature_names())   # Six letter words and longer, Contraction, Agentless passive, By passive...
# specify which feature to extract and save
lfe.save_corpus_one_extracted_feature_by_name('Six letter words and longer')

# extract and save specific linguistic feature by feature regex, for example, 'you know' 
lfe.save_corpus_one_extracted_feature_by_regex(r'you_\S+ know_\S+', 2, 2, feature_name='You Know')  # Extract phrase 'you know' along with 2 words spanning around. Also remember the '_\S+' at the end of each word since the corpus will be automatically POS tagged.
# for more complex structure, the features_set.py can be ultilized, for example, to extract "article + adj + noun" structure
from LFE import features_set as fs
ART = fs.ART
ADJ = fs.ADJ
NOUN = fs.NOUN
lfe.save_corpus_one_extracted_feature_by_regex(rf'{ART} {ADJ} {NOUN}', 2, 2, 'Noun phrase')
# result example (use test_sample): away_RB by_IN	【 the_DT whole_JJ thing_NN 】	In_IN fact_NN 
```

### Dealing with a text
```
from LFE import extractor as ex
# check the functionalities contained in ex by dir(ex)
# show built-in feature names
print(ex.show_feature_names())   # Six letter words and longer, Contraction, Agentless passive, By passive...
# get built-in features' regex by its name
print(ex.get_feature_regex_by_name('Contraction'))  # (n't| '\S\S?)_[^P]\S+
# get built-in features' names by regex
print(ex.get_feature_name_by_regex(r"(n't| '\S\S?)_[^P]\S+"))  # Contraction

# text processing
# tagged file
ex.save_single_tagged_text('/path/to/the/file')
# cleaned file
ex.save_single_cleaned_text('/path/to/the/file')

# display extracted feature by name
res = ex.display_extracted_feature_by_name('/path/to/the/file', 'Contraction', left=0, right=0)
print(res)  #  's_VBZ, n't_NEG, 've_VBP...
# save the result
ex.save_extracted_feature_by_name('/path/to/the/file', 'Contraction', left=0, right=0)

# display extracted feature by regex, for example, noun phrase
from LFE import features_set as fs
ART = fs.ART
ADJ = fs.ADJ
NOUN = fs.NOUN
res = ex.display_extracted_feature_by_regex(rf'{ART} {ADJ} {NOUN}', 2, 2, 'Noun phrase')
print(res)  # One_CD is_VBZ	【 the_DT extraordinary_JJ evidence_NN 】	of_IN human_JJ
# save the result
ex.save_extracted_feature_by_regex(rf'{ART} {ADJ} {NOUN}', 2, 2, 'Noun phrase')

# get the frequency data of all the linguistic features for a file 
res = ex.get_single_file_feature_fre(file_path, normalized_rate=100, save_tagged_file=True, save_extracted_features=True, left=0, right=0)
print(res)
```

### Dealing with a part of a corpus
```
from LFE.extractor import *
lfe = CorpusLFE('/directory/to/the/corpus/under/analysis/')
# get_filepath_list and select the files you want to examine and construct a list
fp_list = lfe.get_filepath_list()   
# loop with the list and use the functionalities mentioned above to get the results you want
```
