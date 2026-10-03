nilai_teori = True
nilai_praktik = True
kehadiran = True

lulus = nilai_teori and nilai_praktik and kehadiran

if lulus:
    print("Mahasiswa LULUS")
else:
    print("Mahasiswa TIDAK LULUS")