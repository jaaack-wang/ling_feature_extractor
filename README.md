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
**Please specify _the directory to StanfordCoreNLP_ in the text_processor.py under LFE folder when first using the program.**
### Dealing with a corpus of files
- Basic Use: to extract frequencies of 95 built-in linguistic features by inputting the corpus directory
```
from LFE.extractor import CorpusLFE
lfe = CorpusLFE('/directory/to/the/corpus/under/analysis/')
lfe.corpus_feature_fre_extraction() 
```
By default, this will result in: (1) a .xlsx file containing the frequency data of all the linguistic features for all the files in the corpus; (2) a newly created folder called `ST_POS_TAGGED` under the corpus folder that contained the tagged corpus by Stanford POS tagger; (3) another new folder called `Extracted_Features` that contains 93 sub-folders named after each linguistic feature (except two mean word length, type-token ratio) where the extracted results for the specific feature are stored separately in .txt files.

**To turn off the tagged corpus and extracted features**: `lfe.corpus_feature_fre_extraction(save_tagged_corpus=False, save_extracted_features=False)`

**To change the normalized rate for the features**: `lfe.corpus_feature_fre_extraction(normalized_rate=XXXX)`. The default rate is 100, meaning each feature, except 2 already normalized features, mean word length and type-token ratio, is all normalized at 100 words level.

**To display contexts for extracted features**: use `lfe.corpus_feature_fre_extraction(left=XX, right=XX)` to specify how many words you'd like to see to the left or right of the target feature. Of course, please do not turn of `save_extracted_features=True` first. 

- Baisc Use: to save cleaned corpus or tagged corpus or extracted features

```
# save cleaned corpus. The corpus will be tokenized, unpunctuated and several paralinguistic information will be removed.
lfe.save_cleaned_corpus
# save tagged corpus
lfe.save_tagged_corpus()
# save extracted features
lfe.save_corpus_extracted_features()
# by default the extracted results will only save the target feature, but it is possible to get the context by specify how many words you'd like to see to the left/right of the target feature
lfe.save_corpus_extracted_features(left=XX, right=XX)
```



## Comparison with MAT
The performance of this extractor has been compared to Nini's(2014) Multidimensional Analysis Tagger (MAT), a similar program that is based solely on Biber(1988) and can be accessed at: https://github.com/andreanini/multidimensionalanalysistagger. The results show that these two programs are generally comparable. There are only 1/3 of the results showing significant differences, the rest being either identical or mostly similar. However, the current program is neater in terms of the code length and in many ways more accurate in the results. The improvements come from three aspects: the adoption of the lastest Stanford POS tagger, instead of the 2013 version used in MAT; bug fixing; and algorithms rewriting. See Algorithms.txt for brief descriptions on the latter two aspects.  

A final package is still yet to be finished. 
