# -*- coding: utf-8 -*-
"""ISI SITUS — SATU SUMBER UNTUK DUA BAHASA.

   Situs lamamu punya dua berkas yang dibangun dengan cara yang sama sekali
   berbeda: yang Inggris HTML biasa 10 KB, yang Indonesia hasil ekspor
   bundler 3,8 MB. Setiap perbaikan harus dikerjakan dua kali, dan cepat
   atau lambat isinya akan berbeda.

   Di sini tidak bisa. Semua tulisan ada di berkas ini, berpasangan
   Indonesia-Inggris. `bangun.py` menghasilkan index.html dan en.html dari
   pasangan itu. Lupa menerjemahkan satu kalimat = galat saat membangun,
   bukan ketahuan tiga bulan kemudian oleh pengunjung.
"""

# ════════════════════════════════════════════════════════════════════
# BAGIAN YANG HARUS KAMU ISI
# ────────────────────────────────────────────────────────────────────
# Yang dikosongkan TIDAK akan muncul di halaman — tidak ada kurung siku
# seperti [NOMOR TELEPON] yang membuat situs terlihat belum jadi. Baris
# yang kosong hilang sama sekali, dan bagiannya menyesuaikan diri.
# ════════════════════════════════════════════════════════════════════
FIRMA = {
    'nama':        'Naratama Adya Dewata',
    'nama_resmi':  '',          # mis. 'PT Naratama Adya Dewata'
    'alamat':      'Jalan Raya Abianbase No. 89, Kel. Abianbase, '
                   'Kec. Mengwi, Kab. Badung, Bali 80351',
    'telepon':     '0815 4261 2333',
    'wa':          '6281542612333',   # 0815... ditulis ulang dengan awalan 62
    'email':       'naratamaadyadewata.cs@gmail.com',
    'nib':         '',
    'npwp':        '',
    'tahun':       '',          # tahun mulai beroperasi, mis. '2025'
    'asosiasi':    '',          # mis. 'ALFI/ILFA Bali' — kosongkan jika belum
    'pic':         '',          # nama orang yang menangani permintaan masuk
    'pic_jabatan_id': '', 'pic_jabatan_en': '',
    'jam_id':      'Senin–Jumat 08.00–17.00 WITA, Sabtu 08.00–13.00 WITA',
    'jam_en':      'Mon–Fri 8am–5pm WITA, Sat 8am–1pm WITA',
    'maps':        '',          # tautan Google Maps kantor
    # Kalau nanti mau formulir masuk ke email sungguhan, daftar gratis di
    # formspree.io lalu tempel alamat endpoint-nya di sini. Dikosongkan,
    # formulir tetap bekerja lewat WhatsApp dan email.
    'formspree':   '',
}

# ════════════════════════════════════════════════════════════════════
# RUTE — PERIKSA SEBELUM TERBIT
# ────────────────────────────────────────────────────────────────────
# Ini rute yang masuk akal untuk forwarder berbasis Bali, TAPI saya tidak
# tahu mana yang benar-benar kamu layani. Hapus yang tidak kamu kerjakan.
# Mencantumkan rute yang tidak kamu layani adalah cara tercepat kehilangan
# kepercayaan: klien menelepon, kamu menolak, dan dia tidak menelepon lagi.
#
# (kota asal, kota tujuan, moda, estimasi transit ID, transit EN, frekuensi ID, frekuensi EN)
RUTE = [
    ('Denpasar', 'Surabaya',    'darat', '1–2 hari',  '1–2 days',  'Harian',      'Daily'),
    ('Denpasar', 'Jakarta',     'darat', '3–4 hari',  '3–4 days',  'Harian',      'Daily'),
    ('Denpasar', 'Jakarta',     'udara', '1 hari',    '1 day',     'Harian',      'Daily'),
    ('Denpasar', 'Makassar',    'laut',  '3–5 hari',  '3–5 days',  '2x seminggu', 'Twice weekly'),
    ('Denpasar', 'Mataram',     'darat', '1 hari',    '1 day',     'Harian',      'Daily'),
    ('Denpasar', 'Labuan Bajo', 'laut',  '2–3 hari',  '2–3 days',  'Mingguan',    'Weekly'),
    ('Surabaya', 'Banjarmasin', 'laut',  '2–3 hari',  '2–3 days',  'Mingguan',    'Weekly'),
    ('Jakarta',  'Medan',       'laut',  '4–6 hari',  '4–6 days',  'Mingguan',    'Weekly'),
]

