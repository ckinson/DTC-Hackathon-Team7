#!/bin/bash
FILE=$1
while read LINE; do
  echo "sending $LINE"
  aws kinesis put-record --stream-name "dxc-7" --data "$LINE" --partition-key "test"
  sleep .5s
done < $FILE
