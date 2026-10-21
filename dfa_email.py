def validasi_email(email):
    # Definisi state
    q0 = "q0"  # State awal
    q1 = "q1"  # Membaca username
    q2 = "q2"  # Simbol @ sudah dibaca
    q3 = "q3"  # Membaca domain
    q4 = "q4"  # Titik setelah domain
    q5 = "q5"  # Satu huruf ekstensi
    q6 = "q6"  # Minimal dua huruf ekstensi
    qd = "qd"  # Dead state

    state = q0

    # Membaca input satu karakter demi satu karakter
    for karakter in email:

        if state == q0:
            if karakter.isalnum():
                state = q1
            else:
                state = qd

        elif state == q1:
            if karakter.isalnum():
                state = q1
            elif karakter == "@":
                state = q2
            else:
                state = qd

        elif state == q2:
            if karakter.isalnum():
                state = q3
            else:
                state = qd

        elif state == q3:
            if karakter.isalnum():
                state = q3
            elif karakter == ".":
                state = q4
            else:
                state = qd

        elif state == q4:
            if karakter.isalpha():
                state = q5
            else:
                state = qd

        elif state == q5:
            if karakter.isalpha():
                state = q6
            else:
                state = qd

        elif state == q6:
            if karakter.isalpha():
                state = q6
            else:
                state = qd

        elif state == qd:
            state = qd

    # Menentukan apakah input diterima atau ditolak
    if state == q6:
        return "VALID (ACCEPT)"
    else:
        return "TIDAK VALID (REJECT)"


# Input email dari pengguna
email = input("Masukkan alamat email: ")

# Validasi dan tampilkan hasil
hasil = validasi_email(email)

print("Hasil validasi:", hasil)