#!/bin/bash
cd ./data/physionet.org/files/tpehgdb/1.0.1/tpehgdb/
FILES=./*[^m].hea

# For all record files run conversion to Matlab compatible file
for f in $FILES
do
  f=$(basename $f)
  f=${f%.*}
  echo $f
  wfdb2mat -r $f
done