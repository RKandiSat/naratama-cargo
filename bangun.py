# -*- coding: utf-8 -*-
"""Membangun index.html (Indonesia) dan en.html (Inggris) dari isi.py.

   Jalankan:  python3 bangun.py
   Hasil   :  index.html, en.html, style.css, script.js, berita.json

   Ubah tulisan di isi.py, jalankan ini, kedua bahasa ikut berubah.
   Tidak ada lagi dua berkas yang harus disunting dua kali.
"""
import io, json, html
from isi import FIRMA, RUTE, MODA_WARNA, T
from peta import PULAU, KOTA, xy, LABEL_GESER

ID, EN = 0, 1
SIAP = bool(FIRMA['wa'] or FIRMA['email'] or FIRMA['formspree'])
def t(k, i):
    v = T[k]
    return v[i]
def e(s):
    return html.escape(str(s), quote=True)

# ───────────────────────── ikon ─────────────────────────
IKON = {
'truk': '<rect x="2" y="12" width="16" height="11" rx="1.5"/><path d="M18 16h6.5L28 20v3h-10v-7Z" stroke-linejoin="round"/><circle cx="9" cy="25" r="2.4"/><circle cx="23" cy="25" r="2.4"/>',
'kapal': '<path d="M6 17V9h14v8" stroke-linejoin="round"/><path d="M3 17h26l-3 8H6l-3-8Z" stroke-linejoin="round"/><path d="M11 9V5h6v4"/>',
'pesawat': '<path d="M4 19.5 27 11c1.8-.66 3.6 1.1 2.9 2.9l-1 2.6c-.3.8-1 1.4-1.8 1.6L4 22.5" stroke-linejoin="round"/><path d="M13 15.5 6.5 12M15 19l-4 6M20 17l1.5 6.5" stroke-linecap="round"/>',
'centang': '<circle cx="16" cy="16" r="13"/><path d="M10 16.5l4 4 8-9" stroke-linecap="round" stroke-linejoin="round"/>',
'berkas': '<path d="M8 4h11l6 6v18a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1Z" stroke-linejoin="round"/><path d="M19 4v6h6" stroke-linejoin="round"/><path d="M12 18h8M12 23h8" stroke-linecap="round"/>',
}
def ikon(nama, ukuran=32, warna='currentColor', tebal=1.6):
    return ('<svg width="%d" height="%d" viewBox="0 0 32 32" fill="none" stroke="%s" '
            'stroke-width="%s" aria-hidden="true">%s</svg>' % (ukuran, ukuran, warna, tebal, IKON[nama]))

# ───────────────────────── peta ─────────────────────────
def peta_svg(i):
    kota_dipakai = []
    for a, b, *_ in RUTE:
        for k in (a, b):
            if k not in kota_dipakai: kota_dipakai.append(k)

    p = ['<svg viewBox="0 0 1000 420" class="peta" role="img" aria-label="%s" '
         'preserveAspectRatio="xMidYMid meet">' % e(t('peta_judul', i))]
    p.append('<g class="peta-pulau">')
    for d in PULAU.values():
        p.append('<path d="%s"/>' % d)
    p.append('</g>')

    # garis rute: lengkung tipis antar kota
    p.append('<g class="peta-rute">')
    for a, b, moda, *_ in RUTE:
        if a not in KOTA or b not in KOTA: continue
        x1, y1 = xy(*KOTA[a]); x2, y2 = xy(*KOTA[b])
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0 - abs(x2 - x1) * 0.22 - 12
        p.append('<path class="rute-garis moda-%s" d="M %.1f %.1f Q %.1f %.1f %.1f %.1f" '
                 'stroke="%s"/>' % (moda, x1, y1, mx, my, x2, y2, MODA_WARNA[moda]))
    p.append('</g>')

    p.append('<g class="peta-kota">')
    for k in kota_dipakai:
        if k not in KOTA: continue
        x, y = xy(*KOTA[k])
        jangkar, dx, dy = LABEL_GESER.get(k, ('start' if x < 820 else 'end',
                                              9 if x < 820 else -9, 4))
        p.append('<circle cx="%.1f" cy="%.1f" r="4.5"/>' % (x, y))
        # Dua kali: yang pertama tebal sewarna latar sebagai alas, supaya
        # tulisan tetap terbaca saat jatuh di atas garis pulau atau rute.
        for kelas in ('alas', 'atas'):
            p.append('<text class="%s" x="%.1f" y="%.1f" text-anchor="%s">%s</text>'
                     % (kelas, x + dx, y + dy, jangkar, e(k)))
    p.append('</g>')
    p.append('</svg>')

    kunci = ''.join(
        '<span class="kunci-butir"><i style="background:%s"></i>%s</span>'
        % (MODA_WARNA[m], e(t('moda_nama', i)[m])) for m in ('darat', 'laut', 'udara'))
    return ('<figure class="peta-bungkus">%s<figcaption class="peta-kaki">'
            '<span class="peta-kunci">%s</span><span>%s</span></figcaption></figure>'
            % (''.join(p), kunci, e(t('peta_ket', i))))

