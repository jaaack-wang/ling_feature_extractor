# ling_feature_extractor
## Description
```
A linguistic feature extraction program that has 95 general lexico-grammatical features built in. It is built to be corpus-linguistic tool to study langauge and gender macroscopically, but since all the built-in features are very general, it is possible to use it jsut a general tool to study textual variation of spoken or written texts. Besides, the program is also part of my thesis project. The thesis version contains three more built-in linguistic features, which are deleted in the main version because those features are not deemed as generally accessible in a normal corpus.
```  

`As for the linguistic features`: Over 2/3 of them come from Biber et al.(2006) with 42 features also present in Biber(1988). These features are generally known as part of the Multi-Dimensional analysis framework.

`As for the program`: the program can be very useful as a search engine to match desired pattern in a corpus. All it takes is a corpus and corresponding pattern of the deisred feature written in Regular Expression. 

## Prerequisites
The program is written in pure Python language, the release of which should be over 3.6 to make the program properly because of some Python packages it uses. However, Java 1.8+ is also required since StanfordCoreNLP is employed, which is written in pure Java. To use the functionalities of StanfordCoreNLP, a Python Wrapper called stanfordcorenlp is used here.

- `Computer Langauges`: 
-- Python 3.6+: check with cmd: `python --version` or `python3 --version` ([Download Page](https://www.python.org/downloads/)); 
-- Java 1.8+: check with cmd: 'java --version' ([Download Page](https://www.java.com/en/download/)). 
- `Python packages`
| Package | Description | Pip download | 
| :---: | :---: | :---: |
| [stanfordcorenlp](https://github.com/Lynten/stanford-corenlp) | A Python wrapper for StanforeCoreNLP | 'pip/pip3 install stanfordcorenlp' |
| pandas | Used for storing extracted feature frequencies  | 'pip/pip3 install pandas' |

Besides, built-in packages are heavily employed in the program, especially the built-in `re` package for Regular Expression.




The performance of this extractor has been compared to Nini's(2014) Multidimensional Analysis Tagger (MAT), a similar program that is based solely on Biber(1988) and can be accessed at: https://github.com/andreanini/multidimensionalanalysistagger. The results show that these two programs are generally comparable. There are only 1/3 of the results showing significant differences, the rest being either identical or mostly similar. However, the current program is neater in terms of the code length and in many ways more accurate in the results. The improvements come from three aspects: the adoption of the lastest Stanford POS tagger, instead of the 2013 version used in MAT; bug fixing; and algorithms rewriting. See Algorithms.txt for brief descriptions on the latter two aspects.  

A final package is still yet to be finished. 
