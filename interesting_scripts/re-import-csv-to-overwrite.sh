#!/usr/bin/env bash

# Note: old (<=3?) versions of sqlite don't have foreign key constraints without explicitly setting them on.
# if using a later version of sqlite you'll have to add to this script to disable that checking. Otherwise, the
# deletes/adds (I expect) should cause issues.

# obtains all data tables from database
TS=`sqlite3 $1 "SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%';"`

# exports each table to csv
for T in $TS; do
echo "processing ${T}"

sqlite3 $1 <<!
DELETE FROM $T;
.headers on
.mode csv
.import conv/$T.csv $T
!

done
