#!/bin/bash

PERIOD=$2
cp ~/Downloads/Chase4058* ~/Documents/Finance/Spending/chase-$PERIOD.csv
rm ~/Downloads/Chase*
cp ~/Downloads/Transactions* ~/Docuents/Finance/Spending/amex-$PERIOD.csv
