import random
import json

LEADERBOARD_FILE = "leaderboard.json"

# Fungsi untuk memuat leaderboard
def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Fungsi untuk menyimpan leaderboard
def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file)

# Fungsi untuk menampilkan leaderboard
def display_leaderboard(leaderboard):
    print("\n=== Leaderboard ===")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    for rank, (player, score) in enumerate(sorted_leaderboard, 1):
        print(f"{rank}. {player} - {score} poin")
    print("===================\n")

# Fungsi utama untuk game
def main():
    print("=== Game Tebak Angka ===")
    print("Tebak angka antara 1 hingga 100!")
    name = input("Masukkan nama Anda: ").strip()
    
    leaderboard = load_leaderboard()
    target_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Masukkan tebakan Anda: "))
            attempts += 1
            
            if guess < target_number:
                print("Terlalu rendah!")
            elif guess > target_number:
                print("Terlalu tinggi!")
            else:
                print(f"Selamat, {name}! Anda menebak angka dengan benar dalam {attempts} kali percobaan!")
                score = max(100 - attempts, 10)  # Skor minimum adalah 10
                print(f"Skor Anda: {score}")
                
                # Update leaderboard
                if name in leaderboard:
                    leaderboard[name] = max(leaderboard[name], score)
                else:
                    leaderboard[name] = score
                
                save_leaderboard(leaderboard)
                break
        except ValueError:
            print("Masukkan angka yang valid!")
    
    display_leaderboard(leaderboard)

if __name__ == "__main__":
    main()
