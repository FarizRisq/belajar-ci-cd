import pymongo
import os
import random
from datetime import datetime, timedelta

def generate_random_data():
    uri = os.getenv('MONGODB_URI')
    client = pymongo.MongoClient(uri)
    db = client['ProjectFariz']
    collection = db['CMR_Data']

    jumlah_data = random.randint(10, 15)
    data_list = []

    for i in range(jumlah_data):
        # Simulasi tanggal random dalam 30 hari terakhir
        random_days = random.randint(0, 30)
        dt_defect = datetime.now() - timedelta(days=random_days)
        dt_repair = dt_defect + timedelta(days=random.randint(1, 10))

        new_data = {
            "defect_identifier": f"IU-SH-{random.randint(100000, 999999)}",
            "defect_date": dt_defect.strftime("%Y-%m-%d 00:00:00"),
            "defect_reg": random.choice(["PK-SGC", "PK-SAA", "PK-SAB"]),
            "defect_desc": "Auto: " + random.choice([
                "when crew arrive at aerobridge, aerobridge not install",
                "engine oil low pressure message on display",
                "unusual vibration during descent",
                "cargo door indicator light intermittent"
            ]),
            "matched": True,
            "forced_match": False,
            "match_rank": 1,
            "repair_id": f"S{random.randint(3000000, 3999999)}",
            "repair_date": dt_repair.strftime("%Y-%m-%d 00:00:00"),
            "repair_ac": "PK-SGC",
            "repair_desc": random.choice(["AIR BLEED MAINT MSG", "HYDRAULIC PUMP REPLACEMENT", "CHECK SENSOR CABLE"]),
            "repair_resolution": "REF TSM 36-00-00. C/O BITE TEST. RESULT SATISFACTORY.",
            "text_sim": round(random.uniform(0.1, 0.9), 4),
            "final_score": round(random.uniform(0.1, 0.9), 4),
            "keyword_score_raw": round(random.uniform(0.5, 1.5), 2),
            "seat_score": 0,
            "defect_keywords": random.choice(["seat_explicit", "engine_sys", "none"]),
            "repair_keywords": "display,seat_explicit",
            "reg_match": True,
            "fallback": False,
            "timeout": False,
            "is_auto_generated": True # Penanda kalau ini data bot
        }
        data_list.append(new_data)

    collection.insert_many(data_list)
    print(f"✅ Sukses! {jumlah_data} data baru dengan kolom lengkap telah di-import.")

if __name__ == "__main__":
    generate_random_data()
