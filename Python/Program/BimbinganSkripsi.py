# BimbinganSkripsi.py

from Mahasiswa import Mahasiswa
from Dosen import Dosen

# Menggunakan Composition (Mahasiswa & Dosen dimiliki secara utuh oleh BimbinganSkripsi)
class BimbinganSkripsi:
    def __init__(self, id_bimbingan: str = "-", judul_skripsi: str = "-",
                mhs: Mahasiswa = None, dsn: Dosen = None, catatan: str = "Belum ada revisi"):
        self.__id_bimbingan = id_bimbingan
        self.__judul_skripsi = judul_skripsi
        self.__mhs = mhs if mhs is not None else Mahasiswa()
        self.__dsn_pembimbing = dsn if dsn is not None else Dosen()
        self.__catatan = catatan

    # Getter & Setter
    def get_id_bimbingan(self) -> str:
        return self.__id_bimbingan

    def get_judul_skripsi(self) -> str:
        return self.__judul_skripsi

    def set_judul_skripsi(self, judul: str):
        self.__judul_skripsi = judul

    def get_catatan(self) -> str:
        return self.__catatan

    def set_catatan(self, catatan: str):
        self.__catatan = catatan

    def cetak_kartu(self):
        print("\n======================================================")
        print(f" KARTU KONTROL BIMBINGAN SKRIPSI | ID: {self.__id_bimbingan}")
        print("======================================================")
        print(f"Judul Skripsi : {self.__judul_skripsi}")
        print("------------------------------------------------------")
        print("MAHASISWA:")
        self.__mhs.tampilkan_profil()
        print("------------------------------------------------------")
        print("DOSEN PEMBIMBING:")
        self.__dsn_pembimbing.tampilkan_profil()
        print("------------------------------------------------------")
        print(f"Catatan Revisi: {self.__catatan}")
        print("======================================================")