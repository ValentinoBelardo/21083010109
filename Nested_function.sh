#!/bin/bash

# Mendeklarasikan fungsi
nama() {
echo "kamu siapa?"
read nama
id # <------ Memanggil fungsi di dalam fungsi (fungsi bersarang)
}
id() {
echo "Sebutkan id mu"
read id
echo -e "Hai $nama dengan id $id, selamat datang!!"
}

# Memanggil fungsi
nama
