import json
import os

def run_analysis():
    # Path ke file JSON kamu
    file_path = 'database/corruson_matches_strict_exactseat.json'
    
    if not os.path.exists(file_path):
        print(f"❌ Error: File {file_path} tidak ditemukan!")
        return

    with open(file_path, 'r') as f:
        data = json.load(f)

    # Menampilkan ringkasan data
    print("=== DATA ANALYSIS REPORT ===")
    print(f"Defect ID  : {data.get('defect_identifier')}")
    print(f"Aircraft   : {data.get('defect_reg')}")
    print(f"Description: {data.get('defect_desc')}")
    print(f"Repair ID  : {data.get('repair_id')}")
    print(f"Match Score: {data.get('final_score')}")
    print("============================")

if __name__ == "__main__":
    run_analysis()
