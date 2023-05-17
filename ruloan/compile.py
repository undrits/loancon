#! usr/bin/env python

""" Build RuLoan lexicon out """

import argparse
from google.protobuf import text_format
import ruloan_pb2
from utils import compile
import time


def read_lexicon(path: str) -> ruloan_pb2.Lexicon:
    lexicon = ruloan_pb2.Lexicon()
    f = open(path, "rb")
    lexicon.ParseFromString(f.read())
    f.close()
    return lexicon


def main(args: argparse.Namespace) -> None:

    # create lexicon
    lexicon = ruloan_pb2.Lexicon()

    # add data
    lexicon = compile(args.datapath, lexicon)

    # save to disk
    if args.lexicon_path:
        output = open(args.lexicon_path, "wb")
    else:
        output = open("lexicon.pb", "wb")
    output.write(lexicon.SerializeToString())
    output.close()

    # save in a human readable format
    if args.lexicon_readable_path:
        output_h = open(args.lexicon_readable_path, "w")
    else:
        output_h = open("lexicon.textproto", "w")
    output_h.write(text_format.MessageToString(lexicon, as_utf8=True))
    output_h.close()

    print("Done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--datapath",
        required=True,
        help="path to data (json)",
    )
    parser.add_argument(
        "--lexicon_path",
        required=False,
        help="path for the binary lexicon output",
    )
    parser.add_argument(
        "--lexicon_readable_path",
        required=False,
        help="path for the human readable lexicon output",
    )

    main(parser.parse_args())
    print("Time:", time.process_time())
