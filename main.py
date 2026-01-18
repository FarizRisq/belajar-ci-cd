import json
import os

def run_analysis():
    file_path = 'database/corruson_matches_strict_exactseat.json'
    
    # Cek apakah file ada sebelum dibuka
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} tidak ditemukan!")
        return

    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Error: Gagal membaca JSON, format file rusak!")
            return

    print("=== DATA ANALYSIS REPORT ===")
    
    # Memastikan data diperlakukan sebagai list agar bisa di-loop
    items = data if isinstance(data, list) else [data]
    
    total_data = len(items)
    print(f"Total entries found: {total_data}")
    print("-" * 30)

    for item in items:
        # Menggunakan .get() agar tidak crash jika key tidak ada
        defect_id = item.get('defect_identifier', 'N/A')
        reg = item.get('defect_reg', 'Unknown')
        status = item.get('matched', 'No Status')
        score = item.get('final_score', 0)

        print(f"Defect ID   : {defect_id}")
        print(f"Registration: {reg}")
        print(f"Match Status: {status}")
        print(f"Final Score : {score}")
        print("-" * 30)

    print("=== ANALYSIS COMPLETED ===")

if __name__ == "__main__":
    run_analysis()
