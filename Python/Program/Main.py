# Main.py

from Mahasiswa import Mahasiswa
from Dosen import Dosen
from BimbinganSkripsi import BimbinganSkripsi

def tampilkan_semua_data(list_bimbingan: list, jumlah_data: int):
    if jumlah_data == 0:
        print("[ Data bimbingan masih kosong ]")
        return
    
    for i in range(jumlah_data):
        print(f"\n>>> Data Bimbingan Ke-{i + 1} <<<")
        list_bimbingan[i].cetak_kartu()

def main():
    MAX_KAPASITAS = 10
    list_bimbingan = [None] * MAX_KAPASITAS  # Array of Objects
    jumlah_data = 0

    # --- 1. INISIALISASI DATA AWAL (STATIS) ---
    m1 = Mahasiswa("Budi Santoso", "320101010101", "Bandung, 10 Mei 2002", "Laki-laki", "2205001", "FPMIPA", "Ilmu Komputer", 7)
    d1 = Dosen("Dr. Hendra Wijaya", "320102020202", "Jakarta, 15 Agustus 1980", "Laki-laki", "19800815200501", "PBO", 12000000)

    m2 = Mahasiswa("Siti Aminah", "320101020202", "Surabaya, 12 April 2003", "Perempuan", "2205002", "FPMIPA", "MIPA Utama", 7)
    d2 = Dosen("Dr. Rina Maryana", "320102030303", "Bandung, 20 Des 1985", "Perempuan", "19851220201002", "Basis Data", 11500000)

    list_bimbingan[jumlah_data] = BimbinganSkripsi("BIM-2026-001", "Rancang Bangun Sistem Presensi QR Code", m1, d1, "Perbaiki bab 3")
    jumlah_data += 1

    list_bimbingan[jumlah_data] = BimbinganSkripsi("BIM-2026-002", "Analisis Sentimen Twitter Menggunakan NLP", m2, d2, "ACC Judul, lanjut Bab 1")
    jumlah_data += 1

    # --- 2. PRINT DATA SEBELUM DITAMBAHKAN ---
    print("========================================================")
    print("      DAFTAR BIMBINGAN SKRIPSI      ")
    print("========================================================")
    tampilkan_semua_data(list_bimbingan, jumlah_data)

    # --- 3. PENAMBAHAN DATA BARU (STATIS) ---
    print("\n\n>>> Memproses Penambahan Data Baru... <<<")
    m3 = Mahasiswa("Ahmad Fauzi", "320101030303", "Yogyakarta, 1 Januari 2002", "Laki-laki", "2205003", "FPMIPA", "Sistem Informasi", 8)
    
    if jumlah_data < MAX_KAPASITAS:
        list_bimbingan[jumlah_data] = BimbinganSkripsi("BIM-2026-003", "Implementasi Blockchain untuk Keamanan Data", m3, d1, "Revisi Bab 2 Landasan Teori")
        jumlah_data += 1
        print("Data baru berhasil ditambahkan!")

    # --- 4. PRINT DATA SESUDAH DITAMBAHKAN ---
    print("\n========================================================")
    print("      DAFTAR BIMBINGAN SKRIPSI     ")
    print("========================================================")
    tampilkan_semua_data(list_bimbingan, jumlah_data)

if __name__ == "__main__":
    main()