from ruloan import ruloan_pb2
import gzip
import os
from pathlib import Path

DIR = Path(__file__).resolve().parent
DATA_PATH = os.path.join(DIR, 'data', 'loan_lexicon.pb.gz')


def loan_lexicon(path: str = DATA_PATH):
    """Returns the loanword lexicon"""
    lexicon = ruloan_pb2.Lexicon()
    with gzip.open(path, "rb") as byte_file:
        lexicon.ParseFromString(byte_file.read())
    return lexicon
