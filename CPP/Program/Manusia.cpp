#ifndef MANUSIA_CPP
#define MANUSIA_CPP

#include <iostream>
#include <string>

using namespace std;

// Base Class untuk Hierarchical Inheritance
class Manusia {
protected:
    string nama;
    string nik;
    string ttl;
    string jenisKelamin;

public:
    Manusia(string n = "", string id_nik = "", string tempat_tgl = "", string jk = "")
        : nama(n), nik(id_nik), ttl(tempat_tgl), jenisKelamin(jk) {}

    virtual ~Manusia() {}

    // Getter & Setter
    string getNama() const { return nama; }
    void setNama(string n) { nama = n; }

    string getNik() const { return nik; }
    void setNik(string id_nik) { nik = id_nik; }

    string getTtl() const { return ttl; }
    void setTtl(string tempat_tgl) { ttl = tempat_tgl; }

    string getJenisKelamin() const { return jenisKelamin; }
    void setJenisKelamin(string jk) { jenisKelamin = jk; }

    virtual void tampilkanProfil() const {
        cout << "Nama          : " << nama << endl;
        cout << "NIK           : " << nik << endl;
        cout << "TTL           : " << ttl << endl;
        cout << "Jenis Kelamin : " << jenisKelamin << endl;
    }
};

#endif // MANUSIA_CPP