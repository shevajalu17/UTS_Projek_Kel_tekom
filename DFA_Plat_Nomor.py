START = "p0"
ACCEPT = {"d1", "d2", "d3", "d4", "f1", "f2", "f3"}

DELTA = {
    "p0": {"HURUF": "p1"},
    "p1": {"HURUF": "p2", "DIGIT": "d1", "SPASI": "p3"},
    "p2": {"DIGIT": "d1", "SPASI": "p3"},
    "p3": {"DIGIT": "d1"},
    "d1": {"DIGIT": "d2", "SPASI": "sp", "HURUF": "f1"},
    "d2": {"DIGIT": "d3", "SPASI": "sp", "HURUF": "f1"},
    "d3": {"DIGIT": "d4", "SPASI": "sp", "HURUF": "f1"},
    "d4": {"SPASI": "sp", "HURUF": "f1"},
    "sp": {"HURUF": "f1"},
    "f1": {"HURUF": "f2"},
    "f2": {"HURUF": "f3"},
}

def klasifikasi(ch):
    if "A" <= ch <= "Z":
        return "HURUF"
    if "0" <= ch <= "9":
        return "DIGIT"
    if ch == " ":
        return "SPASI"
    return "LAIN"

def validasi(teks):
    state = START
    jejak = [state]
    for ch in teks:
        state = DELTA.get(state, {}).get(klasifikasi(ch), "DEAD")
        jejak.append(state)
        if state == "DEAD":
            break
    return state in ACCEPT, jejak

if __name__ == "__main__":
    uji = [
        ("AD 1234 XY", True),
        ("B1234CD", True),
        ("H 9 AB", True),
        ("DK 5678", True),
        ("AB 123 CDE", True),
        ("1234 AB", False),
        ("ABC 123 D", False),
        ("AD 12345 X", False),
        ("AD 1234 WXYZ", False),
        ("ad 1234 xy", False),
        ("AD  1234", False),
        ("AD", False),
    ]
    
    print("=== Validasi Nomor Registrasi (DFA) ===")
    for s, harapan in uji:
        diterima, jejak = validasi(s)
        status = "VALID" if diterima else "TIDAK VALID"
        cek = "OK " if diterima == harapan else "SALAH"
        print(f"[{cek}] {s!r:16} -> {status:12} | {' -> '.join(jejak)}")
        
    print("\nKetik string untuk diuji (kosongkan untuk keluar): ")
    while True:
        s = input("> ").strip()
        if not s:
            break
        diterima, jejak = validasi(s)
        print(" ", "VALID" if diterima else "TIDAK VALID", "|", " -> ".join(jejak))