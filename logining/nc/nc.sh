#!/bin/bash

for i in `seq 101 200`
do
j="172.20.$i.101"
echo "Attack 8080 $j..."
./nc.py -H $j
done
