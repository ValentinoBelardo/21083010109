a=120
b=20

let jumlah=$a+$b
let kurang=$a-$b
let kali=$a*$b

bagi=`expr $a / $b`

mod=$(($a % $b))

echo "a + b = $jumlah"
echo "a - b = $kurang"
echo "a * b = $kali"
echo "a / b = $bagi"
echo "a % b = $mod"

echo "a = $a"
echo "b = $b"
