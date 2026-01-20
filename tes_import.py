import pymongo
import json
import os

def kirim_data_sample():
    # 1. Ambil URI dari Secret
    uri = os.getenv('MONGODB_URI')
    client = pymongo.MongoClient(uri)
    
    # Pilih Database dan Collection (tabel)
    db = client['ProjectFariz']
    collection = db['CMR_Data']

    # 2. Buka file JSON di folder database
    file_path = 'database/corruson_matches_strict_exactseat.json'
    
    try:
        with open(file_path, 'r') as f:
            data_full = json.load(f)
            
        # Ambil hanya 1 data pertama sebagai percobaan
        sample_data = data_full[0]
        
        # 3. Kirim ke MongoDB
        result = collection.insert_one(sample_data)
        print(f"✅ Berhasil! Data pertama masuk dengan ID: {result.inserted_id}")
        
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    kirim_data_sample()
