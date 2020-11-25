from stanfordcorenlp import StanfordCoreNLP
import re
import json
import os
from os import listdir
from os.path import isfile, join

# loading Stanford tagger
# please specify the path to StanfordCoreNLP when first using the program
nlp = StanfordCoreNLP("/path/to/StanfordCoreNLP/")
# setting the properties for the nlp annotator
props = {'annotators': 'tokenize,ssplit,pos,lemma', 'tokenize.whitespace': 'true', 'outputFormat': 'json'}
# spelling standardization patten


def get_filenames_from_dir(file_dir):
    file_names = [f for f in listdir(file_dir) if isfile(join(file_dir, f)) if f != '.DS_Store']
    file_names.sort()
    return file_names


def americanize(raw_text):
    with open('uk_us_en_dict.json', 'r') as f:
        uk_us_en_dict = json.load(f)

    for uk, us in uk_us_en_dict.items():
        if uk in raw_text.lower():
            raw_text = re.sub(rf"\b{uk}\b", us, raw_text, flags=re.IGNORECASE)
    return raw_text


def text_cleaning(raw_text):

    text = " " + raw_text + " "
    filler = r"(?<= )(hm'?|huh|mm|mhm|uh|um|uhuh|yuhuh|h?uh'uh|'m'm|uh'oh" \
             r"|ach|ah|ahah|gee|jeez|oh|ooh|oops?|tch|ugh|whoa|yay)(?= )"

    # patterns for cleaning the raw texts: targeted patterns + replaced patterns
    cleaner = {
        # targeted pattern: replaced pattern

        # remove all the truncations, tags
        r"(<trunc>[^>]+>|<[^>]+>|\(?\S+-\)? |[^-'\s\w])": "",
        # delete non-lexical sounds (e.g., filled pauses, interjections)
        rf"{filler}": "",
        # remove non-language symbols except ['-] when used as part of the word
        r"(?<= )\W+(?= )": "",

        # split basic contractions as the whitespace is turned on for tokenizing
        r"(\S+)(n't )": r"\1 \2",
        # r"(\S+)('[^t\s]\S? )": r"\1 \2",
        r"(\S+)('(m|re|s|d|ll|ve) )": r"\1 \2",
        r"(\S+s)(' )": r"\1 \2",
        r"(y')(\S+)": r"\1 \2",

        # standardize the writing so that stanford tagger can achieve better performance or understand
        # pronoun
        r"\bi\b": "I",
        r"\bgimme\b": "give me",
        r"\bbetcha\b": "bet you",
        r"\bya\b": "you",

        # of
        r"\b(kind|lots|sort)(a)\b": r"\1 of",
        r"\blotta\b": "lot of",

        # to
        r"\bgotta\b": "got to",
        r"\bhafta\b": "have to",
        r"\boughta\b": "ought to",
        r"\bgonna\b": "going to",
        r"\bwanna\b": "want to",

        # other contractions
        rf"(?<= )('cause|cuz|coz)\b": "because",
        r"(could|would|should)(a)": r"\1 've",
        r"(could|would|should)(na)": r"\1 n't 've",
        r"(\S+)n'ta": r"\1 n't 've",
        r"\bcannot\b": r"can not",
        r"\bmkay\b": r"okay"
    }

    for target, replace in cleaner.items():
        text = re.sub(target, replace, text, flags=re.IGNORECASE)

    # americanized spellings
    text = americanize(text)

    # stripping extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def text_annotating(raw_text):
    cleaned_text = text_cleaning(raw_text)
    # change the global props value above to allow more annotations, such as ner, depparse
    annotated_text = nlp.annotate(cleaned_text, properties=props)
    return annotated_text


def get_pos_tagged_text(raw_text):
    annotated_text = text_annotating(raw_text)
    annotated_text = json.loads(annotated_text)
    tagged_words = []
    for s in annotated_text['sentences']:
        for token in s['tokens']:
            tagged_words.append(
                token['originalText'] + "_" + token['pos']
            )
    return ' '.join(tagged_words)


def get_modified_pos_tagged_text(raw_text):
    tagged_text = get_pos_tagged_text(raw_text)
    text_mod = re.sub(r"(?<=\b(not|n't))_\S+", "_NEG", tagged_text, flags=re.IGNORECASE)
    return text_mod


def get_texts_lemmas(raw_text):
    annotated_text = text_annotating(raw_text)
    annotated_text = json.loads(annotated_text)
    lemmas = []
    for s in annotated_text['sentences']:
        for token in s['tokens']:
            lemmas.append(token['lemma'])
    return [lemma for lemma in lemmas]


def get_num_unique_lemmas(raw_text):
    lemmas = get_texts_lemmas(raw_text)
    return len(set(lemmas))


def save_processed_text(file_path, new_filename, new_dir_name, processed_text):
    filename = file_path.split('/')[-1]
    root = file_path.replace(filename, '')
    output_root = root + new_dir_name + "/"
    if not os.path.exists(output_root):
        os.mkdir(output_root)
    filepath = output_root + new_filename
    with open(filepath, 'w') as f:
        f.write(processed_text)
        f.close()
        print(f"{new_filename} saved in {filepath}")
