#!/bin/bash

# deklarasikan array [Explicit Declaration] :
declare -a angka

#clear
i=0;
while [ $i -le 5 ];
do
let isi=$i*5;
angka[$i]=$isi;
let i=$i+1;
done

#tampilkan semua elemen array
#dengan indexnya berisi "*" atau "@"
echo ${angka[@]}
