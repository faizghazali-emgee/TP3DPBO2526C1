# Dosen.py

from Manusia import Manusia

# Turunan 2 dari Manusia (Hierarchical)
class Dosen(Manusia):
    def __init__(self, nama: str = "", nik: str = "", ttl: str = "", jenis_kelamin: str = "",
                 nip: str = "", mata_kuliah: str = "", gaji: float = 0.0):
        super().__init__(nama, nik, ttl, jenis_kelamin)
        self.__nip = nip
        self.__mata_kuliah = mata_kuliah
        self.__gaji = gaji

    # Getter & Setter
    def get_nip(self) -> str:
        return self.__nip

    def set_nip(self, nip: str):
        self.__nip = nip

    def get_mata_kuliah(self) -> str:
        return self.__mata_kuliah

    def set_mata_kuliah(self, mata_kuliah: str):
        self.__mata_kuliah = mata_kuliah

    def get_gaji(self) -> float:
        return self.__gaji

    def set_gaji(self, gaji: float):
        self.__gaji = gaji

    def tampilkan_profil(self):
        print("[ PROFIL DOSEN ]")
        super().tampilkan_profil()
        print(f"NIP           : {self.__nip}")
        print(f"Mata Kuliah   : {self.__mata_kuliah}")
        print(f"Gaji          : Rp {self.__gaji:,.0f}".replace(",", "."))