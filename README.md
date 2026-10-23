# Pertemuan 10 – String dan Pengolahan Teks

**Nama:** Dwi Reva Rahmadiniyah  
**NIM:** 2225250070 
**Kelas:** 3E

**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika FKIP Universitas Sultan Ageng Tirtayasa  
**Tahun Akademik:** 2026/2027 Ganjil

## Tujuan

Mengolah dan menormalisasi data teks menggunakan string Python agar data nama mahasiswa dan kode kelas menjadi lebih rapi, konsisten, dan mudah dibaca.

## Cara Menjalankan

Program dijalankan melalui terminal VS Code dengan langkah-langkah berikut:

1. Membuka folder proyek di VS Code.
2. Membuat file `normalisasi_data_mahasiswa.py` di dalam folder `tugas`.
3. Menuliskan kode program dan menyimpan file.
4. Membuka terminal VS Code.
5. Menjalankan perintah berikut:

   `python3 tugas/normalisasi_data_mahasiswa.py`

6. Memasukkan nama mahasiswa dan kode kelas sesuai permintaan program.
7. Melihat hasil normalisasi yang ditampilkan di terminal.

## Algoritma

Proses normalisasi data teks dilakukan melalui beberapa langkah berikut.

1. Program meminta pengguna memasukkan nama mahasiswa dan kode kelas.
2. Nama mahasiswa diproses menggunakan fungsi `strip()` untuk menghapus spasi di awal dan akhir teks, kemudian `title()` untuk membuat huruf awal setiap kata menjadi kapital.
3. Nama yang sudah dimasukkan diproses menggunakan `split()` untuk memisahkan setiap kata. Huruf pertama dari setiap kata diambil dan digabungkan menjadi inisial menggunakan perulangan.
4. Kode kelas diproses menggunakan `strip()` untuk menghapus spasi di awal dan akhir, `upper()` untuk mengubah huruf menjadi kapital, dan `replace()` untuk menghapus spasi di dalam kode.
5. Program menampilkan nama yang sudah dinormalisasi, inisial nama, dan kode kelas yang sudah diperbaiki.

## Test Case

| No. | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Nama: `  dwi reva rahmadiniyah  `; Kode: `mtk 2a` | Nama: `Dwi Reva Rahmadiniyah`; Inisial: `DRR`; Kode: `MTK2A` | Dwi Reva Rahmadiniyah; DRR; MTK2A | Berhasil |
| 2 | Nama: `andi saputra`; Kode: `ti 1b` | Nama: `Andi Saputra`; Inisial: `AS`; Kode: `TI1B` | Andi Saputra; AS; TI1B | Berhasil |
| 3 | Nama: `siti nurhaliza`; Kode: `pm 3c` | Nama: `Siti Nurhaliza`; Inisial: `SN`; Kode: `PM3C` | Siti Nurhaliza; SN; PM3C | Berhasil |

*Catatan: Hasil aktual pada tabel merupakan hasil yang diharapkan berdasarkan logika program. Jalankan program dan cocokkan kembali dengan hasil di terminal sebelum mengumpulkan laporan.*

## Refleksi

Salah satu masalah teks yang sering ditemukan adalah penulisan nama dengan huruf kapital yang tidak konsisten dan adanya spasi berlebih. Hal tersebut dapat membuat data terlihat kurang rapi dan tidak seragam. Masalah ini dapat diperbaiki menggunakan fungsi `strip()` untuk menghapus spasi di awal dan akhir teks serta `title()` untuk menyeragamkan huruf kapital pada nama. Untuk kode kelas, fungsi `upper()` dan `replace()` digunakan agar penulisannya lebih konsisten. Melalui praktikum ini, saya memahami bahwa pengolahan string dapat membantu membersihkan dan menstandarkan data sebelum digunakan lebih lanjut.
