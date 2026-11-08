/* ══════════════════════════════════════════════════════════════════════
   Naratama Adya Dewata

   Tiga pekerjaan: ticker berita, menu layar kecil, dan formulir penawaran
   yang BENAR-BENAR mengirim. Versi sebelumnya hanya menampilkan ucapan
   terima kasih lalu mengosongkan isian -- setiap permintaan yang masuk
   sejak situs itu hidup, hilang tanpa jejak, dan pengunjung diberi tahu
   bahwa semuanya baik-baik saja.
   ══════════════════════════════════════════════════════════════════════ */
'use strict';

var CFG = window.NARATAMA || {};
var $ = function (id) { return document.getElementById(id); };

/* ───────────────────────── 1. TICKER BERITA ─────────────────────────
   Beritanya ada di berita.json, bukan di dalam kode. Menambah satu berita
   = menambah satu baris di berkas itu, tanpa menyentuh halaman.

   Yang paling penting di sini: TICKER MENYEMBUNYIKAN DIRINYA SENDIRI
   kalau berita terbarunya sudah lewat UMUR_MAKS hari. Ticker berisi
   berita bulan Maret yang dibaca orang bulan Desember membuat situs
   terbaca terbengkalai -- lebih merugikan daripada tidak ada ticker sama
   sekali. Lebih baik dia diam daripada mempermalukan. */
var UMUR_MAKS = 45;   /* hari */

function tanggalPendek(iso, lang) {
  var d = new Date(iso + 'T00:00:00');
  if (isNaN(d)) return '';
  var bln = (lang === 'en')
    ? ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    : ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agu','Sep','Okt','Nov','Des'];
  return d.getDate() + ' ' + bln[d.getMonth()];
}

function pasangTicker(daftar) {
  var kotak = $('ticker'), jalur = $('ticker-jalur');
  if (!kotak || !jalur || !daftar || !daftar.length) return;

  daftar = daftar.filter(function (b) { return b && b.judul && b.tanggal; });
  daftar.sort(function (a, b) { return a.tanggal < b.tanggal ? 1 : -1; });
  if (!daftar.length) return;

  var umur = (Date.now() - new Date(daftar[0].tanggal + 'T00:00:00')) / 86400000;
  if (!(umur >= 0) || umur > UMUR_MAKS) return;   /* diam, bukan basi */

  var lang = CFG.lang || 'id';
  function butir(b) {
    var a = document.createElement('a');
    if (b.tautan) { a.href = b.tautan; a.target = '_blank'; a.rel = 'noopener nofollow'; }
    var tg = document.createElement('span');
    tg.className = 'ticker-tgl'; tg.textContent = tanggalPendek(b.tanggal, lang);
    var jd = document.createElement('span'); jd.textContent = b.judul;
    a.appendChild(tg); a.appendChild(jd);
    if (b.sumber) {
      var s = document.createElement('span');
      s.className = 'ticker-sumber'; s.textContent = b.sumber;
      a.appendChild(s);
    }
    return a;
  }
  /* Isinya digandakan supaya gulungannya menyambung mulus di tengah
     (keyframe bergeser tepat -50%). */
  for (var putaran = 0; putaran < 2; putaran++) {
    daftar.forEach(function (b) { jalur.appendChild(butir(b)); });
  }
  kotak.hidden = false;

  var tbl = $('ticker-jeda');
  if (tbl) {
    tbl.addEventListener('click', function () {
      var henti = jalur.classList.toggle('henti');
      tbl.textContent = henti ? '▶' : '❚❚';
      tbl.setAttribute('aria-label', henti ? tbl.dataset.jalan : tbl.dataset.jeda);
    });
  }
  /* Berhenti saat disentuh/diarahkan, supaya judulnya bisa dibaca. */
  jalur.addEventListener('mouseenter', function () { jalur.classList.add('henti'); });
  jalur.addEventListener('mouseleave', function () {
    if ($('ticker-jeda').textContent !== '▶') jalur.classList.remove('henti');
  });
}

fetch('berita.json', { cache: 'no-cache' })
  .then(function (r) { return r.ok ? r.json() : null; })
  .then(function (j) { if (j) pasangTicker(j.berita || j); })
  .catch(function () { /* ticker tetap tersembunyi -- halaman tidak terganggu */ });

