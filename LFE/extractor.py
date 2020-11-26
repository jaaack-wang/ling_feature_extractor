try:
    from LFE import features_set as fs
except ImportError:
    import features_set as fs
try:
    from LFE import text_processor as tp
except ImportError:
    import text_processor as tp
    
import pandas as pd
import os


def show_feature_names():
    return '\n'.join([k for k in fs.FEATURE_DICT.keys()])


def get_feature_regex_by_name(feature_name_):
    return fs.FEATURE_DICT[feature_name_]


def get_feature_name_by_regex(regex, feature_name=None):
    try:
        name = [k for k, v in fs.FEATURE_DICT.items() if v == regex][0]
    except:
        if not feature_name:
            name = 'Unnamed Feature'
        else:
            name = feature_name
    return name


def save_single_tagged_text(file_path):
    filename = file_path.split('/')[-1]
    raw_text = str(open(file_path, 'rb').read())
    tagged_text = tp.get_pos_tagged_text(raw_text)
    tp.save_processed_text(file_path, 'ST_' + filename, 'ST_POS_TAGGED', tagged_text)
    print(filename + ' tagged')


def save_single_cleaned_text(file_path):
    filename = file_path.split('/')[-1]
    raw_text = str(open(file_path, 'rb').read())
    cleaned_text = tp.text_cleaning(raw_text)
    tp.save_processed_text(file_path, filename, 'CLEANED', cleaned_text)
    print(filename + ' cleaned')


def display_extracted_feature_by_name(file_path, feature_name, left=0, right=0):
    raw_text = str(open(file_path, 'rb').read())
    tagged_text = tp.get_modified_pos_tagged_text(raw_text)
    pattern = get_feature_regex_by_name(feature_name)
    return fs.display_extracted_res_by_regex(pattern, tagged_text, left, right, feature_name)


def display_extracted_feature_by_regex(file_path, regex, left=0, right=0, feature_name=None):
    raw_text = str(open(file_path, 'rb').read())
    tagged_text = tp.get_modified_pos_tagged_text(raw_text)
    if '(' not in regex and ')' not in regex:
        regex = '(' + regex + ')'
    feature_name = get_feature_name_by_regex(regex, feature_name)
    return fs.display_extracted_res_by_regex(regex, tagged_text, left, right, feature_name)


def save_extracted_feature_by_name(file_path, feature_name, left=0, right=0):
    result = display_extracted_feature_by_name(file_path, feature_name, left, right)
    filename = file_path.split('/')[-1]
    root = file_path.replace(filename, '')
    new_root = root + 'Extracted_Features/'
    if not os.path.exists(new_root):
        os.mkdir(new_root)

    new_path = new_root + 'none'
    tp.save_processed_text(new_path, filename, f'{feature_name}', result)
    print(f'{feature_name} extracted and saved in {new_root}')


def save_extracted_feature_by_regex(file_path, regex, left=0, right=0, feature_name=None):
    result = display_extracted_feature_by_regex(file_path, regex, left, right, feature_name)
    feature_name = get_feature_name_by_regex(regex, feature_name)
    filename = file_path.split('/')[-1]
    root = file_path.replace(filename, '')
    new_root = root + 'Extracted_Features/'
    if not os.path.exists(new_root):
        os.mkdir(new_root)

    new_path = new_root + 'none'
    tp.save_processed_text(new_path, filename, f'{feature_name}', result)
    print(f'"{feature_name}" extracted and saved in {new_root}')


def save_extracted_feature_by_res(file_path, results, feature_name, pos_tagged_text=None, left=0, right=0):
    filename = file_path.split('/')[-1]
    result = fs.display_extracted_res(results, pos_tagged_text, left, right, feature_name=feature_name)
    root = file_path.replace(filename, '')
    new_root = root + 'Extracted_Features/'
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    new_path = new_root + 'none'
    tp.save_processed_text(new_path, filename, f'{feature_name}', result)


