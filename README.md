# Salt the Spire

Decodes and encodes save files of [Slay the Spire](https://store.steampowered.com/app/646570/Slay_the_Spire/), a fun deck-building roguelike made by [Mega Crit](https://www.megacrit.com/). This was conceived after a *Who Needs Relics?* achievement run was rudely interrupted by *Mark of the Bloom*.

Save files are the XOR of base 64 encoded JSON strings and a "key" phrase.


## Contents

- [salt_the_spire.py](salt_the_spire.py) decodes and encodes files

- [tests/test_salting.py](tests/test_salting.py) tests the encoding and decoding functions

- [tests/decoded.txt](tests/decoded.txt) contains an example JSON object

- [tests/encoded.txt](tests/encoded.txt) contains the corresponding encoded JSON object


## Usage

```
usage: salt_the_spire.py [-h] (-d | -e) input output

positional arguments:
  input         save file to decode/encode
  output        file to store decoded/encoded save file

optional arguments:
  -h, --help    show this help message and exit
  -d, --decode  decode save file
  -e, --encode  encode save file
```


## Tests

`python -m pytest tests/`

Requires Python 3.
