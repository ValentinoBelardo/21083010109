from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

x = int(input("Masukan nilai = "))

def cetak(i):
	if(i+1)%2== 0:
	 print(i+1, "Genap",  "-punya ID proses", getpid())

	else:
	 print(i+1, "Ganjil", "-punya ID proses", getpid())
	sleep(1)

print("\n")
print("Sekuensial")
sekuensial_awal = time()
for i in range(x):
    cetak(i)
sekuensial_akhir = time()


print("\n")
print("multiprocessing.Process")
kumpulan_proses = []
process_awal = time()
for i in range(x):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()
for i in kumpulan_proses:
    p.join()
process_akhir = time()


print("\n")
print("multiprocessing.Pool")
pool_awal = time()
pool = Pool()
pool.map(cetak, range(0,x))
pool.close()
pool_akhir = time()


print("\n")
print("Sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Kelas Process :", process_akhir - process_awal, "detik")
print("Kelas Pool :", pool_akhir - pool_awal, "detik")
