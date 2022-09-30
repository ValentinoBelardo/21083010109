#!/bin/bash

select makanan in onigiri pasta pizza ada semua
do
  case $makanan in
    onigiri|pasta|pizza|semua)
      echo "Maaf, ada"
      ;;
    gorengan)
      echo "habis"
      ;;
      gaada)
        break
      ;;
      *) echo "tidak tersedia"
      ;;
    esac
  done
