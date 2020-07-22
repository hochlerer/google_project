from data_interface import *
from auxiliary_functions import *
from auto_complete_data import AutoCompleteData
# hide data

def complete(prefix):
    prefix_ignore_del = ignore_delimiters(prefix)
    results = [word for word in get_sentIndex(prefix_ignore_del)]
    best_completions = []

    for i in range(len(results)):
        best_completions.append(AutoCompleteData(get_sentence(results[i]), get_sentence_src(results[i]), offset(results[i], prefix), len(prefix) * 2))

    fit_sents = fix_word(prefix_ignore_del, results)
    for sent in fit_sents:
        best_completions.append(AutoCompleteData(get_sentence(sent["sentence_index"]), get_sentence_src(sent["src"]), sent["offset"], sent["score"]))

    return best_completions
