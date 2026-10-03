### 1. akses_wifi.py (Logika OR)
| akun_mahasiswa | akun_dosen | Luaran Program | Keterangan |
| :---: | :---: | :---: | :--- |
| True | False | Akses WiFi DITERIMA | PASS |
| True | True | Akses WiFi DITERIMA | PASS |
| False | True |  Akses WiFi DITERIMA | PASS |
| False | False | Akses WiFi DITOLAK| PASS |

### 2. beasiswa.py (Logika AND)
| ipk_memenuhi | aktif_organisasi | penghasilan_memenuhi | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- |
| True | True | True | Mahasiswa mendapat beasiswa | PASS |
| True | True | False | Mahasiswa TIDAK mendapat beasiswa | PASS |
| True | False | True | Mahasiswa TIDAK mendapat beasiswa | PASS |
| False | False | False | Mahasiswa TIDAK mendapat beasiswa | PASS |

### 3. kelulusan.py (Logika AND)
| nilai_teori | nilai_praktik | kehadiran | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- |
| True | True | True | Mahasiswa LULUS | PASS |
| True | True | False | Mahasiswa TIDAK LULUS | PASS |
| True | False | True | Mahasiswa TIDAK LULUS | PASS |
| False | False | False | Mahasiswa TIDAK LULUS | PASS |

### 4. kendaraan.py (Logika XOR)
| mode_manual | mode_otomatis | Luaran Program | Keterangan |
| :---: | :---: | :---: | :--- |
| True | False | Mode kendaraan valid | PASS |
| True | True | Mode kendaraan TIDAK valid | PASS |
| False | True | Mode kendaraan valid | PASS |
| False | False | Mode kendaraan TIDAK valid | PASS |

### 5. login.py (Logika AND)
| username_benar | pasword_benar | akun_aktif | Luaran Program | Keterangan |
| :---: | :---: | :---: | :---: | :--- |
| True | True | True | Login BERHASIL | PASS |
| True | True | False | Login GAGAL | PASS |
| True | False | True | Login GAGAL | PASS |
| False | False | False | Login GAGAL | PASS |

### 6. pembayaran.py (Logika XOR)
| transfer_bank | e_wallet | Luaran Program | Keterangan |
| :---: | :---: | :---: | :--- |
| True | False | pembayaran DITERIMA | PASS |
| True | True | pilihan pembayaran tidak valid  | PASS |
| False | True | pembayaran DITERIMA | PASS |
| False | False | pilihan pembayaran tidak valid | PASS |


### 7. prioritas_seleksi.py (Logika OR)
| pengalaman | sertifikat | Luaran Program | Keterangan |
| :---: | :---: | :---: | :--- |
| True | False | peserta mendapat PRIORITAS | PASS |
| True | True | peserta mendapat PRIORITAS | PASS |
| False | True |  peserta mendapat PRIORITAS | PASS |
| False | False | peserta TIDAK mendapat PRIORITAS| PASS |

### 8. ujian_susulan.py (Logika OR)
| sakit | keperluan_keluarga | Luaran Program | Keterangan |
| :---: | :---: | :---: | :--- |
| True | False | Boleh mengikuti ujian susulan | PASS |
| True | True | Boleh mengikuti ujian susulan | PASS |
| False | True |  Boleh mengikuti ujian susulan | PASS |
| False | False | TIDAK Boleh mengikuti ujian susulan| PASS |

## Tabel Rekapitulasi Hasil Uji
| No | Studi Kasus                 |  AND |  OR  |  XOR | Hasil Utama             |
| -: | --------------------------- | :--: | :--: | :--: | ----------------------- |
|  1 | Akses wifi             | True | True | True | **Akses WiFi diterima**               |
|  2 | Beasiswa            | True | True | True | **Mahasiswa MENDAPAT beasiswa**               |
|  3 | Kelulusan          | True | True | True | **Mahasiswa LULUS**         |
|  4 | Kendaraan | True | True | True | **Mode kendaraan VALID**            |
|  5 | Login       | True | True | True | **Login BERHASIL** |
|  6 | Pembayaran             | True | True | True | **Pembayaran DITERIMA**     |
|  7 | Prioritas seleksi         | True | True | True | **Peserta mendapat PRIORITAS**          |
|  8 | Ujian susulan           | True | True | True | **Boleh mengikuti ujian susulan**     |

#### Kesimpulan Pengujian
Berdasarkan tabel pengujian, seluruh 8 studi kasus menerapkan tiga jenis logika Boolean:

* AND (and) untuk menentukan syarat utama yang harus dipenuhi secara bersamaan.
* OR (or) untuk menentukan kondisi alternatif, yaitu cukup salah satu kondisi terpenuhi.
* XOR (^) untuk menentukan apakah hanya salah satu dari dua kondisi yang terpenuhi.
