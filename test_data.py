import json
import os

def test_check_json_structure():
    # Sesuaikan path jika folder Database kamu menggunakan huruf besar/kecil
    file_path = 'database/corruson_matches_strict_exactseat.json'
    
    # Pastikan file ada
    assert os.path.exists(file_path), f"File tidak ditemukan di: {file_path}"

    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Handle jika data berupa list atau objek tunggal
    items = data if isinstance(data, list) else [data]

    for item in items:
        # 1. Pastikan ID defect ada
        assert item.get('defect_identifier'), "Ada data tanpa Defect ID!"
        
        # 2. Cek registrasi (Skip jika kosong, tapi jika ada wajib PK-)
        reg = item.get('defect_reg')
        if reg: 
            assert str(reg).startswith("PK-"), f"ID {item.get('defect_identifier')}: Registrasi '{reg}' salah!"

        # 3. Pastikan kolom 'matched' ada
        assert 'matched' in item, f"ID {item.get('defect_identifier')} tidak punya status 'matched'"
