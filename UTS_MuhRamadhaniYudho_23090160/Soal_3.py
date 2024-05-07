def hitung_total_harga(jumlah_barang):
    total_harga = 0
    
    for i in range(jumlah_barang):
        harga_barang = float(input(f"Masukkan harga barang ke-{i+1}: "))
        total_harga += harga_barang
    
    return total_harga

def main():
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    
    total_harga = hitung_total_harga(jumlah_barang)
    
    print("Total harga pembelanjaan adalah:", total_harga)

if __name__ == "__main__":
    main()
