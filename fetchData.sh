#!/bin/sh

mkdir -p data

wget https://github.com/archiveofblades/dnddata/blob/master/data-raw/dnd_chars_all.tsv?raw=true -O data/dnd_chars_all.tsv
