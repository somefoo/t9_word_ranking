#! /bin/bash

rm superbook.txt
for book in $1/*
do
  #cat $book | sed 's/[,.;;“”‘’?"!_]//g' | tr [:upper:] [:lower:] >> superbook.txt
  cat $book | sed 's/[,.;;“”‘’?"!_]//g' >> superbook.txt
  #cat $book | sed "s/[^[:alpha:]-]/ /g" >> superbook.txt
  echo $book
done

echo 'Done creating super book'

tr ' ' '\12' < superbook.txt | sort | uniq -c | sort -nr | awk '{print $2 ", " $1 ", 1"}' > result.txt

echo 'Done ranking'


cat result.txt | sed 's/[abcABC]/a/g' | sed 's/[defDEF]/d/g' | sed 's/[ghiGHI]/g/g' | sed 's/[jklJKL]/j/g' | sed 's/[mnoMNO]/m/g' | sed 's/[pqrsPQRS]/p/g' | sed 's/[tuvTUV]/t/g' | sed 's/[wxyzWXYZ]/w/g' > result_t9.txt

echo 'Done creating the T9 version'

cat original_files/t9backup_en.txt | sed 's/[abcABC]/a/g' | sed 's/[defDEF]/d/g' | sed 's/[ghiGHI]/g/g' | sed 's/[jklJKL]/j/g' | sed 's/[mnoMNO]/m/g' | sed 's/[pqrsPQRS]/p/g' | sed 's/[tuvTUV]/t/g' | sed 's/[wxyzWXYZ]/w/g' > original_files/t9backup_en_t9.txt

echo 'Done converting input'