def tabel_rute(i):
    th = t('rute_th', i)
    b = ['<div class="tabel-gulung"><table class="rute"><thead><tr>']
    for j, h in enumerate(th):
        b.append('<th scope="col"%s>%s</th>' % (' class="num"' if j >= 2 else '', e(h)))
    b.append('</tr></thead><tbody>')
    for a, c, moda, tid, ten, fid, fen in RUTE:
        b.append('<tr>')
        b.append('<td class="rute-nama"><span>%s</span><svg class="panah" width="18" height="8" '
                 'viewBox="0 0 18 8" aria-hidden="true"><path d="M0 4h15M12 1l3 3-3 3" '
                 'stroke="currentColor" stroke-width="1.3" fill="none" stroke-linecap="round" '
                 'stroke-linejoin="round"/></svg><span>%s</span></td>' % (e(a), e(c)))
        b.append('<td><span class="pil moda-%s">%s</span></td>' % (moda, e(t('moda_nama', i)[moda])))
        b.append('<td class="num">%s</td>' % e(tid if i == ID else ten))
        b.append('<td class="num">%s</td>' % e(fid if i == ID else fen))
        b.append('</tr>')
    b.append('</tbody></table></div>')
    return ''.join(b)

# ───────────────────────── potongan ─────────────────────────
def bagian_judul(i, atas, judul, sub=None, terang=False):
    h = ['<div class="bagian-kepala%s">' % (' terang' if terang else '')]
    h.append('<span class="mata">%s</span>' % e(t(atas, i)))
    h.append('<h2>%s</h2>' % e(t(judul, i)))
    if sub: h.append('<p class="bagian-sub">%s</p>' % e(t(sub, i)))
    h.append('</div>')
    return ''.join(h)

def strip_bukti(i):
    butir = [(t('bukti_moda', i), t('bukti_moda_isi', i)),
             (t('bukti_basis', i), t('bukti_basis_isi', i)),
             (t('bukti_balas', i), t('bukti_balas_isi', i))]
    if FIRMA['tahun']:     butir.append((t('bukti_tahun', i), FIRMA['tahun']))
    if FIRMA['nama_resmi']: butir.append((t('bukti_badan', i), FIRMA['nama_resmi']))
    return ('<section class="bukti" aria-label="%s"><div class="wadah bukti-baris">%s</div></section>'
            % (e(t('bukti_moda', i)),
               ''.join('<div class="bukti-butir"><dt>%s</dt><dd>%s</dd></div>' % (e(a), e(b))
                       for a, b in butir)))

