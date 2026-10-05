#include "BimbinganSkripsi.cpp"

using namespace std;

void tampilkanSemuaData(const BimbinganSkripsi listBimbingan[], int jumlahData) {
    if (jumlahData == 0) {
        cout << "[ Data bimbingan masih kosong ]\n";
        return;
    }
    for (int i = 0; i < jumlahData; i++) {
        cout << "\n>>> Data Bimbingan Ke-" << (i + 1) << " <<<";
        listBimbingan[i].cetakKartu();
    }
}

int main() {
    const int MAX_KAPASITAS = 10;
    BimbinganSkripsi listBimbingan[MAX_KAPASITAS]; // Array of Objects
    int jumlahData = 0;

    // --- 1. INISIALISASI DATA AWAL (STATIS) ---
    Mahasiswa m1("Budi Santoso", "320101010101", "Bandung, 10 Mei 2002", "Laki-laki", "2205001", "FPMIPA", "Ilmu Komputer", 7);
    Dosen d1("Dr. Hendra Wijaya", "320102020202", "Jakarta, 15 Agustus 1980", "Laki-laki", "19800815200501", "PBO", 12000000);

    Mahasiswa m2("Siti Aminah", "320101020202", "Surabaya, 12 April 2003", "Perempuan", "2205002", "FPMIPA", "MIPA Utama", 7);
    Dosen d2("Dr. Rina Maryana", "320102030303", "Bandung, 20 Des 1985", "Perempuan", "19851220201002", "Basis Data", 11500000);

    listBimbingan[jumlahData++] = BimbinganSkripsi("BIM-2026-001", "Rancang Bangun Sistem Presensi QR Code", m1, d1, "Perbaiki bab 3");
    listBimbingan[jumlahData++] = BimbinganSkripsi("BIM-2026-002", "Analisis Sentimen Twitter Menggunakan NLP", m2, d2, "ACC Judul, lanjut Bab 1");

    // --- 2. PRINT DATA SEBELUM DITAMBAHKAN ---
    cout << "========================================================\n";
    cout << "      DAFTAR BIMBINGAN SKRIPSI      \n";
    cout << "========================================================\n";
    tampilkanSemuaData(listBimbingan, jumlahData);

    // --- 3. PENAMBAHAN DATA BARU (STATIS) ---
    cout << "\n\n>>> Memproses Penambahan Data Baru... <<<\n";
    Mahasiswa m3("Ahmad Fauzi", "320101030303", "Yogyakarta, 1 Januari 2002", "Laki-laki", "2205003", "FPMIPA", "Sistem Informasi", 8);
    
    if (jumlahData < MAX_KAPASITAS) {
        listBimbingan[jumlahData++] = BimbinganSkripsi("BIM-2026-003", "Implementasi Blockchain untuk Keamanan Data", m3, d1, "Revisi Bab 2 Landasan Teori");
        cout << "Data baru berhasil ditambahkan!\n";
    }

    // --- 4. PRINT DATA SESUDAH DITAMBAHKAN ---
    cout << "\n========================================================\n";
    cout << "      DAFTAR BIMBINGAN SKRIPSI     \n";
    cout << "========================================================\n";
    tampilkanSemuaData(listBimbingan, jumlahData);

    return 0;
}