# Naratama Adya Dewata — situs baru

## Yang diunggah ke server

    index.html            halaman Indonesia
    en.html               halaman Inggris
    style.css
    script.js
    berita.json           isi ticker berita
    favicon.svg           ikon di bilah tab
    favicon-32.png        cadangan untuk peramban lama
    apple-touch-icon.png  ikon kalau situs disimpan di layar utama HP

Lima berkas itu saja. Total sekitar 60 KB — situs lamamu 3,8 MB untuk satu
halaman Indonesia saja.

## Yang TIDAK perlu diunggah

    isi.py         semua tulisan, dua bahasa, dan data perusahaan
    bangun.py      pembangkit: menghasilkan index.html dan en.html dari isi.py
    peta.py        koordinat kota dan bentuk pulau untuk peta rute
    BACA-DULU.md   berkas ini

Simpan tetap di folder yang sama supaya tidak hilang, tapi tidak masalah
kalau ikut terunggah — ketiganya tidak dibaca oleh peramban.

## SEBELUM TERBIT — wajib

Buka `isi.py`, isi bagian `FIRMA`, terutama `wa` atau `email`. Lalu:

    python3 bangun.py

Selama ketiganya (`wa`, `email`, `formspree`) masih kosong, halaman memasang
spanduk merah di paling atas. Itu disengaja: formulir penawaran belum punya
tujuan kirim, dan situs yang mengucapkan terima kasih sambil membuang
permintaan pelanggan adalah cacat yang membuat situs lamamu gagal diam-diam.

Periksa juga daftar `RUTE` di `isi.py`. Isinya rute yang masuk akal untuk
forwarder berbasis Bali, tapi saya tidak tahu mana yang benar-benar kamu
layani. **Hapus yang tidak kamu kerjakan.** Mencantumkan rute yang tidak kamu
layani adalah cara tercepat kehilangan kepercayaan.

## Mengubah tulisan

Semua tulisan ada di `isi.py`, berpasangan Indonesia–Inggris. Ubah di situ,
jalankan `python3 bangun.py`, kedua bahasa ikut berubah. Tidak ada lagi dua
berkas yang harus disunting dua kali.

## Menambah berita

Buka `berita.json`, tambahkan satu obyek di awal daftar:

    { "tanggal": "2026-11-20",
      "judul": "...",
      "sumber": "Bisnis.com",
      "tautan": "https://..." }

Tidak perlu menjalankan apa pun. Cukup unggah `berita.json` yang baru.

Tanggal **wajib** berbentuk YYYY-MM-DD. Ticker memakainya untuk mengurutkan
dan untuk **menyembunyikan dirinya sendiri** kalau berita terbaru sudah lewat
45 hari. Jadi kalau kamu berhenti memperbarui, tickernya hilang diam-diam —
bukan memajang berita basi yang membuat situs terbaca terbengkalai.

Sekali atau dua kali sebulan sudah cukup.

## Kalau nanti punya foto

Situs ini sengaja dibangun tanpa foto. Nanti kalau sempat memotret kegiatan
sendiri — pakai HP saja, siang hari, dipotong rapat ke satu benda, bukan
pemandangan luas — fotonya bisa masuk satu per satu tanpa merombak apa pun.
Jangan memasang foto stok di bawah tulisan "armada kami"; di situlah
kepercayaan benar-benar patah kalau ketahuan.

## Supaya terpisah dari proyek lain

Buka folder ini sebagai **workspace tersendiri** di VS Code — File → Open
Folder → pilih folder Naratama, bukan folder induknya. Live Server menyajikan
dari folder yang sedang terbuka; kalau yang terbuka folder induk yang juga
berisi Cipta Guru, berkas Cipta Guru ikut terjangkau dan favicon-nya yang
muncul.

Faviconnya sendiri sekarang sudah disebutkan tegas di dalam HTML, jadi
peramban tidak lagi menebak dengan meminta /favicon.ico dari akar server.
