# Implementasi DFA untuk Validasi Sintaks/Input

Tugas Kelompok - Mata Kuliah [Nama Mata Kuliah / Teori Bahasa dan Automata]

## Anggota Kelompok

| No | Nama | NIM | Kontribusi |
|----|------|-----|------------|
| 1  | [Nama Anggota 1] | [NIM] | [mis. Kasus 1 & dokumentasi] |
| 2  | [Nama Anggota 2] | [NIM] | [mis. Kasus 2 & pengujian] |
| 3  | [Nama Anggota 3] | [NIM] | [mis. Kasus 3, Kasus 4 & kode] |

## Deskripsi

Program ini mengimplementasikan **Deterministic Finite Automata (DFA)** untuk memvalidasi string masukan. Setiap string diproses karakter demi karakter mengikuti tabel transisi, lalu dinyatakan **VALID** (berhenti di state akhir) atau **TIDAK VALID** (berhenti di state non-akhir atau masuk state `DEAD`). Program juga menampilkan **jejak transisi state**.

- Bahasa pemrograman: Python 3
- Kasus yang diimplementasikan:
  1. Validasi nama variabel
  2. Validasi format email sederhana
  3. Validasi notasi ilmiah (eksponen)
  4. Validasi plat nomor kendaraan Indonesia *(kasus tambahan)*

## Struktur Folder

```
.
├── README.md
├── kasus1_variabel.py
├── kasus2_email.py
├── kasus3_notasi_ilmiah.py
└── kasus4_plat_nomor.py
```

## Cara Menjalankan

```bash
python3 kasus1_variabel.py
python3 kasus2_email.py
python3 kasus3_notasi_ilmiah.py
python3 kasus4_plat_nomor.py
```