def get_single_file_feature_fre(file_path, normalized_rate=100, save_tagged_file=True,
                                save_extracted_features=True, left=0, right=0):
    sub_data = []

    raw_text = str(open(file_path, 'rb').read())
    filename = file_path.split('/')[-1]
    tagged_text = tp.get_modified_pos_tagged_text(raw_text)

    if save_tagged_file:
        save_single_tagged_text(file_path)

    num_words = fs.word_count(tagged_text)
    num_chars = fs.total_char(tagged_text)
    num_types = len(set(tp.get_texts_lemmas(raw_text)))

    # start calculating feature frequency

    mean_word_len = num_chars / num_words
    type_token_ratio = num_types / num_words
    sub_data.extend([mean_word_len, type_token_ratio])

    other_feature_patterns = [v for v in fs.FEATURE_DICT.values()]
    for pattern in other_feature_patterns:
        results = fs.feature_finder(pattern, tagged_text)
        fre = len(results)
        sub_data.append(fre / num_words * normalized_rate)
        if save_extracted_features:
            feature_name = get_feature_name_by_regex(pattern)
            save_extracted_feature_by_res(file_path, results, feature_name, tagged_text, left, right)

    sub_data = [filename, num_words] + [float("%.2f" % sd) for sd in sub_data]
    print(filename)
    return sub_data


class CorpusLFE:

    def __init__(self, file_dir):
        self._file_dir = file_dir

    def get_filepath_list(self):
        filenames = tp.get_filenames_from_dir(self._file_dir)
        path_list = []
        for filename in filenames:
            path_list.append(self._file_dir + filename)
        return '\n'.join(path_list)

    def save_tagged_corpus(self):
        filenames = tp.get_filenames_from_dir(self._file_dir)
        for filename in filenames:
            save_single_tagged_text(self._file_dir + filename)
        print('Tagged corpus saved!')

    def save_cleaned_corpus(self):
        filenames = tp.get_filenames_from_dir(self._file_dir)
        for filename in filenames:
            save_single_cleaned_text(self._file_dir + filename)
        print('Cleaned corpus saved!')

    def corpus_feature_fre_extraction(self, normalized_rate=100, save_tagged_corpus=True,
                                      save_extracted_features=True, left=0, right=0):
        freq_data = [['Filename', 'Words', 'Mean word length', 'Type-token ratio']]
        feature_names = [k for k in fs.FEATURE_DICT.keys()]
        freq_data[0].extend(feature_names)
        filenames = tp.get_filenames_from_dir(self._file_dir)
        for filename in filenames:
            sub_data = get_single_file_feature_fre(self._file_dir + filename, normalized_rate, save_tagged_corpus,
                                                   save_extracted_features, left, right)
            freq_data.append(sub_data)
        pd.DataFrame(freq_data).to_excel('Feature_Fre_Extracted.xlsx')
        return freq_data

    def save_corpus_extracted_features(self, left=0, right=0):
        other_feature_patterns = [v for v in fs.FEATURE_DICT.values()]
        filenames = tp.get_filenames_from_dir(self._file_dir)
        for filename in filenames:
            raw_text = str(open(self._file_dir + filename, 'rb').read())
            tagged_text = tp.get_modified_pos_tagged_text(raw_text)
            for pattern in other_feature_patterns:
                results = fs.feature_finder(pattern, tagged_text)
                feature_name = get_feature_name_by_regex(pattern)
                file_p = self._file_dir + filename
                save_extracted_feature_by_res(file_p, results, feature_name, tagged_text, left, right)
        print('The extracted features of the corpus saved!')

    def save_corpus_one_extracted_feature_by_name(self, feature_name):
        filenames = tp.get_filenames_from_dir(self._file_dir)
        for filename in filenames:
            save_extracted_feature_by_name(self._file_dir + filename, feature_name)

    def save_corpus_one_extracted_feature_by_regex(self, regex, left=0, right=0, feature_name=None):
        filenames = tp.get_filenames_from_dir(self._file_dir)
        for filename in filenames:
            save_extracted_feature_by_regex(self._file_dir + filename, regex, left, right, feature_name)

