from app.model.mahasiswa import Mahasiswa
from app.model.fakultas import Fakultas
from app.model.prodi import Prodi
from app import response, db
from flask import request


def getallMahasiswa():
    try:
        mahasiswa = db.session.query(Mahasiswa, Fakultas, Prodi).join(
            Fakultas, Fakultas.id_fakultas == Mahasiswa.id_fakultas).join(Prodi, Prodi.id_prodi == Mahasiswa.id_prodi).all()
        data = formatarray(mahasiswa)
        return response.berhasil(data, "Berhasil Mendapatkan Data Mahasiswa")
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Mahasiswa")


def getoneMahasiswa(id_mahasiswa):
    try:
        mahasiswa = db.session.query(Mahasiswa, Fakultas, Prodi).join(
            Fakultas, Fakultas.id_fakultas == Mahasiswa.id_fakultas).join(Prodi, Prodi.id_prodi == Mahasiswa.id_prodi).filter(Mahasiswa.id_mahasiswa == id_mahasiswa)
        data = formatarray(mahasiswa)
        return response.berhasil(data, "Berhasil Mendapatkan Data Mahasiswa")
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Mahasiswa")


def updateMahasiswa(id_mahasiswa):
    try:
        nim_mahasiswa = request.form.get('nim_mahasiswa')
        nama_mahasiswa = request.form.get('nama_mahasiswa')
        angkatan_mahasiswa = request.form.get('angkatan_mahasiswa')
        id_fakultas = request.form.get('id_fakultas')
        id_prodi = request.form.get('id_prodi')

        datamahasiswa = [{
            'nim_mahasiswa': nim_mahasiswa,
            'nama_mahasiswa': nama_mahasiswa,
            'angkatan_mahasiswa': angkatan_mahasiswa,
            'id_fakultas': id_fakultas,
            'id_prodi': id_prodi
        }]

        mahasiswa = Mahasiswa.query.filter_by(
            id_mahasiswa=id_mahasiswa).first()
        mahasiswa.nim_mahasiswa = nim_mahasiswa
        mahasiswa.nama_mahasiswa = nama_mahasiswa
        mahasiswa.angkatan_mahasiswa = angkatan_mahasiswa
        mahasiswa.id_fakultas = id_fakultas
        mahasiswa.id_prodi = id_prodi

        db.session.commit()

        return response.berhasil(datamahasiswa, "Berhasil Mengubah Data Mahasiswa")
    except Exception as e:
        return response.gagal([], "Gagal Mengubah Data Mahasiswa")

def deleteMahasiswa(id_mahasiswa):
    try:
        mahasiswa = Mahasiswa.query.filter_by(id_mahasiswa=id_mahasiswa).first()
        if not mahasiswa:
            return response.gagal([], "Data Mahasiswa Tidak Ditemukan")
        
        db.session.delete(mahasiswa)
        db.session.commit()
        return response.berhasil([], "Berhasil Menghapus Data Mahasiswa")
    except Exception as e:
        return response.gagal([], "Gagal Menghapus Data Mahasiswa")


def formatarray(datas):
    dataarray = []
    for i in datas:
        dataarray.append(singleObject(i.Mahasiswa, i.Fakultas, i.Prodi))
    return dataarray


def singleObject(mahasiswa, fakultas, prodi):
    data = {
        'id_mahasiswa': mahasiswa.id_mahasiswa,
        'nim_mahasiswa': mahasiswa.nim_mahasiswa,
        'nama_mahasiswa': mahasiswa.nama_mahasiswa,
        'angkatan_mahasiswa': mahasiswa.angkatan_mahasiswa,
        'id_fakultas': fakultas.id_fakultas,
        'nama_fakultas': fakultas.nama_fakultas,
        'id_prodi': prodi.id_prodi,
        'nama_prodi': prodi.nama_prodi,
        'created_at': mahasiswa.created_at,
        'updated_at': mahasiswa.updated_at
    }
    return data


def addMahasiswa():
    try:
        nim_mahasiswa = request.form.get('nim_mahasiswa')
        nama_mahasiswa = request.form.get('nama_mahasiswa')
        angkatan_mahasiswa = request.form.get('angkatan_mahasiswa')
        id_fakultas = request.form.get('id_fakultas')
        id_prodi = request.form.get('id_prodi')

        mahasiswa = Mahasiswa(nim_mahasiswa=nim_mahasiswa, nama_mahasiswa=nama_mahasiswa,
                              angkatan_mahasiswa=angkatan_mahasiswa, id_fakultas=id_fakultas, id_prodi=id_prodi)
        db.session.add(mahasiswa)
        db.session.commit()

        return response.berhasil([], 'Berhasil Menambahkan Data Mahasiswa')
    except Exception as e:
        return response.gagal([], 'Gagal Menambahkan Data Mahasiswa')
