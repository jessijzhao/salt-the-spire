#!/usr/bin/env python3

"""
Author: jessijzhao
Date: November 29, 2020

Decodes or encodes save files for Save the Spire.
"""

import base64
import argparse
from itertools import cycle


def parse_args():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser()

    # whether to decode or encode save file
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--decode", action="store_true", help="decode save file")
    group.add_argument("-e", "--encode", action="store_true", help="encode save file")

    # which files to read from / write to
    parser.add_argument("input", type=argparse.FileType('rb'), help="save file to decode/encode")
    parser.add_argument("output", type=argparse.FileType('wb'), help="file to store decoded/encoded save file")

    return parser.parse_args()


def xor_key(bstring, key=b"key"):
    """
    bstring: bytestring to xor with cyclic key
    key: key phrase (actually just "key")

    Takes the XOR of the input text and the key phrase ("key").
    """
    return bytes(_a ^ _b for _a, _b in zip(bstring, cycle(key)))


def decode(infile, outfile):
    """
    infile: save file to decode
    outfile: file to store decoded save file

    Decodes the infile into human-readable JSON.
    """
    b64_text = infile.read()
    infile.close()

    json_text = xor_key(base64.b64decode(b64_text))
    outfile.write(json_text)
    outfile.close()


def encode(infile, outfile):
    """
    infile: save file to encode
    outfile: file to store encoded save file

    Encodes the infile into Slay the Spire save file format.
    """
    json_text = infile.read()
    infile.close()

    b64_text = base64.b64encode(xor_key(json_text))
    outfile.write(b64_text)
    outfile.close()


def main():

    args = parse_args()

    if args.decode:
        decode(args.input, args.output)
    elif args.encode:
        encode(args.input, args.output)
    else:
        raise RuntimeError


if __name__ == "__main__":
    main()

