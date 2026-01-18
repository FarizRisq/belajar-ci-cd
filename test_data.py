import json
import os

def test_check_json_structure():
    file_path = 'database/corruson_matches_strict_exactseat.json'
    assert os.path.exists(file_path), "File JSON hilang!"

    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Bungkus ke list jika data cuma satu objek agar loop tetap jalan
    items = data if isinstance(data, list) else [data]

    for item in items:
        # 1. Pastikan ID defect ada (Sangat penting buat database)
        assert item.get('defect_identifier'), "Ada data tanpa Defect ID!"
        
        # 2. Cek registrasi tetap harus PK- (Standard operasional)
        reg = item.get('defect_reg', '')
        assert reg.startswith("PK-"), f"ID {item.get('defect_identifier')}: Registrasi '{reg}' salah!"

        # 3. Pastikan kolom 'matched' ada (biar program utama nggak crash)
        assert 'matched' in item, f"ID {item.get('defect_identifier')} tidak punya status 'matched'"
