#!/bin/bash

# deklarasi fungsi
nama(){
echo "kamu siapa?"
read nama
}
id(){
echo "sebut id kamu"
read id
echo -e "halo $nama dengan id $id, selamat datang!!"
}

# memanggil fungsi
nama
id
