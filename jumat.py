pilihan  = "y"
while pilihan=="y":
    print("""ITA TEH ORIGINAL
    
    List Menu Minuman TEH 
    ==============================
    1. ES Teh Susu    : Rp 11.000
    2. ES Teh Coklat  : Rp 12.000
    3. ES Teh Manis   : Rp 11.000
    4. Es Teh Campur  : Rp 14.000
    5. ES Teh Hitam   : Rp 18.000
    ==============================
    """)
    pesan=str(input("masukkan list nomor  menu teh ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "1":
        listnama= "ES Teh Susu"
        harga=(11000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "2":
        listnama= "ES Teh Coklat"
        harga = (12000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "3":
        listnama= "ES Teh Manis"
        harga=int(11000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "4":
        listnama= "ES Teh Campur"
        harga=int(14000*jumlahpesan)
        ppn = int(harga * 0.1)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan nomor menu yang tersedia silahkan ulangi kembali YA/TIDAK =")
 
    print("--------------------------")
    print("ITA TEH ORIGINAL")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali YA/TIDAK =")
  
    