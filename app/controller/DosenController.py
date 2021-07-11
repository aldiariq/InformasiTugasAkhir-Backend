from app.controller.TugasakhirController import singleObjecttugasakhir
from app.model.dosen import Dosen
from app.model.fakultas import Fakultas
from app.model.prodi import Prodi
from app.model.tugasakhir import Tugasakhir
from app import response, db
from flask import request


def getallDosen():
    try:
        jumlah_mahasiswa_bimbingan = db.session.query(Dosen, Tugasakhir).join(
            Tugasakhir, Tugasakhir.id_dosen == Dosen.id_dosen).filter(Tugasakhir.status_tugasakhir == "BELUMSELESAI").count()
        dosen = db.session.query(Dosen, Fakultas, Prodi).join(
            Fakultas, Fakultas.id_fakultas == Dosen.id_fakultas).join(Prodi, Prodi.id_prodi == Dosen.id_prodi).all()
        data = formatarray(dosen, jumlah_mahasiswa_bimbingan)
        return response.berhasil(data, "Berhasil Mendapatkan Data Dosen")
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Dosen")


def getoneDosen(id_dosen):
    try:
        jumlah_mahasiswa_bimbingan = db.session.query(Dosen, Tugasakhir).join(
            Tugasakhir, Tugasakhir.id_dosen == Dosen.id_dosen).filter(Tugasakhir.status_tugasakhir == "BELUMSELESAI").count()
        dosen = db.session.query(Dosen, Fakultas, Prodi).join(
            Fakultas, Fakultas.id_fakultas == Dosen.id_fakultas).join(Prodi, Prodi.id_prodi == Dosen.id_prodi).filter(Dosen.id_dosen == id_dosen)
        data = formatarray(dosen, jumlah_mahasiswa_bimbingan)
        return response.berhasil(data, "Berhasil Mendapatkan Data Dosen")
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Dosen")


def updateDosen(id_dosen):
    try:
        nip_dosen = request.form.get('nip_dosen')
        nama_dosen = request.form.get('nama_dosen')
        id_fakultas = request.form.get('id_fakultas')
        id_prodi = request.form.get('id_prodi')

        datadosen = [{
            'nip_dosen': nip_dosen,
            'nama_dosen': nama_dosen,
            'id_fakultas': id_fakultas,
            'id_prodi': id_prodi
        }]

        dosen = Dosen.query.filter_by(id_dosen=id_dosen).first()
        dosen.nip_dosen = nip_dosen
        dosen.nama_dosen = nama_dosen
        dosen.id_fakultas = id_fakultas
        dosen.id_prodi = id_prodi
        db.session.commit()

        return response.berhasil(datadosen, "Berhasil Mengubah Data Dosen")
    except Exception as e:
        return response.gagal([], "Gagal Mengubah Data Dosen")


def deleteDosen(id_dosen):
    try:
        dosen = Dosen.query.filter_by(id_dosen=id_dosen).first()
        if not dosen:
            return response.gagal([], "Data Dosen Tidak Ditemukan")

        db.session.delete(dosen)
        db.session.commit()
        return response.berhasil([], "Berhasil Menghapus Data Dosen")
    except Exception as e:
        return response.gagal([], "Gagal Menghapus Data Dosen")


def formatarray(datas, jumlah_mahasiswa_bimbingan):
    dataarray = []
    for i in datas:
        dataarray.append(singleObject(i.Dosen, i.Fakultas,
                         i.Prodi, jumlah_mahasiswa_bimbingan))
    return dataarray


def singleObject(dosen, fakultas, prodi, jumlah_mahasiswa_bimbingan):
    data = {
        'id_dosen': dosen.id_dosen,
        'nip_dosen': dosen.nip_dosen,
        'nama_dosen': dosen.nama_dosen,
        'id_fakultas': fakultas.id_fakultas,
        'nama_fakultas': fakultas.nama_fakultas,
        'id_prodi': prodi.id_prodi,
        'nama_prodi': prodi.nama_prodi,
        'jumlah_mahasiswa_bimbingan': jumlah_mahasiswa_bimbingan,
        'judul_tugasakhir_mahasiswa': getTugasakhir(dosen.id_dosen),
        'created_at': dosen.created_at,
        'updated_at': dosen.updated_at
    }
    return data


def getTugasakhir(id_dosen):
    try:
        tugasakhir = Tugasakhir.query.filter(
            Tugasakhir.id_dosen == id_dosen, Tugasakhir.status_tugasakhir == "BELUMSELESAI")
        data = formatarrayTugasakhir(tugasakhir)
        return data
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Tugas Akhir")


def formatarrayTugasakhir(datas):
    dataarray = []
    for i in datas:
        dataarray.append(singleObjecttugasakhir(i))
    return dataarray


def singleObjecttugasakhir(data):
    data = {
        'judul_tugasakhir': data.judul_tugasakhir
    }
    return data


def addDosen():
    try:
        nip_dosen = request.form.get('nip_dosen')
        nama_dosen = request.form.get('nama_dosen')
        id_fakultas = request.form.get('id_fakultas')
        id_prodi = request.form.get('id_prodi')

        dosen = Dosen(nip_dosen=nip_dosen, nama_dosen=nama_dosen,
                      id_fakultas=id_fakultas, id_prodi=id_prodi)
        db.session.add(dosen)
        db.session.commit()

        return response.berhasil([], 'Berhasil Menambahkan Data Dosen')
    except Exception as e:
        return response.gagal([], "Berhasil Mengubah Data Dosen")
