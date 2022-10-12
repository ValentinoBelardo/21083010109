#!/bin/bash

# deklarasi array2dimensi " : " pemisah nilai (array [3][4])
array2dimensi="1.5:1.6:1.7:1.8 2.5:2.6:2.7:2.8 3.5:3.6:3.7:3.8"

# mengakali multi dimensi -> dengan pemisah dimensi "tr :"
function dimensiBaris {
for baris in $array2dimensi
do
dimensiKolom `echo $baris | tr : " "`
done
}

function dimensiKolom {
for kolom in $*
do
echo -n $kolom " "
done
echo
}

# melakukan pemanggilan fungsi
dimensiBaris
