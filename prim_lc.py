#Codingan Algo Prim
INF = 9999999  #definisi bilangan tertinggi
N = int(input("Masukkan jumlah vertex: ")) #input jumlah vertex

# Matriks Tetangga
# 0 112 0 169 29 340 202 258
# 112 0 0 81 0 0 11 0
# 0 0 0 0	588 598	0 495
# 169 81 0 0 0 0 150 0
# 29 0 588 0 0 339 0 199
# 340 0 598 0 339 0 0 0
# 202 11 0 150 0 0 0 0
# 258 0 495 0 199 0 0 0

G = []      # Untuk nampung matriks ketetanggaan

for _ in range(N):   # input matriks ketetanggaan
    x = [int(x) for x in input().split()]
    G.append(x)
print(*G,'\n',sep='\n')    # tampilkan matriks ketetanggan

seen = []        # buat array baru untuk vertex yg udah dikunjungi
for _ in range(N):
    seen.append(0)

seen[0] = True  # set vertex pertama udah dikunjungi
mst = 0 # buat variabel nampung mst

# printing for edge and weight
print("Edge : Weight\n")

for _ in range(N-1):
    minimum = INF   # set nilai min untuk dibandingkan sama bobot
    min_a = 0       # buat nampung indeks minimum
    min_b = 0
    for m in range(N):    # looping yang intinya kl dah dikunjungi, dicek yang
        if seen[m]:       # berhubungan, lalu cari yang paling kecil, di tiap vertex
            for n in range(N):
                if ((not seen[n]) and G[m][n]):  
                    # kl pasangannya belum dilihat, dan tentunya ada edge (kl dah terlihat berarti cycle)
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        min_a = m
                        min_b = n
    print(str(min_a) + " --> " + str(min_b) + " : " + str(G[min_a][min_b]))
    mst = mst + G[min_a][min_b] # jumlahkan ke mst
    seen[min_b] = True   # set udah dikunjungin

print(f'MST: {mst}') # cetak mst akhir
    
