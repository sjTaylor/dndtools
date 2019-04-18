#!/usr/bin/env bash

# obtains all data tables from database
TS=`sqlite3 $1 "SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%';"`

mkdir dumped

# exports each table to csv
for T in $TS; do

sqlite3 $1 <<!
.mode csv
.output dumped/$T.csv
select * from $T;
!

done
