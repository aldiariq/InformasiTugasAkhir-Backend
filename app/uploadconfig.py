EKSTENSI_FILE = set(['png','jpg','jpeg'])

def cek_ekstensi(namafile):
    return '.' in namafile and namafile.rsplit('.', 1)[1].lower() in EKSTENSI_FILE