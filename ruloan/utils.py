import json
from typing import Dict, List, Union, Optional

import ruloan_pb2


def _build_entry(
    lexicon: ruloan_pb2.Lexicon,
    lemma: str,
    data: Dict[str, Union[int, str, List, Dict]]
) -> object:

    """Internal function for building the protobuf lexicon entry"""

    # start entry
    entry = lexicon.analyses[lemma].analysis.add()

    # add sources
    entry.sources = ", ".join(data['sources'])

    # add lemma features
    entry.frequency = data['freq_count']
    entry.upos = data['upos']
    entry.donor = data['donor']
    entry.spacy_tag = data['spacy_tag']
    entry.pymystem_lemma = data['pymystem_lemma']

    # add wordforms
    for wordform, wordform_data in data['wordforms'].items():
        word = entry.wordform.add()
        word.wordform = wordform
        word.frequency = wordform_data['freq_count']
        word.upos = wordform_data['upos']
        features = word.features
        features.animacy = wordform_data['feats']['animacy']
        features.case = wordform_data['feats']['case']
        features.gender = wordform_data['feats']['gender']
        features.number = wordform_data['feats']['number']
        features.aspect = wordform_data['feats']['aspect']
        features.mood = wordform_data['feats']['mood']
        features.tense = wordform_data['feats']['tense']
        features.verbform = wordform_data['feats']['verbform']
        features.voice = wordform_data['feats']['voice']
        features.degree = wordform_data['feats']['degree']
        features.variant = wordform_data['feats']['variant']
        features.person = wordform_data['feats']['person']

    return lexicon


def compile(
    filepath: str,
    lexicon: Optional[object] = None,
) -> object:

    """Compile a lemma and wordform lexicon out of Apertium data"""

    if not lexicon:
        lexicon = ruloan_pb2.Lexicon()
    data = json.load(open(filepath))
    counter = 0
    for lemma, lemma_data in data.items():
        if not isinstance(lemma_data['donor'], str):
            continue
        lexicon = _build_entry(
            lexicon,
            lemma,
            lemma_data
        )
        counter += 1

    print(f"added {counter} loan lemmas!")

    return lexicon
