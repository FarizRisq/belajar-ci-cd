import pymongo
import json
import os

def kirim_semua_data():
    uri = os.getenv('MONGODB_URI')
    client = pymongo.MongoClient(uri)
    db = client['ProjectFariz']
    collection = db['CMR_Data']

    file_path = 'database/corruson_matches_strict_exactseat.json'
    
    try:
        with open(file_path, 'r') as f:
            data_full = json.load(f)
            
        total_data = len(data_full)
        print(f"Memulai import {total_data} data ke MongoDB...")

        # Gunakan insert_many untuk mengirim list secara massal
        # Ini jauh lebih cepat daripada kirim satu-satu pakai loop
        result = collection.insert_many(data_full)
        
        print(f"✅ BERHASIL! {len(result.inserted_ids)} data telah mendarat di Cloud.")
        
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat bulk import: {e}")

if __name__ == "__main__":
    kirim_semua_data()
