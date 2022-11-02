#!/bin/bash

# Mendeklarasikan fungsi
panjang() {
echo "Masukkan Panjang : "
read panjang
printf "\n"
}
lebar() {
echo "Masukkan Lebar :"
read lebar
printf "\n"
}
luas() {
echo "Luas Persegi : "
let luas=$panjang*$lebar
echo $luas
}

panjang
lebar
luas