def kartu_layanan(i):
    k = []
    for nama_ikon, judul, ringkas, poin in T['layanan']:
        li = ''.join('<li>%s</li>' % e(x) for x in poin[i])
        k.append('<article class="kartu-layanan"><div class="kartu-ikon">%s</div>'
                 '<h3>%s</h3><p>%s</p><ul class="centang">%s</ul></article>'
                 % (ikon(nama_ikon, 30, '#10192B'), e(judul[i]), e(ringkas[i]), li))
    return '<div class="kisi-3">%s</div>' % ''.join(k)

def langkah_langkah(i):
    k = []
    for n, (judul, isi) in enumerate(T['langkah'], 1):
        k.append('<li class="langkah"><span class="langkah-no">%02d</span>'
                 '<h3>%s</h3><p>%s</p></li>' % (n, e(judul[i]), e(isi[i])))
    return '<ol class="kisi-4 langkah-daftar">%s</ol>' % ''.join(k)

def daftar_dokumen(i):
    k = []
    for judul, isi in T['dokumen']:
        k.append('<div class="dok-butir">%s<div><h3>%s</h3><p>%s</p></div></div>'
                 % (ikon('berkas', 22, '#C6963A', 1.5), e(judul[i]), e(isi[i])))
    return '<div class="kisi-dok">%s</div>' % ''.join(k)

def daftar_kenapa(i):
    k = []
    for judul, isi in T['kenapa']:
        k.append('<div class="kenapa-butir">%s<div><h3>%s</h3><p>%s</p></div></div>'
                 % (ikon('centang', 24, '#C6963A', 1.6), e(judul[i]), e(isi[i])))
    return '<div class="kenapa-daftar">%s</div>' % ''.join(k)

def daftar_tanya(i):
    k = []
    for n, (q, a) in enumerate(T['tanya']):
        k.append('<details class="tanya"%s><summary><span>%s</span>'
                 '<svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true">'
                 '<path d="M7 1v12M1 7h12" stroke="currentColor" stroke-width="1.6" '
                 'stroke-linecap="round"/></svg></summary><p>%s</p></details>'
                 % (' open' if n == 0 else '', e(q[i]), e(a[i])))
    return '<div class="tanya-daftar">%s</div>' % ''.join(k)

def isian(idn, label, i, tipe='text', ph='', wajib=False, lebar=''):
    w = ' <abbr class="wajib" title="%s">*</abbr>' % e(t('f_wajib', i)) if wajib else ''
    return ('<div class="isian %s"><label for="%s">%s%s</label>'
            '<input id="%s" name="%s" type="%s" placeholder="%s"%s></div>'
            % (lebar, idn, e(label), w, idn, idn, tipe, e(ph), ' required' if wajib else ''))

def pilihan(idn, label, opsi, lebar=''):
    o = ''.join('<option>%s</option>' % e(x) for x in opsi)
    return ('<div class="isian %s"><label for="%s">%s</label>'
            '<select id="%s" name="%s">%s</select></div>' % (lebar, idn, e(label), idn, idn, o))

