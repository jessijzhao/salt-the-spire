#!/usr/bin/env python3

"""
Author: jessijzhao
Date: November 29, 2020

Decodes or encodes save files for Slay the Spire.
"""

import base64
import argparse
from itertools import cycle


def xor_key(bstring, key=b'key'):
    """
    bstring: bytestring to xor with cyclic key
    key: key phrase (actually just "key")

    Takes the XOR of the input text and the key phrase ("key").
    """
    return bytes(_a ^ _b for _a, _b in zip(bstring, cycle(key)))


def decode(inbytes):
    """
    inbytes: bytes to decode

    Returns decoded bytes representing a human-readable JSON.
    """
    return xor_key(base64.b64decode(inbytes))


def encode(inbytes):
    """
    inbytes: bytes to encode

    Returns encoded bytes in Slay the Spire save file format.
    """
    return base64.b64encode(xor_key(inbytes))


def main():

    parser = argparse.ArgumentParser()

    # whether to decode or encode save file
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--decode', action='store_true', help='decode save file')
    group.add_argument('-e', '--encode', action='store_true', help='encode save file')

    # which files to read from / write to
    parser.add_argument('input', type=argparse.FileType('rb'), help='save file to decode/encode')
    parser.add_argument('output', type=argparse.FileType('wb'), help='file to store decoded/encoded save file')

    args = parser.parse_args()

    inbytes = args.input.read()
    args.input.close()

    if args.decode:
        outbytes = decode(inbytes)
    elif args.encode:
        outbytes = encode(inbytes)
    else:
        raise RuntimeError

    args.output.write(outbytes)
    args.output.close()


if __name__ == '__main__':
    main()

