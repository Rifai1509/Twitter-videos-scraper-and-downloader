# Twitter-videos-scraper-and-downloader

1. Inspeksi halaman target
2. Cari url dengan mengetik kata2 di status melalui network
3. Cek request header, disana ada guest token yang harus di isikan ke file json headers.json
4. Jalankan step 1 untuk mendapatkan end cursor (untuk pagination) agar bisa dapat berapapun data semaunya
5. Jalabkan step 2 untuk mendapatkan url video. Bisa ganti ukuran video sesuai keinginan dengan mengedit variabel list video url
6. Jalankan step 3, bisa atur berapa video yang akan di download
