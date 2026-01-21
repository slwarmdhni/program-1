def display_board(board):
    """Menampilkan papan permainan Tic Tac Toe."""
    print("\n")
    for i in range(3):
        for j in range(3):
            cell = board[i * 3 + j]
            print(f" {cell} ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("-----------")
    print("\n")


def check_winner(board, player):
    """Mengecek apakah pemain menang."""
    # Kombinasi kemenangan (3 dalam satu baris, kolom, atau diagonal)
    win_conditions = [
        [0, 1, 2],  # Baris pertama
        [3, 4, 5],  # Baris kedua
        [6, 7, 8],  # Baris ketiga
        [0, 3, 6],  # Kolom pertama
        [1, 4, 7],  # Kolom kedua
        [2, 5, 8],  # Kolom ketiga
        [0, 4, 8],  # Diagonal dari kiri atas ke kanan bawah
        [2, 4, 6],  # Diagonal dari kanan atas ke kiri bawah
    ]
    
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def is_board_full(board):
    """Mengecek apakah papan sudah penuh (seri)."""
    return all(cell in ['X', 'O'] for cell in board)


def is_valid_move(board, position):
    """Memvalidasi apakah langkah yang diinputkan valid."""
    if position < 1 or position > 9:
        return False
    if board[position - 1] in ['X', 'O']:
        return False
    return True


def play_game():
    """Fungsi utama untuk menjalankan game Tic Tac Toe."""
    # Inisialisasi papan dengan posisi 1-9
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'
    
    print("=" * 50)
    print("  SELAMAT DATANG DI GAME TIC TAC TOE")
    print("=" * 50)
    print("\nPapan permainan menggunakan posisi 1-9:")
    print("\n 1 | 2 | 3")
    print("-----------")
    print(" 4 | 5 | 6")
    print("-----------")
    print(" 7 | 8 | 9")
    print("\nPemain X dan O bergantian memilih posisi.")
    print("=" * 50)
    
    while True:
        # Tampilkan papan saat ini
        display_board(board)
        
        # Cek kemenangan
        if check_winner(board, 'X'):
            print("🎉 Pemain X MENANG! Selamat!")
            break
        elif check_winner(board, 'O'):
            print("🎉 Pemain O MENANG! Selamat!")
            break
        elif is_board_full(board):
            print("🤝 Game SERI! Semua posisi sudah terisi.")
            break
        
        # Input pemain
        while True:
            try:
                position = int(input(f"Pemain {current_player}, pilih posisi (1-9): "))
                if is_valid_move(board, position):
                    board[position - 1] = current_player
                    break
                else:
                    print("❌ Posisi tidak valid! Pilih posisi yang kosong (1-9).")
            except ValueError:
                print("❌ Input tidak valid! Masukkan angka 1-9.")
        
        # Ganti pemain
        current_player = 'O' if current_player == 'X' else 'X'
    
    # Tampilkan papan akhir
    display_board(board)
    
    # Tanya apakah ingin bermain lagi
    while True:
        play_again = input("Ingin bermain lagi? (y/n): ").lower()
        if play_again in ['y', 'n']:
            if play_again == 'y':
                play_game()
            else:
                print("\nTerima kasih telah bermain Tic Tac Toe! Sampai jumpa!")
            break
        else:
            print("Masukkan 'y' atau 'n'")


if __name__ == "__main__":
    play_game()