def formulir(i):
    f = ['<form id="form-penawaran" class="form" novalidate>']
    f.append('<div class="form-kisi">')
    f.append(isian('nama',   t('f_nama', i),  i, wajib=True))
    f.append(isian('firma',  t('f_firma', i), i))
    f.append(isian('email',  t('f_email', i), i, tipe='email'))
    f.append(isian('telp',   t('f_telp', i),  i, tipe='tel', ph='+62 8xx xxxx xxxx', wajib=True))
    f.append(pilihan('moda',  t('f_moda', i),  t('f_moda_opt', i)))
    f.append(pilihan('jenis', t('f_jenis', i), t('f_jenis_opt', i)))
    f.append(isian('asal',   t('f_asal', i),   i, wajib=True))
    f.append(isian('tujuan', t('f_tujuan', i), i, wajib=True))
    f.append(isian('barang', t('f_barang', i), i, ph=t('f_barang_ph', i), wajib=True, lebar='penuh'))
    f.append(isian('berat',  t('f_berat', i),  i, tipe='number'))
    f.append(isian('volume', t('f_volume', i), i, tipe='number'))
    f.append(isian('koli',   t('f_koli', i),   i, tipe='number'))
    f.append(isian('dimensi', t('f_dimensi', i), i, ph=t('f_dimensi_ph', i)))
    f.append(isian('tanggal', t('f_tanggal', i), i, tipe='date'))
    f.append(pilihan('incoterm', t('f_incoterm', i), t('f_incoterm_opt', i)))
    f.append('<div class="isian penuh"><label for="catatan">%s</label>'
             '<textarea id="catatan" name="catatan" rows="3" placeholder="%s"></textarea></div>'
             % (e(t('f_catatan', i)), e(t('f_catatan_ph', i))))
    f.append('</div>')
    f.append('<p class="form-bantu">%s</p>' % e(t('f_bantu', i)))
    f.append('<div class="form-tombol">')
    if FIRMA['wa']:
        f.append('<button type="submit" class="tbl tbl-utama" data-lewat="wa">%s</button>'
                 % e(t('f_kirim_wa', i)))
        f.append('<button type="button" class="tbl tbl-garis-gelap" data-lewat="email">%s</button>'
                 % e(t('f_kirim_em', i)))
    else:
        f.append('<button type="submit" class="tbl tbl-utama" data-lewat="email">%s</button>'
                 % e(t('f_kirim', i)))
    f.append('</div>')
    f.append('<p class="form-galat" id="form-galat" role="alert" hidden>%s</p>'
             % e(t('f_kurang', i)))
    f.append('<p class="form-sukses" id="form-sukses" role="status" hidden>%s</p>'
             % e(t('f_terkirim', i)))
    f.append('</form>')
    return ''.join(f)

def blok_kontak(i):
    b = ['<div class="kontak-rinci">']
    b.append('<h3>%s</h3>' % e(t('kon_judul', i)))
    b.append('<dl>')
    if FIRMA['pic']:
        jab = FIRMA['pic_jabatan_id'] if i == ID else FIRMA['pic_jabatan_en']
        b.append('<dt>%s</dt><dd>%s%s</dd>' % (e(t('kon_pic', i)), e(FIRMA['pic']),
                 ' — ' + e(jab) if jab else ''))
    if FIRMA['telepon']:
        b.append('<dt>%s</dt><dd><a href="tel:%s">%s</a></dd>' % (e(t('kon_telepon', i)),
                 e(FIRMA['telepon'].replace(' ', '')), e(FIRMA['telepon'])))
    if FIRMA['wa']:
        b.append('<dt>WhatsApp</dt><dd><a href="https://wa.me/%s" rel="noopener">+%s</a></dd>'
                 % (e(FIRMA['wa']), e(FIRMA['wa'])))
    if FIRMA['email']:
        b.append('<dt>Email</dt><dd><a href="mailto:%s">%s</a></dd>'
                 % (e(FIRMA['email']), e(FIRMA['email'])))
    if FIRMA['alamat']:
        peta = (' <a class="tautan-peta" href="%s" target="_blank" rel="noopener">%s</a>'
                % (e(FIRMA['maps']), e(t('kon_peta', i)))) if FIRMA['maps'] else ''
        b.append('<dt>%s</dt><dd>%s%s</dd>' % (e(t('kon_alamat', i)), e(FIRMA['alamat']), peta))
    jam = FIRMA['jam_id'] if i == ID else FIRMA['jam_en']
    if jam:
        b.append('<dt>%s</dt><dd>%s</dd>' % (e(t('kon_jam', i)), e(jam)))
    legal = ' · '.join(x for x in [
        FIRMA['nama_resmi'],
        ('NIB ' + FIRMA['nib']) if FIRMA['nib'] else '',
        ('NPWP ' + FIRMA['npwp']) if FIRMA['npwp'] else '',
        FIRMA['asosiasi']] if x)
    if legal:
        b.append('<dt>%s</dt><dd>%s</dd>' % (e(t('kon_legal', i)), e(legal)))
    b.append('</dl></div>')
    return ''.join(b)

