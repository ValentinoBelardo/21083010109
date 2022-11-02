#!/bin/bash

# deklarasi fungsi
function nama {
	echo "kamu siapa?"
	read nama
}
function id {
	echo "sebut id kamu"
	read id
	echo -e "halo $nama dengan id $id, selamat datang!!"
}

# memanggil fungsi
nama
id


