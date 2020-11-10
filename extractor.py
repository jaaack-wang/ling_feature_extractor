import features_set as fs
import text_processor as tp
import pandas as pd
from time import time

fre_data = [['Filename', 'Words per utterance', 'Utterance', 'Mean word length', 'Type-token ratio', 'Overlap']]
other_feature_names = [k for k in fs.FEATURE_DICT.keys()]
fre_data[0].extend(other_feature_names)


def feature_fre_extraction(raw_text, filename):
    sub_data = []

    num_utterances = fs.num_utterances(raw_text)
    num_overlaps = fs.num_overlaps(raw_text)
    tagged_text = tp.get_modified_pos_tagged_text(raw_text)
    num_words = fs.word_count(tagged_text)
    num_chars = fs.total_char(tagged_text)
    num_types = len(set(tp.get_texts_lemmas(raw_text)))

    # start calculating feature frequency
    words_per_utter = num_words / num_utterances
    utter = num_utterances / num_words * 100
    mean_word_len = num_chars / num_words
    type_token_ratio = num_types / num_words
    overlaps = num_overlaps / num_words * 100
    sub_data.extend([words_per_utter, utter, mean_word_len, type_token_ratio, overlaps])

    other_feature_patterns = [v for v in fs.FEATURE_DICT.values()]
    for pattern in other_feature_patterns:
        fre = fs.get_feature_frequency(pattern, tagged_text)
        sub_data.append(fre / num_words * 100)

    sub_data = [filename] + [float("%.2f" % sd) for sd in sub_data]
    fre_data.append(sub_data)
    print(filename)
    return fre_data


def main():
    file_dir = '/Users/wzx/Downloads/corpus/'
    filenames = tp.get_filenames_from_dir(file_dir)
    threads = []
    for filename in filenames[:2]:
        raw_text = open(file_dir + filename, 'r').read()
        feature_fre_extraction(raw_text, filename)

    pd.DataFrame(fre_data).to_excel('Feature_Fre_Extracted.xlsx')


if __name__ == '__main__':
    s = time()
    main()
    e = time()
    print(f"Total time taken: {e-s}")



