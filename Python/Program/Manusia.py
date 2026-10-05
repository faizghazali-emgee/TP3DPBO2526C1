# Manusia.py

class Manusia:
    """Base Class untuk Hierarchical Inheritance.

    Menyimpan atribut umum yang dimiliki semua manusia (nama, NIK, TTL, jenis kelamin).
    Class Mahasiswa dan Dosen akan mewarisi class ini.
    """
    def __init__(self, nama: str = "", nik: str = "", ttl: str = "", jenis_kelamin: str = ""):
        # Atribut diberi satu underscore (protected) agar bisa diakses oleh class turunan
        self._nama = nama
        self._nik = nik
        self._ttl = ttl
        self._jenis_kelamin = jenis_kelamin

    # Getter & Setter
    def get_nama(self) -> str:
        return self._nama

    def set_nama(self, nama: str):
        self._nama = nama

    def get_nik(self) -> str:
        return self._nik

    def set_nik(self, nik: str):
        self._nik = nik

    def get_ttl(self) -> str:
        return self._ttl

    def set_ttl(self, ttl: str):
        self._ttl = ttl

    def get_jenis_kelamin(self) -> str:
        return self._jenis_kelamin

    def set_jenis_kelamin(self, jenis_kelamin: str):
        self._jenis_kelamin = jenis_kelamin

    def tampilkan_profil(self):
        print(f"Nama          : {self._nama}")
        print(f"NIK           : {self._nik}")
        print(f"TTL           : {self._ttl}")
        print(f"Jenis Kelamin : {self._jenis_kelamin}")