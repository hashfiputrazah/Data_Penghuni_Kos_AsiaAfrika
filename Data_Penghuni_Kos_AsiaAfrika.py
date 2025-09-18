# Aplikasi CRUD Data Penghuni Kos Asia Afrika

from tabulate import tabulate

# Data dummy awal
data_penghuni = [
    {"No_Kamar": "A1", "Nama": "Jason", "Gender": "Pria", "Asal_Kota": "Surabaya", "Pekerjaan": "Pegawai Swasta", "Umur": 25},
    {"No_Kamar": "A2", "Nama": "Firda", "Gender": "Wanita", "Asal_Kota": "Malang", "Pekerjaan": "Mahasiswa", "Umur": 19},
    {"No_Kamar": "A3", "Nama": "Kira", "Gender": "Wanita", "Asal_Kota": "Semarang", "Pekerjaan": "Guru", "Umur": 27},
    {"No_Kamar": "A4", "Nama": "Dyah", "Gender": "Wanita", "Asal_Kota": "Cirebon", "Pekerjaan": "PNS", "Umur": 26},
    {"No_Kamar": "A5", "Nama": "Jafar", "Gender": "Pria", "Asal_Kota": "Jakarta", "Pekerjaan": "Insinyur", "Umur": 20},
    {"No_Kamar": "B1", "Nama": "Dany", "Gender": "Pria", "Asal_Kota": "Jakarta", "Pekerjaan": "Mahasiswa", "Umur": 19},
    {"No_Kamar": "B2", "Nama": "Firda", "Gender": "Wanita", "Asal_Kota": "Bogor", "Pekerjaan": "Dokter", "Umur": 30},
    {"No_Kamar": "B3", "Nama": "Abyan", "Gender": "Pria", "Asal_Kota": "Tangerang", "Pekerjaan": "Mahasiswa", "Umur": 18},
    {"No_Kamar": "B4", "Nama": "Putri", "Gender": "Wanita", "Asal_Kota": "Medan", "Pekerjaan": "Dosen", "Umur": 35},
    {"No_Kamar": "B5", "Nama": "Zia", "Gender": "Pria", "Asal_Kota": "Palembang", "Pekerjaan": "Pedagang", "Umur": 19}
]

# Fungsi untuk menampilkan menu utama
def menu_utama():
    print("===========Data Penghuni Kos Asia Afrika===========")
    print("1. Lihat Data Penghuni")
    print("2. Menambahkan Data Penghuni")
    print("3. Mengubah Data Penghuni")
    print("4. Menghapus Data Penghuni")
    print("5. Exit")

# Fungsi untuk menampilkan semua data dengan tabulate
def tampilkan_data():
    if len(data_penghuni) == 0:
        print("*******Tidak ada Data Penghuni*******")
    else:
        tabel = []
        for i, d in enumerate(data_penghuni, start=1):
            tabel.append([i, d["No_Kamar"], d["Nama"], d["Gender"], d["Asal_Kota"], d["Pekerjaan"], d["Umur"]])
        print(tabulate(tabel, headers=["No", "No_Kamar", "Nama", "Gender", "Asal_Kota", "Pekerjaan", "Umur"], tablefmt="grid"))

# ---------------- READ ----------------
def read_data():
    while True:
        print("+++++++++Lihat Data Penghuni+++++++++")
        print("1. Lihat Seluruh Data Penghuni")
        print("2. Lihat Data Tertentu")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Silakan Pilih Menu Read Data [1-3] : ")
        
        if pilihan == "1":
            tampilkan_data()

        elif pilihan == "2":
            no_kamar = input("Masukkan No_Kamar : ").upper()
            found = False
            for d in data_penghuni:
                if d["No_Kamar"].upper() == no_kamar:
                    print(f"Data penghuni dengan No_Kamar : {no_kamar}")
                    tampilkan_data_tertentu(d)
                    found = True
            if not found:
                print(f"Data penghuni dengan No_Kamar : {no_kamar}")
                print("*******Tidak ada Data Penghuni*******")

        elif pilihan == "3":
            break
        else:
            continue

def tampilkan_data_tertentu(d):
    tabel = [[d["No_Kamar"], d["Nama"], d["Gender"], d["Asal_Kota"], d["Pekerjaan"], d["Umur"]]]
    print(tabulate(tabel, headers=["No_Kamar", "Nama", "Gender", "Asal_Kota", "Pekerjaan", "Umur"], tablefmt="grid"))

