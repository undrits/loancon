#!usr/bin/env python

from ruloan import rus_loan_lexicon


def test():
    lexicon = rus_loan_lexicon.loan_lexicon()

    for key in lexicon.analyses:
        if key == "абдоминальный":

            print("Data format:")
            print(lexicon.analyses[key])

            for analysis in lexicon.analyses[key].analysis:
                print("Sources:", analysis.sources)
                print("Frequency:", analysis.frequency)
                print("Donor:", analysis.donor)
                print("UPOS:", analysis.upos)
                print("spaCy tag:", analysis.spacy_tag)
                print("Pymystem lemma:", analysis.pymystem_lemma)
                print()

                print("All wordforms:", analysis.wordform)

                print("Individual wordforms:")
                for word in analysis.wordform:
                    print("Wordform:", word.wordform)
                    print("Frequency:", word.frequency)
                    print("UPOS:", word.upos)
                    print("Features:", word.features)
                    print()


if __name__ == "__main__":
    test()
