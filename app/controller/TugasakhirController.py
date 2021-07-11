from app.model.tugasakhir import Tugasakhir
from app.model.mahasiswa import Mahasiswa
from app.model.dosen import Dosen
from app.model.fakultas import Fakultas
from app.model.prodi import Prodi
from app import response, db
from flask import request


def getallTugasakhir():
    try:
        tugasakhir = db.session.query(Tugasakhir, Mahasiswa, Fakultas, Dosen, Prodi).join(Mahasiswa, Mahasiswa.id_mahasiswa == Tugasakhir.id_mahasiswa).join(
            Dosen, Dosen.id_dosen == Tugasakhir.id_dosen).join(Fakultas, Fakultas.id_fakultas == Tugasakhir.id_fakultas).join(Prodi, Prodi.id_prodi == Tugasakhir.id_prodi).all()
        data = formatarray(tugasakhir)
        return response.berhasil(data, "Berhasil Mendapatkan Data Tugas Akhir")
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Tugas Akhir")


def getoneTugasakhir(id_tugasakhir):
    try:
        tugasakhir = db.session.query(Tugasakhir, Mahasiswa, Fakultas, Dosen, Prodi).join(Mahasiswa, Mahasiswa.id_mahasiswa == Tugasakhir.id_mahasiswa).join(
            Dosen, Dosen.id_dosen == Tugasakhir.id_dosen).join(Fakultas, Fakultas.id_fakultas == Tugasakhir.id_fakultas).join(Prodi, Prodi.id_prodi == Tugasakhir.id_prodi).filter(Tugasakhir.id_tugasakhir == id_tugasakhir)
        data = formatarray(tugasakhir)
        return response.berhasil(data, "Berhasil Mendapatkan Data Tugas Akhir")
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Tugas Akhir")


def getTugasakhirclient(judul_tugasakhir):
    try:
        tugasakhir = db.session.query(Tugasakhir, Mahasiswa, Fakultas, Dosen, Prodi).join(Mahasiswa, Mahasiswa.id_mahasiswa == Tugasakhir.id_mahasiswa).join(
            Dosen, Dosen.id_dosen == Tugasakhir.id_dosen).join(Fakultas, Fakultas.id_fakultas == Tugasakhir.id_fakultas).join(Prodi, Prodi.id_prodi == Tugasakhir.id_prodi).filter(Tugasakhir.judul_tugasakhir.contains(judul_tugasakhir))
        data = formatarray(tugasakhir)
        return response.berhasil(data, "Berhasil Mendapatkan Data Tugas Akhir")
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Tugas Akhir")


def updateTugasakhir(id_tugasakhir):
    try:
        judul_tugasakhir = request.form.get('judul_tugasakhir')
        tanggal_tugasakhir = request.form.get('tanggal_tugasakhir')
        status_tugasakhir = request.form.get('status_tugasakhir')
        id_mahasiswa = request.form.get('id_mahasiswa')
        id_dosen = request.form.get('id_dosen')
        id_fakultas = request.form.get('id_fakultas')
        id_prodi = request.form.get('id_prodi')

        datatugasakhir = [{
            'judul_tugasakhir': judul_tugasakhir,
            'tanggal_tugasakhir': tanggal_tugasakhir,
            'status_tugasakhir': status_tugasakhir,
            'id_mahasiswa': id_mahasiswa,
            'id_dosen': id_dosen,
            'id_fakultas': id_fakultas,
            'id_prodi': id_prodi
        }]

        tugasakhir = Tugasakhir.query.filter_by(
            id_tugasakhir=id_tugasakhir).first()
        tugasakhir.judul_tugasakhir = judul_tugasakhir
        tugasakhir.tanggal_tugasakhir = tanggal_tugasakhir
        tugasakhir.status_tugasakhir = status_tugasakhir
        tugasakhir.id_mahasiswa = id_mahasiswa
        tugasakhir.id_dosen = id_dosen
        tugasakhir.id_fakultas = id_fakultas
        tugasakhir.id_prodi = id_prodi

        db.session.commit()

        return response.berhasil(datatugasakhir, "Berhasil Mengubah Data Tugas Akhir")
    except Exception as e:
        print(e)
        return response.gagal([], "Gagal Mengubah Data Tugas Akhir")


def formatarray(datas):
    dataarray = []
    for i in datas:
        dataarray.append(singleObjecttugasakhir(
            i.Tugasakhir, i.Mahasiswa, i.Dosen, i.Fakultas, i.Prodi))
    return dataarray


def singleObjecttugasakhir(tugasakhir, mahasiswa, dosen, fakultas, prodi):
    status_tugasakhir = ''
    if tugasakhir.status_tugasakhir == "BELUMSELESAI":
        status_tugasakhir = "BELUM SELESAI"
    else:
        status_tugasakhir = tugasakhir.status_tugasakhir

    data = {
        'id_tugasakhir': tugasakhir.id_tugasakhir,
        'judul_tugasakhir': tugasakhir.judul_tugasakhir,
        'tanggal_tugasakhir': tugasakhir.tanggal_tugasakhir,
        'status_tugasakhir': status_tugasakhir,
        'nim_mahasiswa': mahasiswa.nim_mahasiswa,
        'nama_mahasiswa': mahasiswa.nama_mahasiswa,
        'nip_dosen': dosen.nip_dosen,
        'nama_dosen': dosen.nama_dosen,
        'id_fakultas': fakultas.id_fakultas,
        'nama_fakultas': fakultas.nama_fakultas,
        'id_prodi': prodi.id_prodi,
        'nama_prodi': prodi.nama_prodi,
        'created_at': tugasakhir.created_at,
        'updated_at': tugasakhir.updated_at
    }
    return data


def addTugasakhir():
    try:
        judul_tugasakhir = request.form.get('judul_tugasakhir')
        tanggal_tugasakhir = request.form.get('tanggal_tugasakhir')
        status_tugasakhir = request.form.get('status_tugasakhir')
        id_mahasiswa = request.form.get('id_mahasiswa')
        id_dosen = request.form.get('id_dosen')
        id_fakultas = request.form.get('id_fakultas')
        id_prodi = request.form.get('id_prodi')

        tugasakhir = Tugasakhir(judul_tugasakhir=judul_tugasakhir, tanggal_tugasakhir=tanggal_tugasakhir,
                                status_tugasakhir=status_tugasakhir, id_mahasiswa=id_mahasiswa, id_dosen=id_dosen, id_fakultas=id_fakultas, id_prodi=id_prodi)
        db.session.add(tugasakhir)
        db.session.commit()

        return response.berhasil([], 'Berhasil Menambahkan Data Tugas Akhir')
    except Exception as e:
        print(e)
        return response.gagal([], "Gagal Menambahkan Data Tugas Akhir")


def deleteTugasakhir(id_tugasakhir):
    try:
        tugasakhir = Tugasakhir.query.filter_by(
            id_tugasakhir=id_tugasakhir).first()
        if not tugasakhir:
            return response.gagal([], "Data Tugas Akhir Tidak Ditemukan")

        db.session.delete(tugasakhir)
        db.session.commit()
        return response.berhasil([], "Berhasil Menghapus Data Mahasiswa")
    except Exception as e:
        return response.gagal([], "Gagal Menghapus Data Tugas Akhir")
