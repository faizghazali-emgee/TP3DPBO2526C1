#ifndef DOSEN_CPP
#define DOSEN_CPP

#include <iomanip>
#include "Manusia.cpp"

// Turunan 2 dari Manusia (Hierarchical)
class Dosen : public Manusia {
private:
    string nip;
    string mataKuliah;
    double gaji;

public:
    Dosen() : Manusia(), gaji(0.0) {}
    Dosen(string n, string id_nik, string tempat_tgl, string jk,
            string id_nip, string mk, double g)
        : Manusia(n, id_nik, tempat_tgl, jk), nip(id_nip), mataKuliah(mk), gaji(g) {}

    string getNip() const { return nip; }
    void setNip(string id_nip) { nip = id_nip; }

    string getMataKuliah() const { return mataKuliah; }
    void setMataKuliah(string mk) { mataKuliah = mk; }

    double getGaji() const { return gaji; }
    void setGaji(double g) { gaji = g; }

    void tampilkanProfil() const override {
        cout << "[ PROFIL DOSEN ]" << endl;
        Manusia::tampilkanProfil();
        cout << "NIP           : " << nip << endl;
        cout << "Mata Kuliah   : " << mataKuliah << endl;
        cout << "Gaji          : Rp " << fixed << setprecision(0) << gaji << endl;
    }
};

#endif // DOSEN_CPP