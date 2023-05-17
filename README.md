# RuLoan

A database of Russian loanwords from English with morphological features and predicted English donor words. See more in ["Detection and Morphological Analysis of Novel Russian Loanwords" by Yulia Spektor (2021)](https://academicworks.cuny.edu/gc_etds/4572/)

## installation

To install, clone the repo and run:

```shell
pip install -e .
```

After that, the data can be imported as follows:
```python
from ruloan import rus_loan_lexicon

loan_lexicon = rus_loan_lexicon.loan_lexicon()
```

## data 

The ProtoBuf structure of the data is described in the ```ruloan.proto``` file.

The data can be explored as follows:

```python
from google.protobuf import text_format

for key in loan_lexicon.analyses:
	if key == "абдоминальный":

            print("Data format:")
            print(loan_lexicon.analyses[key])

            for analysis in loan_lexicon.analyses[key].analysis:
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
```


The ```.textproto``` file contains the data in a human readable format

## license

The codebase is distributed under the GNU General Public License v3 (GPLv3). Please see ```License.txt``` for details.

