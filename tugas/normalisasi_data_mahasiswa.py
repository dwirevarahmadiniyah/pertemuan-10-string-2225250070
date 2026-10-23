
def normalisasi_nama(nama):
    return nama.strip().title()


def buat_inisial(nama):
    kata = nama.strip().split()
    inisial = ""

    for k in kata:
        inisial += k[0].upper()

    return inisial


def normalisasi_kode(kode):
    return kode.strip().upper().replace(" ", "")


nama = input("Nama: ")
kode = input("Kode kelas : ")

# Tampilkan hasil normalisasi
print("\n=== HASIL NORMALISASI ===")
print("Nama normal  :", normalisasi_nama(nama))
print("Inisial      :", buat_inisial(nama))
print("Kode kelas   :", normalisasi_kode(kode))
