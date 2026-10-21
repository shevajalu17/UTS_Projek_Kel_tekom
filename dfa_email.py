def validasi_email(email):
    # Definisi state
    q0 = "q0"  # State awal
    q1 = "q1"  # Membaca username
    q2 = "q2"  # Simbol @ sudah dibaca
    q3 = "q3"  # Membaca domain
    q4 = "q4"  # Titik setelah domain
    q5 = "q5"  # Satu huruf ekstensi
    q6 = "q6"  # Minimal dua huruf ekstensi
    qd = "DEAD"  # Dead state

    state = q0
    alur = [q0]

    # Membaca input satu karakter demi satu karakter
    for karakter in email:
        if state == q0:
            if karakter.isascii() and karakter.isalnum():
                state = q1
            else:
                state = qd

        elif state == q1:
            if karakter.isascii() and karakter.isalnum():
                state = q1
            elif karakter == "@":
                state = q2
            else:
                state = qd

        elif state == q2:
            if karakter.isascii() and karakter.isalnum():
                state = q3
            else:
                state = qd

        elif state == q3:
            if karakter.isascii() and karakter.isalnum():
                state = q3
            elif karakter == ".":
                state = q4
            else:
                state = qd

        elif state == q4:
            if karakter.isascii() and karakter.isalpha():
                state = q5
            else:
                state = qd

        elif state == q5:
            if karakter.isascii() and karakter.isalpha():
                state = q6
            else:
                state = qd

        elif state == q6:
            if karakter.isascii() and karakter.isalpha():
                state = q6
            else:
                state = qd

        elif state == qd:
            state = qd

        # Menyimpan setiap perpindahan state
        alur.append(state)

    # Menentukan hasil validasi
    if state == q6:
        hasil = "VALID (ACCEPT)"
    else:
        hasil = "TIDAK VALID (REJECT)"

    return hasil, alur


# Input email dari pengguna
email = input("Masukkan alamat email: ")

# Validasi dan tampilkan hasil
hasil, alur = validasi_email(email)

print("Hasil validasi:", hasil)
print("Alur string:", " -> ".join(alur))