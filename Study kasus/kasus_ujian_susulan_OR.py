sakit = False
keperluan_keluarga = False

ujian_susulan = sakit or keperluan_keluarga

if ujian_susulan:
    print("Boleh mengikuti ujian susulan")
else:
    print("Tidak boleh mengikuti ujian susulan")