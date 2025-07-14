def tampilkan_menu_utama():
    """Menampilkan menu utama game."""
    print("\n=== Game Uji Kualitatif Senyawa Organik dan Anorganik ===")
    print("1. Materi")
    print("2. Latihan")
    print("3. Keluar")

def tampilkan_materi():
    """Menampilkan dan mengelola menu materi."""
    while True:
        print("\n=== Menu Materi ===")
        print("1. Materi Organik")
        print("2. Materi Anorganik")
        print("3. Kembali")
        pilihan = input("Pilih: ")

        if pilihan == '1':
            print("\n--- Materi Organik ---")
            print("Senyawa organik mengandung karbon, seperti alkohol, karbohidrat, dan protein.")
        elif pilihan == '2':
            print("\n--- Materi Anorganik ---")
            print("Senyawa anorganik seperti garam, asam, basa, dan oksida logam.")
        elif pilihan == '3':
            break  # Keluar dari loop materi
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
