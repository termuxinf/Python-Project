class Ruangan:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        self.luas = panjang * lebar

bangunan = [
    Ruangan(3, 4),
    Ruangan(4, 3),
    Ruangan(4, 3),
    Ruangan(8, 5),
    Ruangan(3, 4),
    Ruangan(4, 3),
    Ruangan(4, 4),
    Ruangan(4, 4),
    Ruangan(4, 4),
]

luas = 0
for ruangan in bangunan:
    luas += ruangan.luas

print(luas)