/* ───────────────────────── 2. MENU LAYAR KECIL ───────────────────────── */
(function () {
  var tbl = $('menu-tbl'), nav = $('nav');
  if (!tbl || !nav) return;
  tbl.addEventListener('click', function () {
    var buka = nav.classList.toggle('buka');
    tbl.setAttribute('aria-expanded', buka ? 'true' : 'false');
  });
  nav.addEventListener('click', function (ev) {
    if (ev.target.tagName === 'A') {
      nav.classList.remove('buka');
      tbl.setAttribute('aria-expanded', 'false');
    }
  });
  document.addEventListener('keydown', function (ev) {
    if (ev.key === 'Escape' && nav.classList.contains('buka')) {
      nav.classList.remove('buka');
      tbl.setAttribute('aria-expanded', 'false');
      tbl.focus();
    }
  });
})();

/* ───────────────────────── 3. FORMULIR PENAWARAN ─────────────────────────
   Tanpa server, ada tiga jalan keluar, dan ketiganya dipakai sesuai apa
   yang sudah diisi di isi.py:

     Formspree  -- kalau alamat endpoint-nya diisi. Permintaan masuk ke
                   email dan tercatat, pengunjung tidak berpindah halaman.
     WhatsApp   -- kalau nomornya diisi. Untuk B2B di Indonesia ini jalur
                   yang paling sering benar-benar dipakai orang, dan
                   pesannya tersusun rapi sebelum dikirim.
     Email      -- jalan terakhir, lewat aplikasi email pengunjung.

   Yang tidak akan terjadi lagi: halaman mengucapkan terima kasih padahal
   tidak ada apa pun yang terkirim ke mana pun. */
(function () {
  var form = $('form-penawaran');
  if (!form) return;
  var galat = $('form-galat'), sukses = $('form-sukses');
  var L = CFG.label || {};

  var URUT = ['nama','firma','email','telp','moda','jenis','asal','tujuan','barang',
              'berat','volume','koli','dimensi','tanggal','incoterm','catatan'];

  function nilai(n) {
    var el = form.elements[n];
    return el ? String(el.value || '').trim() : '';
  }

  function periksa() {
    var kurang = [];
    ['nama','telp','asal','tujuan','barang'].forEach(function (n) {
      var el = form.elements[n];
      if (!el) return;
      var kosong = !nilai(n);
      el.closest('.isian').classList.toggle('kurang', kosong);
      if (kosong) kurang.push(el);
    });
    if (kurang.length) {
      galat.hidden = false;
      kurang[0].focus();
      return false;
    }
    galat.hidden = true;
    return true;
  }

  function susunPesan() {
    var baris = [CFG.judulPesan || 'PERMINTAAN PENAWARAN', ''];
    URUT.forEach(function (n) {
      var v = nilai(n);
      if (!v) return;
      baris.push((L[n] || n) + ': ' + v);
    });
    return baris.join('\n');
  }

  function kirimWa() {
    var url = 'https://wa.me/' + CFG.wa + '?text=' + encodeURIComponent(susunPesan());
    window.open(url, '_blank', 'noopener');
    tampilSukses();
  }

  function kirimEmail() {
    var subjek = (CFG.judulPesan || 'Quote request') + ' — ' + (nilai('asal') || '') +
                 ' → ' + (nilai('tujuan') || '');
    var ke = CFG.email || '';
    window.location.href = 'mailto:' + ke + '?subject=' + encodeURIComponent(subjek) +
                           '&body=' + encodeURIComponent(susunPesan());
    tampilSukses();
  }

  function kirimFormspree() {
    var data = new FormData(form);
    fetch(CFG.formspree, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
      .then(function (r) {
        if (!r.ok) throw new Error('gagal');
        tampilSukses(); form.reset();
      })
      .catch(function () {
        /* Jangan berpura-pura berhasil. Alihkan ke jalur yang pasti sampai. */
        if (CFG.wa) kirimWa(); else kirimEmail();
      });
  }

  function tampilSukses() {
    sukses.hidden = false;
    sukses.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    if (!periksa()) return;
    if (CFG.formspree) kirimFormspree();
    else if (CFG.wa)   kirimWa();
    else               kirimEmail();
  });

  var tblEmail = form.querySelector('[data-lewat="email"][type="button"]');
  if (tblEmail) {
    tblEmail.addEventListener('click', function () { if (periksa()) kirimEmail(); });
  }

  /* Tanda "kurang" dihapus begitu isiannya diperbaiki -- bukan menunggu
     tombol ditekan lagi. */
  form.addEventListener('input', function (ev) {
    var bungkus = ev.target.closest && ev.target.closest('.isian');
    if (bungkus && ev.target.value.trim()) bungkus.classList.remove('kurang');
  });
})();
