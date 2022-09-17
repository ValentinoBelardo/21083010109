a=20
b=19
if [ $a -ne $b ]
then
echo "a tidak sama dengan b"
elif [ $a -gt $b ]
then
echo "a lebih besar dari b"
elif [ $a -le $b ]
then
echo "a lebih kecil atau sama dari b"
else
echo "Tidak ada kondisi yang memenuhi"
fi
