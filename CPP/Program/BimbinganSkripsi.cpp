#ifndef BIMBINGANSKRIPSI_CPP
#define BIMBINGANSKRIPSI_CPP

#include "Mahasiswa.cpp"
#include "Dosen.cpp"

// Menggunakan Composition (Mahasiswa & Dosen dimiliki secara utuh oleh BimbinganSkripsi)
class BimbinganSkripsi {
private:
    string idBimbingan;
    string judulSkripsi;
    string catatan;
    Mahasiswa mhs;          // Composition
    Dosen dsnPembimbing;    // Composition

public:
    BimbinganSkripsi() : idBimbingan("-"), judulSkripsi("-"), catatan("-") {}
    
    BimbinganSkripsi(string id, string judul, const Mahasiswa& m, const Dosen& d, string c = "Belum ada revisi")
        : idBimbingan(id), judulSkripsi(judul), mhs(m), dsnPembimbing(d), catatan(c) {}

    string getIdBimbingan() const { return idBimbingan; }
    string getJudulSkripsi() const { return judulSkripsi; }
    string getCatatan() const { return catatan; }

    void setJudulSkripsi(string judul) { judulSkripsi = judul; }
    void setCatatan(string txt) { catatan = txt; }

    void cetakKartu() const {
        cout << "\n======================================================\n";
        cout << " KARTU KONTROL BIMBINGAN SKRIPSI | ID: " << idBimbingan << endl;
        cout << "======================================================\n";
        cout << "Judul Skripsi : " << judulSkripsi << endl;
        cout << "------------------------------------------------------\n";
        cout << "MAHASISWA:\n";
        mhs.tampilkanProfil();
        cout << "------------------------------------------------------\n";
        cout << "DOSEN PEMBIMBING:\n";
        dsnPembimbing.tampilkanProfil();
        cout << "------------------------------------------------------\n";
        cout << "Catatan Revisi: " << catatan << endl;
        cout << "======================================================\n";
    }
};

#endif // BIMBINGANSKRIPSI_CPP