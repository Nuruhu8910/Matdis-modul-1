akun_mahasiswa = True
akun_dosen = True

akses_wifi = akun_mahasiswa or akun_dosen

if akses_wifi:
    print("Akses WiFi DITERIMA")
else:
    print("Akses WiFi DITOLAK")