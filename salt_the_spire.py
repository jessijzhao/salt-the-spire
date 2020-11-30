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
    parser.add_argument("input", type=argparse.FileType('r'), help="save file to decode/encode")
    parser.add_argument("output", type=argparse.FileType('w'), help="file to store decoded/encoded save file")

    return parser.parse_args()


def xor_key(text, key=b"key"):
    """
    text: string to xor with cyclic key
    key: key phrase (actually just "key")

    Takes the XOR of the input text and the key phrase ("key").
    """
    return bytes([_a ^ _b for _a, _b in zip(text, cycle(key))])


def decode(infile, outfile):
    """
    infile: save file to decode
    outfile: file to store decoded save file

    Decodes the infile into human-readable JSON.
    """

    text = infile.read()
    infile.close()

    btext = base64.b64decode(text)
    json = xor_key(btext).decode("utf-8")

    outfile.write(json)


def encode(infile, outfile):
    """
    infile: save file to encode
    outfile: file to store encoded save file

    Encodes the infile into Slay the Spire save file format.
    """
    json = infile.read()
    json = bytes(json, "utf-8")

    text = base64.b64encode(xor_key(json))

    encoded_str = str(text, "utf-8")
    outfile.write(str(encoded_str))
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

