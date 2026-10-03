ipk_memenuhi = True
aktif_organisasi = False
penghasilan_memenuhi = True

beasiswa = ipk_memenuhi and aktif_organisasi and penghasilan_memenuhi

if beasiswa:
    print("Mahasiswa MENDAPAT beasiswa")
else:
    print("Mahasiswa TIDAK mendapat beasiswa")