MODA_WARNA = {'darat': '#C6963A', 'laut': '#5B9BBF', 'udara': '#D98F5F'}

# ════════════════════════════════════════════════════════════════════
# TULISAN
# ════════════════════════════════════════════════════════════════════
T = {
'html_lang':   ('id', 'en'),
'judul_tab':   ('Naratama Adya Dewata — Logistik Darat, Udara & Laut dari Bali',
                'Naratama Adya Dewata — Land, Air & Sea Logistics from Bali'),
'deskripsi':   ('Jasa pengiriman kargo darat, udara, dan laut dari Bali ke seluruh Indonesia. '
                'Satu mitra untuk seluruh rantai pasok Anda, dengan penawaran dalam 1x24 jam.',
                'Land, air and sea freight forwarding from Bali across Indonesia. '
                'One partner for your whole supply chain, with a quote within 24 hours.'),

'nav_layanan': ('Layanan', 'Services'),
'nav_rute':    ('Rute', 'Routes'),
'nav_cara':    ('Cara Kerja', 'How It Works'),
'nav_dokumen': ('Dokumen', 'Documents'),
'nav_tanya':   ('Tanya Jawab', 'FAQ'),
'nav_kontak':  ('Kontak', 'Contact'),
'cta':         ('Minta Penawaran', 'Request a Quote'),
'lewati':      ('Langsung ke isi', 'Skip to content'),

'ticker_label': ('KABAR KARGO', 'CARGO BRIEF'),
'ticker_jeda':  ('Jeda', 'Pause'),
'ticker_jalan': ('Jalankan', 'Play'),

'hero_atas':   ('LOGISTIK MULTIMODA · BALI', 'MULTIMODAL LOGISTICS · BALI'),
'hero_judul':  ('Darat, udara, laut — satu mitra untuk seluruh rantai pasok Anda.',
                'Land, air, sea — one partner for your entire supply chain.'),
'hero_sub':    ('Kami mengurus muatan Anda dari pintu asal sampai pintu tujuan: '
                'penjemputan, dokumen, pemilihan moda, dan pemantauan — dengan satu orang '
                'yang bisa Anda hubungi dari awal sampai barang diterima.',
                'We move your cargo door to door: pickup, documentation, mode selection and '
                'tracking — with one person you can reach from the first call until the '
                'goods are received.'),
'hero_cta2':   ('Lihat Rute & Waktu Tempuh', 'See Routes & Transit Times'),

'bukti_moda':      ('Moda layanan', 'Service modes'),
'bukti_moda_isi':  ('Darat · Laut · Udara', 'Land · Sea · Air'),
'bukti_basis':     ('Basis operasi', 'Operating base'),
'bukti_basis_isi': ('Badung, Bali', 'Badung, Bali'),
'bukti_balas':     ('Penawaran', 'Quotes'),
'bukti_balas_isi': ('Dalam 1x24 jam', 'Within 24 hours'),
'bukti_tahun':     ('Beroperasi sejak', 'Operating since'),
'bukti_badan':     ('Badan hukum', 'Legal entity'),

'lay_atas':  ('LAYANAN', 'SERVICES'),
'lay_judul': ('Tiga moda, satu tim yang mengurus semuanya.',
              'Three modes, one team handling all of them.'),
'lay_sub':   ('Anda tidak perlu mencari vendor terpisah untuk tiap kaki perjalanan. '
              'Kami yang menyambungkannya.',
              'You do not need a separate vendor for each leg. We connect them.'),
'layanan': [
  ('truk',
   ('Angkutan Darat', 'Land Freight'),
   ('Pengiriman antarkota dan antarpulau lewat jalur darat dan penyeberangan, '
    'untuk muatan penuh maupun gabungan.',
    'Intercity and inter-island delivery by road and ferry, for full or consolidated loads.'),
   (['FTL — satu kendaraan untuk muatan Anda sendiri',
     'LTL — muatan gabungan, bayar sesuai ruang yang dipakai',
     'Penjemputan di gudang, pabrik, atau rumah',
     'Pengantaran sampai alamat tujuan, bukan sampai terminal'],
    ['FTL — a dedicated vehicle for your cargo alone',
     'LTL — consolidated loads, pay for the space you use',
     'Pickup at warehouse, factory or residence',
     'Delivery to the destination address, not just to a terminal'])),
  ('kapal',
   ('Kargo Laut', 'Sea Freight'),
   ('Pilihan paling hemat untuk muatan besar dan berat, domestik maupun ekspor-impor.',
    'The most economical option for large, heavy shipments, domestic and international.'),
   (['FCL — satu kontainer penuh (20ft / 40ft / 40HC)',
     'LCL — muatan gabungan dalam satu kontainer',
     'Pengurusan dokumen pelayaran dan Bill of Lading',
     'Koordinasi bongkar muat di pelabuhan asal dan tujuan'],
    ['FCL — a full container (20ft / 40ft / 40HC)',
     'LCL — consolidated cargo sharing a container',
     'Shipping documentation and Bill of Lading handling',
     'Loading and discharge coordination at both ports'])),
  ('pesawat',
   ('Kargo Udara', 'Air Freight'),
   ('Untuk muatan yang mendesak, bernilai tinggi, atau mudah rusak.',
    'For urgent, high-value or perishable cargo.'),
   (['Pengiriman cepat antarkota besar, umumnya tiba hari berikutnya',
     'Cocok untuk suku cadang, dokumen penting, dan barang mudah rusak',
     'Pengurusan Air Waybill dan pemeriksaan keamanan kargo',
     'Antar-jemput dari dan ke bandara'],
    ['Fast delivery between major cities, usually next-day arrival',
     'Suited to spare parts, critical documents and perishables',
     'Air Waybill handling and cargo security screening',
     'Pickup and delivery to and from the airport'])),
],

'rute_atas':  ('RUTE', 'ROUTES'),
'rute_judul': ('Ke mana kami mengirim, dan berapa lama.',
               'Where we ship, and how long it takes.'),
'rute_sub':   ('Waktu tempuh di bawah adalah perkiraan untuk keadaan normal, dihitung sejak '
               'muatan diambil. Cuaca, jadwal kapal, dan antrean pelabuhan dapat mengubahnya — '
               'kalau itu terjadi, kami memberi tahu Anda, bukan menunggu Anda bertanya.',
               'The transit times below are estimates under normal conditions, counted from '
               'pickup. Weather, vessel schedules and port queues can change them — when that '
               'happens we tell you, rather than waiting for you to ask.'),
'rute_th':    (('Rute', 'Moda', 'Estimasi transit', 'Keberangkatan'),
               ('Route', 'Mode', 'Estimated transit', 'Departures')),
'rute_lain':  ('Tujuan Anda tidak ada di daftar? Sebagian besar kota di Indonesia tetap bisa '
               'kami layani lewat jaringan mitra. Tanyakan saja.',
               'Your destination not listed? We still serve most Indonesian cities through our '
               'partner network. Just ask.'),
'moda_nama':  ({'darat': 'Darat', 'laut': 'Laut', 'udara': 'Udara'},
               {'darat': 'Land', 'laut': 'Sea', 'udara': 'Air'}),
'peta_judul': ('Jangkauan pengiriman', 'Shipping coverage'),
'peta_ket':   ('Peta skematis. Titik menandai kota yang kami layani langsung.',
               'Schematic map. Dots mark cities we serve directly.'),

'cara_atas':  ('CARA KERJA', 'HOW IT WORKS'),
'cara_judul': ('Dari permintaan sampai kargo diterima.', 'From request to cargo received.'),
'langkah': [
  (('Ajukan Permintaan', 'Submit a Request'),
   ('Kirim detail muatan, asal, dan tujuan lewat formulir di bawah atau WhatsApp. '
    'Makin lengkap detailnya, makin cepat penawarannya keluar.',
    'Send your cargo details, origin and destination through the form below or by WhatsApp. '
    'The more complete the details, the faster the quote.')),
  (('Terima Penawaran', 'Receive a Quote'),
   ('Kami balas dalam 1x24 jam kerja dengan rincian biaya, moda yang disarankan, dan '
    'perkiraan waktu tempuh — bukan angka gelondongan tanpa penjelasan.',
    'We reply within one working day with a cost breakdown, the mode we recommend and an '
    'estimated transit time — not a single lump-sum figure.')),
  (('Kami Jalankan', 'We Execute'),
   ('Penjemputan, pengemasan ulang bila perlu, dokumen pengiriman, dan koordinasi antarmoda '
    'kami yang urus. Anda tidak berhubungan dengan banyak pihak.',
    'Pickup, repacking where needed, shipping documents and inter-modal coordination are ours '
    'to handle. You deal with one party, not many.')),
  (('Pantau & Terima', 'Track & Receive'),
   ('Anda dapat kabar di setiap tahap penting, dan bukti serah terima saat barang diterima '
    'di tujuan.',
    'You get an update at every significant stage, and proof of delivery when the goods are '
    'received at destination.')),
],

'dok_atas':  ('DOKUMEN & KEPABEANAN', 'DOCUMENTS & CUSTOMS'),
'dok_judul': ('Dokumen yang kami urus, supaya muatan Anda tidak tertahan.',
              'The paperwork we handle, so your cargo is not held up.'),
'dok_sub':   ('Sebagian besar keterlambatan kargo bukan karena kendaraannya, tapi karena '
              'dokumennya kurang satu. Ini yang kami siapkan dan periksa sebelum barang '
              'berangkat.',
              'Most cargo delays are not caused by the vehicle but by one missing document. '
              'This is what we prepare and check before anything moves.'),
'dokumen': [
  (('Surat jalan & packing list', 'Delivery order & packing list'),
   ('Rincian isi, jumlah koli, berat, dan dimensi tiap kemasan.',
    'Contents, number of packages, weight and dimensions of each unit.')),
  (('Bill of Lading (B/L)', 'Bill of Lading (B/L)'),
   ('Dokumen pengangkutan laut sekaligus bukti kepemilikan muatan.',
    'The sea transport document and title to the goods.')),
  (('Air Waybill (AWB)', 'Air Waybill (AWB)'),
   ('Dokumen pengangkutan udara, sekaligus nomor untuk pelacakan.',
    'The air transport document, which also serves as the tracking number.')),
  (('PEB & PIB', 'Export & import declarations'),
   ('Pemberitahuan ekspor dan impor barang untuk pengiriman lintas negara.',
    'Customs declarations for cross-border shipments.')),
  (('Klasifikasi HS Code', 'HS code classification'),
   ('Penentuan kode barang yang menentukan bea dan izin yang berlaku.',
    'Determining the commodity code that sets the duty and permits that apply.')),
  (('Asuransi muatan', 'Cargo insurance'),
   ('Perlindungan nilai barang selama perjalanan, atas permintaan.',
    'Cover for the value of the goods while in transit, on request.')),
],

'ken_atas':  ('KENAPA KAMI', 'WHY US'),
'ken_judul': ('Satu mitra, bukan sekadar vendor pengiriman.',
              'One partner, not just another shipping vendor.'),
'kenapa': [
  (('Satu orang yang bertanggung jawab', 'One person who is accountable'),
   ('Anda tidak dioper dari bagian ke bagian. Satu nama, satu nomor, dari penawaran '
    'sampai barang diterima — termasuk saat ada masalah.',
    'You are not passed between departments. One name, one number, from quote to delivery — '
    'including when something goes wrong.')),
  (('Moda dipilih dari kebutuhan, bukan dari stok kami', 'Mode chosen from your need, not our stock'),
   ('Kami tidak memaksakan satu moda. Kalau laut lebih masuk akal untuk muatan Anda '
    'meski komisinya lebih kecil buat kami, itu yang kami sarankan.',
    'We do not push one mode. If sea makes more sense for your cargo even when it earns us '
    'less, that is what we will recommend.')),
  (('Kabar buruk disampaikan lebih awal', 'Bad news delivered early'),
   ('Kapal tertunda, pelabuhan antre, cuaca menutup jalur — itu terjadi di bisnis ini. '
    'Yang bisa kami janjikan: Anda tahu dari kami, bukan dari pelanggan Anda sendiri.',
    'Delayed vessels, port queues, weather closures — these happen in this business. What we '
    'promise is that you hear it from us, not from your own customer.')),
  (('Harga yang bisa dibaca', 'Pricing you can read'),
   ('Penawaran kami memisahkan ongkos angkut, penanganan, dokumen, dan biaya pelabuhan. '
    'Anda tahu yang mana bisa ditekan dan yang mana tidak.',
    'Our quotes separate freight, handling, documentation and port charges, so you can see '
    'which costs can be reduced and which cannot.')),
],

'tanya_atas':  ('TANYA JAWAB', 'FAQ'),
'tanya_judul': ('Yang paling sering ditanyakan.', 'The questions we get most.'),
'tanya': [
  (('Berapa lama penawaran keluar?', 'How soon will I get a quote?'),
   ('Dalam 1x24 jam kerja untuk rute yang kami layani rutin. Untuk tujuan yang perlu kami '
    'tanyakan ke mitra dulu, biasanya dua hari kerja, dan kami kabari kalau akan lebih lama.',
    'Within one working day for routes we run regularly. For destinations we need to check '
    'with partners first it is usually two working days, and we tell you if it will take longer.')),
  (('Apa saja yang perlu saya siapkan untuk minta penawaran?', 'What do you need from me to quote?'),
   ('Asal dan tujuan, jenis barang, berat dan volume atau dimensi per koli, serta tanggal '
    'siap kirim. Untuk ekspor-impor, tambahkan incoterm dan nilai barang.',
    'Origin and destination, the commodity, weight and volume or dimensions per package, and '
    'your ready date. For cross-border shipments, add the incoterm and the cargo value.')),
  (('Apakah bisa menjemput barang di luar Bali?', 'Can you collect cargo outside Bali?'),
   ('Bisa. Basis kami di Badung, tetapi penjemputan di Jawa, Lombok, dan kota-kota besar '
    'lain kami kerjakan lewat jaringan mitra.',
    'Yes. We are based in Badung, but we arrange pickup in Java, Lombok and other major '
    'cities through our partner network.')),
  (('Bagaimana kalau barang rusak atau hilang?', 'What if cargo is damaged or lost?'),
   ('Tanggung jawab pengangkut diatur dalam dokumen pengangkutan dan nilainya terbatas. '
    'Untuk barang bernilai tinggi kami sarankan asuransi muatan, dan kami bantu mengurusnya '
    'sebelum barang berangkat.',
    'A carrier’s liability is set by the transport document and is capped. For high-value '
    'goods we recommend cargo insurance, and we arrange it before the shipment moves.')),
  (('Bisakah mengirim barang berbahaya atau yang perlu suhu dingin?',
    'Can you handle dangerous goods or temperature-controlled cargo?'),
   ('Tanyakan lebih dulu dengan menyebutkan jenis barangnya. Keduanya punya aturan dan '
    'batasan tersendiri per moda, dan kami akan bilang terus terang kalau tidak bisa.',
    'Ask us first and name the commodity. Both have their own rules and limits per mode, and '
    'we will say plainly if we cannot take it.')),
  (('Apakah ada minimum pengiriman?', 'Is there a minimum shipment size?'),
   ('Tidak ada minimum untuk muatan gabungan. Untuk FTL dan FCL, perhitungannya per '
    'kendaraan atau per kontainer, sehingga lebih masuk akal mulai dari volume tertentu — '
    'kami akan jujur mana yang lebih murah untuk Anda.',
    'There is no minimum for consolidated cargo. FTL and FCL are priced per vehicle or per '
    'container, so they make sense from a certain volume up — we will tell you honestly which '
    'is cheaper for you.')),
],

'form_atas':  ('MULAI SEKARANG', 'GET STARTED'),
'form_judul': ('Siap mengirim kargo Anda?', 'Ready to ship your cargo?'),
'form_sub':   ('Isi detailnya sekali, dan kami balas dengan penawaran dalam 1x24 jam kerja. '
               'Makin lengkap, makin sedikit bolak-balik.',
               'Fill in the details once and we reply with a quote within one working day. '
               'The more complete, the less back and forth.'),
'f_nama':     ('Nama', 'Name'),
'f_firma':    ('Perusahaan', 'Company'),
'f_email':    ('Email', 'Email'),
'f_telp':     ('Telepon / WhatsApp', 'Phone / WhatsApp'),
'f_moda':     ('Moda', 'Mode'),
'f_moda_opt': (['Belum yakin — sarankan', 'Darat', 'Laut', 'Udara'],
               ['Not sure — advise me', 'Land', 'Sea', 'Air']),
'f_jenis':    ('Jenis muatan', 'Load type'),
'f_jenis_opt':(['Muatan gabungan (LTL / LCL)', 'Muatan penuh (FTL / FCL)', 'Belum yakin'],
               ['Consolidated (LTL / LCL)', 'Full load (FTL / FCL)', 'Not sure']),
'f_asal':     ('Kota asal', 'Origin city'),
'f_tujuan':   ('Kota tujuan', 'Destination city'),
'f_barang':   ('Jenis barang', 'Commodity'),
'f_barang_ph':('mis. suku cadang, hasil kerajinan, bahan bangunan',
               'e.g. spare parts, handicrafts, building materials'),
'f_berat':    ('Berat total (kg)', 'Total weight (kg)'),
'f_volume':   ('Volume (m³)', 'Volume (m³)'),
'f_koli':     ('Jumlah koli', 'Number of packages'),
'f_dimensi':  ('Dimensi per koli (cm)', 'Dimensions per package (cm)'),
'f_dimensi_ph':('P × L × T', 'L × W × H'),
'f_tanggal':  ('Tanggal siap kirim', 'Ready date'),
'f_incoterm': ('Incoterm (ekspor/impor)', 'Incoterm (cross-border)'),
'f_incoterm_opt':(['Tidak berlaku / domestik', 'EXW', 'FOB', 'CIF', 'DDP', 'Belum tahu'],
                  ['Not applicable / domestic', 'EXW', 'FOB', 'CIF', 'DDP', 'Not sure']),
'f_catatan':  ('Catatan tambahan', 'Anything else'),
'f_catatan_ph':('Barang mudah pecah, perlu suhu dingin, jadwal khusus, dan sebagainya',
                'Fragile goods, temperature needs, specific schedule, and so on'),
'f_wajib':    ('wajib diisi', 'required'),
'f_kirim_wa': ('Kirim lewat WhatsApp', 'Send via WhatsApp'),
'f_kirim_em': ('Kirim lewat email', 'Send via email'),
'f_kirim':    ('Kirim Permintaan', 'Submit Request'),
'f_bantu':    ('Permintaan Anda akan tersusun rapi di aplikasi pesan — Anda masih bisa '
               'memeriksanya sebelum menekan kirim.',
               'Your request is composed into a message you can still review before sending.'),
'f_kurang':   ('Lengkapi dulu bagian yang ditandai.', 'Please complete the highlighted fields.'),
'f_terkirim': ('Terima kasih. Permintaan Anda sudah kami terima dan akan dibalas dalam '
               '1x24 jam kerja.',
               'Thank you. We have your request and will reply within one working day.'),
'f_judul_pesan':('PERMINTAAN PENAWARAN KARGO', 'CARGO QUOTE REQUEST'),

'kon_judul':  ('Hubungi kami', 'Get in touch'),
'kon_telepon':('Telepon', 'Phone'),
'kon_pic':    ('Penanggung jawab', 'Your contact'),
'kon_alamat': ('Kantor', 'Office'),
'kon_jam':    ('Jam kerja', 'Office hours'),
'kon_peta':   ('Lihat di peta', 'View on map'),
'kon_legal':  ('Legalitas', 'Legal'),

'kaki_tentang':('Mitra logistik multimoda — darat, laut, dan udara — untuk rantai pasok Anda, '
                'dari Bali ke seluruh Indonesia.',
                'A multimodal logistics partner — land, sea and air — for your supply chain, '
                'from Bali across Indonesia.'),
'kaki_hak':   ('Seluruh hak cipta dilindungi.', 'All rights reserved.'),
'kaki_bahasa':('View in English', 'Lihat dalam Bahasa Indonesia'),
'kaki_ket':   ('Waktu tempuh dan jadwal yang tercantum adalah perkiraan, bukan jaminan '
               'kontraktual.',
               'Transit times and schedules shown are estimates, not contractual guarantees.'),
}
