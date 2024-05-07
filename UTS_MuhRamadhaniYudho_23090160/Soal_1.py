def input_bilangan_pertama():
    return float(input("Masukkan bilangan pertama (A): "))

def input_bilangan_kedua():
    return float(input("Masukkan bilangan kedua (B): "))

def tampilkan_penjumlahan(a, b):
    print("Hasil penjumlahan A + B:", a + b)

def tampilkan_pengurangan(a, b):
    print("Hasil pengurangan A - B:", a - b)

def tampilkan_modulus(a, b):
    print("Hasil modulus A % B:", a % b)

def main():
    print("===== Program Operasi Bilangan =====")
    a = input_bilangan_pertama()
    b = input_bilangan_kedua()

    tampilkan_penjumlahan(a, b)
    tampilkan_pengurangan(a, b)
    tampilkan_modulus(a, b)

if __name__ == "__main__":
    main()
