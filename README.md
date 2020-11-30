# Salt the Spire

Decodes and encodes save files of [Slay the Spire](https://store.steampowered.com/app/646570/Slay_the_Spire/), a fun deck-building roguelike made by [Mega Crit](https://www.megacrit.com/). This was conceived after a *Who Needs Relics?* achievement run was rudely interrupted by *Mark of the Bloom*.

Save files are the XOR of base 64 encoded JSON strings and a "key" phrase.

Uses Python 3.

```
usage: salt_the_spire.py [-h] (-d | -e) input output
```
