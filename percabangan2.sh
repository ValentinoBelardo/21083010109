printf "Mobil apa yang kamu suka?\n"
printf "Tesla?\n"
printf "BMW?\n"
printf "Lamboghirni?\n"

read mobil

case "$mobil" in
"Tesla")
echo "Tesla canggih banget"
;;
"BMW")
echo "BMW keren bat"
;;
"Lamboghirni")
echo "Lamboghirni gahar slurrr"
;;
*)
echo "mobil opo iki??"
;;
esac