# ---------------- CREATE ----------------
def create_data():
    while True:
        print("+++++++++Menambahkan Data Penghuni+++++++++")
        print("1. Tambah Data Penghuni")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Silakan Pilih Menu Create Data [1-2] : ")

        if pilihan == "1":
            no_kamar = input("Masukkan No_Kamar : ").upper()
            # cek duplikasi
            if any(d["No_Kamar"].upper() == no_kamar for d in data_penghuni):
                print("Data Sudah Ada")
                continue

            nama = input("Masukkan Nama : ")
            gender = input("Masukkan Gender (Pria/Wanita): ").capitalize()
            if gender not in ["Pria", "Wanita"]:
                print("*******Input Gender salah*******")
                continue
            asal = input("Masukkan Asal Kota : ")
            pekerjaan = input("Masukkan Pekerjaan : ")

            umur_input = input("Masukkan Umur : ")
            if not umur_input.isdigit():
                print("*******Umur harus angka*******")
                continue
            umur = int(umur_input)

            while True:
                konfirmasi = input("Apakah Data akan disimpan? (Y/N) : ").lower()
                if konfirmasi == "y":
                    data_penghuni.append({
                        "No_Kamar": no_kamar,
                        "Nama": nama,
                        "Gender": gender,
                        "Asal_Kota": asal,
                        "Pekerjaan": pekerjaan,
                        "Umur": umur
                    })
                    print("Data berhasil disimpan")
                    break
                elif konfirmasi == "n":
                    print("Data tidak disimpan")
                    break
                else:
                    continue

        elif pilihan == "2":
            break
        else:
            continue

# ---------------- UPDATE ----------------
def update_data():
    while True:
        print("+++++++++Mengubah Data Penghuni+++++++++")
        print("1. Ubah Data Penghuni")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Silakan Pilih Menu Update Data [1-2] : ")

        if pilihan == "1":
            no_kamar = input("Masukkan No_Kamar : ").upper()
            for d in data_penghuni:
                if d["No_Kamar"].upper() == no_kamar:
                    tampilkan_data_tertentu(d)
                    while True:
                        konfirmasi = input("Apakah Data akan diubah? (Y/N) : ").lower()
                        if konfirmasi == "y":
                            kolom = input("Masukkan kolom yang ingin diubah (Nama/Gender/Asal_Kota/Pekerjaan/Umur): ").capitalize()
                            if kolom not in d:
                                print("Kolom tidak ditemukan")
                                break
                            nilai_baru = input(f"Masukkan {kolom} Baru : ")
                            if kolom == "Umur":
                                if not nilai_baru.isdigit():
                                    print("*******Umur harus angka*******")
                                    break
                                nilai_baru = int(nilai_baru)
                            if kolom == "Gender":
                                nilai_baru = nilai_baru.capitalize()
                                if nilai_baru not in ["Pria", "Wanita"]:
                                    print("*******Input Gender salah*******")
                                    break
                            d[kolom] = nilai_baru
                            print("Data berhasil diubah")
                            break
                        elif konfirmasi == "n":
                            print("Data tidak terupdate")
                            break
                        else:
                            continue
                    break
            else:
                print("*******Tidak ada Data Penghuni*******")

        elif pilihan == "2":
            break
        else:
            continue

# ---------------- DELETE ----------------
def delete_data():
    while True:
        print("+++++++++Menghapus Data Penghuni+++++++++")
        print("1. Hapus Data Penghuni")
        print("2. Kembali ke Menu Utama")
        pilihan = input("Silakan Pilih Menu Hapus Data [1-2] : ")

        if pilihan == "1":
            no_kamar = input("Masukkan No_Kamar : ").upper()
            for i, d in enumerate(data_penghuni):
                if d["No_Kamar"].upper() == no_kamar:
                    tampilkan_data_tertentu(d)
                    while True:
                        konfirmasi = input("Apakah Data akan dihapus? (Y/N) : ").lower()
                        if konfirmasi == "y":
                            data_penghuni.pop(i)
                            print("Data berhasil dihapus")
                            break
                        elif konfirmasi == "n":
                            print("Data Tidak Terhapus")
                            break
                        else:
                            continue
                    break
            else:
                print("*******Tidak ada Data Penghuni*******")

        elif pilihan == "2":
            break
        else:
            continue

# ---------------- MAIN PROGRAM ----------------
while True:
    menu_utama()
    pilihan = input("Silakan Pilih Main Menu [1-5] : ")
    
    if pilihan == "1":
        read_data()
    elif pilihan == "2":
        create_data()
    elif pilihan == "3":
        update_data()
    elif pilihan == "4":
        delete_data()
    elif pilihan == "5":
        print("Terima kasih, anda telah keluar dari program…")
        break
    else:
        print("*******Maaf angka yang anda masukkan salah*******")