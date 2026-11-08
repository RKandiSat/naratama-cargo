# -*- coding: utf-8 -*-
"""Peta kepulauan Indonesia yang digambar sendiri -- bukan gambar stok.

   Bentuk pulaunya SENGAJA disederhanakan. Sebuah peta skematis yang jelas
   terlihat skematis itu jujur; peta yang berpura-pura akurat lalu meleset
   justru merusak kepercayaan. Yang harus benar di sini hanya satu: posisi
   relatif kotanya, sebab di situlah rute digambar.

   Titik kota dihitung dari bujur-lintang sungguhan, bukan ditaruh dengan
   perkiraan mata.
"""

def xy(lon, lat):
    x = 40 + (lon - 94.0) * (920.0 / 47.0)
    y = 40 + (6.0 - lat) * (340.0 / 17.0)
    return round(x, 1), round(y, 1)

KOTA = {
    'Banda Aceh': (95.3, 5.55), 'Medan': (98.67, 3.59), 'Pekanbaru': (101.45, 0.51),
    'Padang': (100.37, -0.95), 'Palembang': (104.76, -2.98), 'Bandar Lampung': (105.27, -5.43),
    'Jakarta': (106.85, -6.21), 'Bandung': (107.62, -6.92), 'Semarang': (110.42, -6.97),
    'Surabaya': (112.75, -7.26), 'Banyuwangi': (114.37, -8.22), 'Denpasar': (115.22, -8.67),
    'Mataram': (116.12, -8.58), 'Labuan Bajo': (119.88, -8.49), 'Kupang': (123.59, -10.18),
    'Pontianak': (109.33, -0.03), 'Banjarmasin': (114.59, -3.32), 'Balikpapan': (116.83, -1.27),
    'Makassar': (119.43, -5.15), 'Kendari': (122.51, -3.99), 'Manado': (124.84, 1.49),
    'Ambon': (128.19, -3.69), 'Sorong': (131.26, -0.88), 'Jayapura': (140.70, -2.53),
    'Ternate': (127.38, 0.79),
}

# Garis pulau: poligon sederhana, digambar mengikuti bentuk kasar tiap pulau.
PULAU = {
 # Bentuk disederhanakan, tapi cirinya dipertahankan supaya tetap dikenali
 # sebagai Indonesia: Sumatra memanjang serong, Jawa tipis melintang,
 # Kalimantan bersudut di barat daya dengan teluk di timur, Sulawesi
 # berbentuk K, dan Papua dengan Kepala Burung di sebelah barat.
 'sumatra':
  'M 58 42 L 76 40 L 92 54 L 112 72 L 132 90 L 152 110 L 168 130 L 182 146 '
  'L 198 160 L 216 178 L 236 198 L 256 218 L 268 234 L 262 246 L 248 240 '
  'L 228 222 L 208 204 L 190 190 L 172 174 L 154 156 L 134 136 L 114 114 '
  'L 94 92 L 76 70 L 62 54 Z',
 'jawa':
  'M 274 286 L 296 280 L 320 277 L 346 280 L 372 286 L 396 293 L 418 300 '
  'L 438 309 L 444 318 L 430 322 L 408 316 L 384 309 L 358 302 L 332 297 '
  'L 306 295 L 282 298 L 272 294 Z',
 'kalimantan':
  'M 312 168 L 322 142 L 342 124 L 370 114 L 402 110 L 434 116 L 460 130 '
  'L 480 150 L 492 174 L 486 192 L 468 186 L 456 198 L 462 218 L 452 236 '
  'L 430 246 L 404 242 L 378 230 L 356 214 L 338 196 L 322 182 Z',
 'sulawesi':
  'M 528 126 L 546 116 L 558 130 L 552 158 L 560 180 L 582 174 L 606 162 '
  'L 624 170 L 628 182 L 610 192 L 588 200 L 566 204 L 556 220 L 564 246 '
  'L 556 270 L 538 274 L 528 254 L 534 228 L 522 208 L 506 194 L 512 170 Z',
 'papua':
  # Kepala Burung, leher, lalu badan utama yang melebar ke timur
  'M 748 190 L 764 174 L 786 170 L 800 182 L 794 198 L 806 204 L 828 196 '
  'L 856 190 L 888 192 L 920 202 L 946 218 L 954 238 L 938 254 L 906 264 '
  'L 872 268 L 838 262 L 808 250 L 786 236 L 768 222 L 752 208 Z',
 'maluku':
  'M 700 214 L 714 208 L 724 220 L 718 238 L 702 244 L 692 230 Z',
 'halmahera':
  'M 710 146 L 722 138 L 732 150 L 740 142 L 744 156 L 728 174 L 714 176 '
  'L 706 162 Z',
 'ntb_ntt':
  'M 450 332 L 470 328 L 486 332 L 478 342 L 456 342 Z '
  'M 502 336 L 530 332 L 554 338 L 544 348 L 514 346 Z '
  'M 568 342 L 600 338 L 628 346 L 642 356 L 616 362 L 582 356 Z',
}

# Di sekitar Bali label-label berdesakan: Denpasar, Mataram, dan Labuan Bajo
# berjarak kurang dari 100 px. Dibiarkan memakai aturan baku, ketiganya
# saling menimpa dan terbaca sebagai satu kata kacau. Jadi di sini
# posisinya ditentukan satu per satu: (penjangkaran, geser-x, geser-y).
LABEL_GESER = {
    'Denpasar':    ('middle', 0, 20),
    'Mataram':     ('start',  10, -7),
    'Labuan Bajo': ('start',  10, 7),
    'Jakarta':     ('end',   -10, -3),
    'Surabaya':    ('start',  10, -8),
    'Makassar':    ('start',  10, 4),
    'Banjarmasin': ('start',  10, 4),
}

def titik_svg():
    out = []
    for n, (lo, la) in KOTA.items():
        x, y = xy(lo, la)
        out.append((n, x, y))
    return out

if __name__ == '__main__':
    for n, x, y in titik_svg():
        print('%-14s %6.1f %6.1f' % (n, x, y))
