# Mahasiswa.py

from Manusia import Manusia

# Turunan 1 dari Manusia (Hierarchical)
class Mahasiswa(Manusia):
    def __init__(self, nama: str = "", nik: str = "", ttl: str = "", jenis_kelamin: str = "",
                 nim: str = "", fakultas: str = "", prodi: str = "", semester: int = 1):
        super().__init__(nama, nik, ttl, jenis_kelamin)
        self.__nim = nim
        self.__fakultas = fakultas
        self.__prodi = prodi
        self.__semester = semester

    # Getter & Setter
    def get_nim(self) -> str:
        return self.__nim

    def set_nim(self, nim: str):
        self.__nim = nim

    def get_fakultas(self) -> str:
        return self.__fakultas

    def set_fakultas(self, fakultas: str):
        self.__fakultas = fakultas

    def get_prodi(self) -> str:
        return self.__prodi

    def set_prodi(self, prodi: str):
        self.__prodi = prodi

    def get_semester(self) -> int:
        return self.__semester

    def set_semester(self, semester: int):
        self.__semester = semester

    def tampilkan_profil(self):
        print("[ PROFIL MAHASISWA ]")
        super().tampilkan_profil()
        print(f"NIM           : {self.__nim}")
        print(f"Fakultas      : {self.__fakultas}")
        print(f"Program Studi : {self.__prodi}")
        print(f"Semester      : {self.__semester}")