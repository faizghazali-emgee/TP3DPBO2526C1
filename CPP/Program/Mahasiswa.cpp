#ifndef MAHASISWA_CPP
#define MAHASISWA_CPP

#include "Manusia.cpp"

// Turunan 1 dari Manusia (Hierarchical)
class Mahasiswa : public Manusia {
private:
    string nim;
    string fakultas;
    string prodi;
    int semester;

public:
    Mahasiswa() : Manusia(), semester(1) {}
    Mahasiswa(string n, string id_nik, string tempat_tgl, string jk,
                string id_nim, string fak, string prd, int smt)
        : Manusia(n, id_nik, tempat_tgl, jk), nim(id_nim), fakultas(fak), prodi(prd), semester(smt) {}

    string getNim() const { return nim; }
    void setNim(string id_nim) { nim = id_nim; }

    string getFakultas() const { return fakultas; }
    void setFakultas(string fak) { fakultas = fak; }

    string getProdi() const { return prodi; }
    void setProdi(string prd) { prodi = prd; }

    int getSemester() const { return semester; }
    void setSemester(int smt) { semester = smt; }

    void tampilkanProfil() const override {
        cout << "[ PROFIL MAHASISWA ]" << endl;
        Manusia::tampilkanProfil();
        cout << "NIM           : " << nim << endl;
        cout << "Fakultas      : " << fakultas << endl;
        cout << "Program Studi : " << prodi << endl;
        cout << "Semester      : " << semester << endl;
    }
};

#endif // MAHASISWA_CPP