def json_ld(i):
    org = {"@context": "https://schema.org", "@type": "Organization",
           "name": FIRMA['nama_resmi'] or FIRMA['nama'],
           "description": t('deskripsi', i),
           "address": {"@type": "PostalAddress", "streetAddress": FIRMA['alamat'],
                       "addressRegion": "Bali", "addressCountry": "ID"}}
    if FIRMA['telepon']: org['telephone'] = FIRMA['telepon']
    if FIRMA['email']:   org['email'] = FIRMA['email']
    if FIRMA['tahun']:   org['foundingDate'] = FIRMA['tahun']
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q[i],
                           "acceptedAnswer": {"@type": "Answer", "text": a[i]}}
                          for q, a in T['tanya']]}
    return ('<script type="application/ld+json">%s</script>\n'
            '<script type="application/ld+json">%s</script>'
            % (json.dumps(org, ensure_ascii=False), json.dumps(faq, ensure_ascii=False)))

# ───────────────────────── halaman ─────────────────────────
def halaman(i):
    berkas_ini  = 'index.html' if i == ID else 'en.html'
    berkas_lain = 'en.html' if i == ID else 'index.html'
    label_lain  = 'EN' if i == ID else 'ID'
    nav = [('#layanan', 'nav_layanan'), ('#rute', 'nav_rute'), ('#cara-kerja', 'nav_cara'),
           ('#dokumen', 'nav_dokumen'), ('#tanya', 'nav_tanya'), ('#kontak', 'nav_kontak')]

    h = []
    h.append('<!doctype html>\n<html lang="%s">\n<head>' % t('html_lang', i))
    h.append('<meta charset="utf-8">')
    h.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    h.append('<title>%s</title>' % e(t('judul_tab', i)))
    h.append('<meta name="description" content="%s">' % e(t('deskripsi', i)))
    h.append('<link rel="alternate" hreflang="id" href="index.html">')
    h.append('<link rel="alternate" hreflang="en" href="en.html">')
    h.append('<link rel="alternate" hreflang="x-default" href="index.html">')
    h.append('<meta property="og:type" content="website">')
    h.append('<meta property="og:title" content="%s">' % e(t('judul_tab', i)))
    h.append('<meta property="og:description" content="%s">' % e(t('deskripsi', i)))
    h.append('<meta property="og:locale" content="%s">' % ('id_ID' if i == ID else 'en_US'))
    h.append('<meta name="theme-color" content="#0E1930">')
    # Favicon disebutkan dengan tegas. Tanpa ini peramban menebak sendiri
    # dengan meminta /favicon.ico dari akar server -- dan di Live Server,
    # akar servernya folder yang kebetulan kamu buka di VS Code. Itulah
    # sebabnya favicon Cipta Guru sempat muncul di halaman Naratama.
    h.append('<link rel="icon" href="favicon.svg" type="image/svg+xml">')
    h.append('<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">')
    h.append('<link rel="apple-touch-icon" href="apple-touch-icon.png">')
    h.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
    h.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    h.append('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
             'family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&'
             'family=Public+Sans:wght@400;500;600;700&display=swap">')
    h.append('<link rel="stylesheet" href="style.css">')
    h.append('<script src="script.js" defer></script>')
    h.append(json_ld(i))
    h.append('</head>\n<body>')
    h.append('<a class="lewati" href="#utama">%s</a>' % e(t('lewati', i)))

    # Tanpa WhatsApp, email, atau Formspree, formulir tidak punya tujuan --
    # dan situs yang mengucapkan terima kasih sambil membuang permintaan
    # pelanggan adalah cacat yang persis membuat situs sebelumnya gagal.
    # Jadi keadaan itu TIDAK disembunyikan: dia berteriak di paling atas,
    # supaya ketahuan oleh siapa pun, termasuk olehmu sendiri.
    if not SIAP:
        h.append('<div class="belum-siap">%s</div>' % e(
            'BELUM SIAP TERBIT — isi WhatsApp atau email di isi.py, lalu jalankan '
            'python3 bangun.py. Sebelum itu, formulir penawaran tidak punya tujuan kirim.'
            if i == ID else
            'NOT READY TO PUBLISH — set WhatsApp or email in isi.py and run '
            'python3 bangun.py. Until then the quote form has nowhere to send.'))

    # ── ticker ──
    h.append('<div class="ticker" id="ticker" hidden>'
             '<div class="wadah ticker-dalam">'
             '<span class="ticker-label">%s</span>'
             '<div class="ticker-jendela"><div class="ticker-jalur" id="ticker-jalur"></div></div>'
             '<button type="button" class="ticker-jeda" id="ticker-jeda" '
             'data-jeda="%s" data-jalan="%s" aria-label="%s">❚❚</button>'
             '</div></div>'
             % (e(t('ticker_label', i)), e(t('ticker_jeda', i)),
                e(t('ticker_jalan', i)), e(t('ticker_jeda', i))))

    # ── kepala ──
    h.append('<header class="kepala" id="kepala"><div class="wadah kepala-dalam">')
    h.append('<a class="merek" href="#atas"><span class="merek-1">Naratama</span>'
             '<span class="merek-2">ADYA DEWATA</span></a>')
    h.append('<nav class="nav" id="nav" aria-label="%s">' % e(t('nav_layanan', i)))
    h.append(''.join('<a href="%s">%s</a>' % (u, e(t(k, i))) for u, k in nav))
    h.append('</nav>')
    h.append('<div class="kepala-kanan">')
    # Nomor telepon di bilah atas. Untuk jasa kargo, menelepon masih jalur
    # yang paling sering dipakai calon klien pertama kali -- menaruhnya di
    # sini berarti dia tidak perlu menggulung sampai bawah untuk menemukannya.
    if FIRMA['telepon']:
        h.append('<a class="kepala-telp sembunyi-hp" href="tel:%s">'
                 '<svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
                 '<path d="M5.2 2.5 6.8 5.4 5.4 6.9c.7 1.5 1.9 2.7 3.4 3.4l1.5-1.4 2.9 1.6-.5 2.2'
                 'c-.1.5-.6.8-1.1.8C6.4 13.5 2.5 9.6 2.2 4c0-.5.3-1 .8-1.1l2.2-.4Z" '
                 'stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg>%s</a>'
                 % (e(FIRMA['telepon'].replace(' ', '')), e(FIRMA['telepon'])))
    h.append('<a class="bahasa" href="%s" hreflang="%s">%s</a>'
             % (berkas_lain, 'en' if i == ID else 'id', label_lain))
    h.append('<a class="tbl tbl-gelap sembunyi-hp" href="#kontak">%s</a>' % e(t('cta', i)))
    h.append('<button class="menu-tbl" id="menu-tbl" aria-expanded="false" '
             'aria-controls="nav" aria-label="Menu"><span></span><span></span><span></span></button>')
    h.append('</div></div></header>')

    h.append('<main id="utama">')

    # ── hero ──
    h.append('<section class="hero" id="atas">')
    h.append('''<svg class="hero-peta" viewBox="0 0 1440 640" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs><filter id="beaconGlow" x="-120%" y="-120%" width="340%" height="340%">
<feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<radialGradient id="aurora"><stop offset="0%" stop-color="#C6963A" stop-opacity="0.30"/><stop offset="100%" stop-color="#C6963A" stop-opacity="0"/></radialGradient></defs>
<ellipse class="hero-aurora" cx="1080" cy="180" rx="440" ry="300" fill="url(#aurora)"/>
<g stroke="#C6963A" fill="none" stroke-linecap="round">
<path class="route-line" d="M -60 520 C 300 420, 500 460, 760 340 S 1200 160, 1520 120" stroke-dasharray="3 11"/>
<path class="route-line slow" d="M -60 300 C 260 260, 620 340, 900 220 S 1300 60, 1520 30" stroke-dasharray="3 11" opacity="0.6"/>
<path class="route-line slower" d="M -60 620 C 360 580, 700 540, 1020 430 S 1340 320, 1520 290" stroke-dasharray="3 11" opacity="0.4"/>
</g>
<g fill="#C6963A" class="hero-titik">
<circle class="route-beacon" cx="300" cy="420" r="3.5"/><circle class="route-beacon" cx="760" cy="340" r="3.5"/>
<circle class="route-beacon" cx="1200" cy="160" r="3.5"/><circle class="route-beacon" cx="620" cy="340" r="3.5"/>
<circle class="route-beacon" cx="1020" cy="430" r="3.5"/></g></svg>''')
    h.append('<div class="wadah hero-dalam">')
    h.append('<span class="mata emas">%s</span>' % e(t('hero_atas', i)))
    h.append('<h1>%s</h1>' % e(t('hero_judul', i)))
    h.append('<p class="hero-sub">%s</p>' % e(t('hero_sub', i)))
    h.append('<div class="hero-tombol"><a class="tbl tbl-utama" href="#kontak">%s</a>'
             '<a class="tbl tbl-garis" href="#rute">%s</a></div>'
             % (e(t('cta', i)), e(t('hero_cta2', i))))
    h.append('</div></section>')

    h.append(strip_bukti(i))

    # ── layanan ──
    h.append('<section class="bagian" id="layanan"><div class="wadah">')
    h.append(bagian_judul(i, 'lay_atas', 'lay_judul', 'lay_sub'))
    h.append(kartu_layanan(i))
    h.append('</div></section>')

    # ── rute ──
    h.append('<section class="bagian gelap" id="rute"><div class="wadah">')
    h.append(bagian_judul(i, 'rute_atas', 'rute_judul', 'rute_sub', terang=True))
    h.append(peta_svg(i))
    h.append(tabel_rute(i))
    h.append('<p class="rute-lain">%s</p>' % e(t('rute_lain', i)))
    h.append('</div></section>')

    # ── cara kerja ──
    h.append('<section class="bagian putih" id="cara-kerja"><div class="wadah">')
    h.append(bagian_judul(i, 'cara_atas', 'cara_judul'))
    h.append(langkah_langkah(i))
    h.append('</div></section>')

    # ── dokumen ──
    h.append('<section class="bagian" id="dokumen"><div class="wadah">')
    h.append(bagian_judul(i, 'dok_atas', 'dok_judul', 'dok_sub'))
    h.append(daftar_dokumen(i))
    h.append('</div></section>')

    # ── kenapa kami ──
    h.append('<section class="bagian putih" id="kenapa"><div class="wadah dua-kolom">')
    h.append('<div class="bagian-kepala lengket">'
             '<span class="mata">%s</span><h2>%s</h2></div>'
             % (e(t('ken_atas', i)), e(t('ken_judul', i))))
    h.append(daftar_kenapa(i))
    h.append('</div></section>')

    # ── tanya jawab ──
    h.append('<section class="bagian" id="tanya"><div class="wadah sempit">')
    h.append(bagian_judul(i, 'tanya_atas', 'tanya_judul'))
    h.append(daftar_tanya(i))
    h.append('</div></section>')

    # ── formulir ──
    h.append('<section class="bagian gelap" id="kontak"><div class="wadah kontak-kisi">')
    h.append('<div class="kontak-kiri"><span class="mata emas">%s</span><h2>%s</h2>'
             '<p class="bagian-sub">%s</p>%s</div>'
             % (e(t('form_atas', i)), e(t('form_judul', i)), e(t('form_sub', i)), blok_kontak(i)))
    h.append('<div class="kontak-kanan">%s</div>' % formulir(i))
    h.append('</div></section>')

    h.append('</main>')

    # ── kaki ──
    h.append('<footer class="kaki"><div class="wadah">')
    h.append('<div class="kaki-atas"><div class="kaki-merek">'
             '<span class="merek-1">%s</span><p>%s</p></div>'
             '<nav class="kaki-nav" aria-label="%s">%s</nav></div>'
             % (e(FIRMA['nama']), e(t('kaki_tentang', i)), e(t('nav_kontak', i)),
                ''.join('<a href="%s">%s</a>' % (u, e(t(k, i))) for u, k in nav)))
    hub = []
    if FIRMA['telepon']:
        hub.append('<a href="tel:%s">%s</a>'
                   % (e(FIRMA['telepon'].replace(' ', '')), e(FIRMA['telepon'])))
    if FIRMA['wa']:
        hub.append('<a href="https://wa.me/%s" rel="noopener">WhatsApp</a>' % e(FIRMA['wa']))
    if FIRMA['email']:
        hub.append('<a href="mailto:%s">%s</a>' % (e(FIRMA['email']), e(FIRMA['email'])))
    if FIRMA['alamat']:
        hub.append('<span>%s</span>' % e(FIRMA['alamat']))
    if hub: h.append('<p class="kaki-hubungi">%s</p>' % ' · '.join(hub))

    legal = ' · '.join(x for x in [
        FIRMA['nama_resmi'], ('NIB ' + FIRMA['nib']) if FIRMA['nib'] else '',
        ('NPWP ' + FIRMA['npwp']) if FIRMA['npwp'] else '', FIRMA['asosiasi']] if x)
    if legal: h.append('<p class="kaki-legal">%s</p>' % e(legal))
    h.append('<p class="kaki-legal">%s</p>' % e(t('kaki_ket', i)))
    h.append('<div class="kaki-bawah"><span>© 2026 %s. %s</span>'
             '<a href="%s" hreflang="%s">%s</a></div>'
             % (e(FIRMA['nama']), e(t('kaki_hak', i)), berkas_lain,
                'en' if i == ID else 'id', e(t('kaki_bahasa', i))))
    h.append('</div></footer>')

    h.append('<script>window.NARATAMA=%s;</script>' % json.dumps({
        'lang': t('html_lang', i), 'wa': FIRMA['wa'], 'email': FIRMA['email'],
        'formspree': FIRMA['formspree'], 'judulPesan': t('f_judul_pesan', i),
        'label': {k: t('f_' + k, i) for k in
                  ['nama','firma','email','telp','moda','jenis','asal','tujuan','barang',
                   'berat','volume','koli','dimensi','tanggal','incoterm','catatan']},
    }, ensure_ascii=False))
    h.append('</body>\n</html>')
    return '\n'.join(h)

if __name__ == '__main__':
    for i, nama in ((ID, 'index.html'), (EN, 'en.html')):
        io.open(nama, 'w', encoding='utf-8', newline='\n').write(halaman(i))
        print('%-12s %6d byte' % (nama, len(halaman(i).encode('utf-8'))))
    if not SIAP:
        print()
        print('  PERINGATAN: wa, email, dan formspree ketiganya kosong di isi.py.')
        print('  Formulir penawaran belum punya tujuan kirim, dan halaman memasang')
        print('  spanduk merah di paling atas sampai salah satunya diisi.')
    kurang = [k for k in ('telepon','email','nib','tahun','pic') if not FIRMA[k]]
    if kurang:
        print('  Belum diisi di isi.py: ' + ', '.join(kurang) +
              ' — barisnya tidak ditampilkan, bukan muncul sebagai kurung siku.')
