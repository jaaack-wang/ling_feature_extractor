# ling_feature_extractor
A python program I built for my thesis project to extract 98 linguistic features. Over 2/3 of them come from Biber et al.(2006) with 42 features also present in Biber(1988). These features are generally known as part of the Multi-Dimensional analysis framework.

The performance of this extractor has been compared to Nini's(2014) Multidimensional Analysis Tagger (MAT), a similar program that is based solely on Biber(1988) and can be accessed at: https://github.com/andreanini/multidimensionalanalysistagger. The results show that these two programs are generally comparable. There are only 1/3 of the results showing significant differences, the rest being either identical or mostly similar. However, the current program is neater in terms of the code length and in many ways more accurate in the results. The improvements come from three aspects: the adoption of the lastest Stanford POS tagger, instead of the 2013 version used in MAT; bug fixing; and algorithms rewriting. See Algorithms.txt for brief descriptions on the latter two aspects.  

A final package is still yet to be finished. 
