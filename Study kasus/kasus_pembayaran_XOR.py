transfer_bank = True
e_wallet = True

pembayaran = transfer_bank ^ e_wallet

if pembayaran:
    print("Pembayaran DITERIMA")
else:
    print("Pilihan pembayaran TIDAK VALID")