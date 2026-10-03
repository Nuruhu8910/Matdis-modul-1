mode_manual = False
mode_otomatis = True

mode = mode_manual ^ mode_otomatis

if mode:
    print("Mode kendaraan VALID")
else:
    print("Mode kendaraan TIDAK VALID")