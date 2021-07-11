from app.model.prodi import Prodi
from app.model.fakultas import Fakultas
from app import response, db
from flask import request


def getallProdi():
    try:
        prodi = db.session.query(Fakultas, Prodi).join(
            Fakultas, Fakultas.id_fakultas == Prodi.id_fakultas).all()
        data = formatarray(prodi)
        return response.berhasil(data, "Berhasil Mendapatkan Data Prodi")
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Prodi")


def getoneProdi(id_prodi):
    try:
        prodi = db.session.query(Fakultas, Prodi).join(
            Fakultas, Fakultas.id_fakultas == Prodi.id_fakultas).filter(Prodi.id_prodi == id_prodi)
        data = formatarray(prodi)
        return response.berhasil(data, "Berhasil Mendapatkan Data Prodi")
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Prodi")


def updateProdi(id_prodi):
    try:
        kode_prodi = request.form.get('kode_prodi')
        nama_prodi = request.form.get('nama_prodi')
        id_fakultas = request.form.get('id_fakultas')
        dataprodi = [{
            'kode_prodi': kode_prodi,
            'nama_prodi': nama_prodi,
            'id_fakultas': id_fakultas
        }]
        prodi = Prodi.query.filter_by(id_prodi=id_prodi).first()
        prodi.kode_prodi = kode_prodi
        prodi.nama_prodi = nama_prodi
        prodi.id_fakultas = id_fakultas
        db.session.commit()

        return response.berhasil(dataprodi, "Berhasil Mengubah Data Prodi")
    except Exception as e:
        return response.gagal([], "Gagal Mengubah Data Prodi")


def deleteProdi(id_prodi):
    try:
        prodi = Prodi.query.filter_by(id_prodi=id_prodi).first()
        if not prodi:
            return response.gagal([], "Data Prodi Tidak Ditemukan")

        db.session.delete(prodi)
        db.session.commit()
        return response.berhasil([], "Berhasil Menghapus Data Mahasiswa")
    except Exception as e:
        return response.gagal([], "Gagal Menghapus Data Mahasiswa")


def formatarray(datas):
    dataarray = []
    for i in datas:
        dataarray.append(singleObject(i.Prodi, i.Fakultas))
    return dataarray


def singleObject(prodi, fakultas):
    data = {
        'id_prodi': prodi.id_prodi,
        'kode_prodi': prodi.kode_prodi,
        'nama_prodi': prodi.nama_prodi,
        'id_fakultas': prodi.id_fakultas,
        'nama_fakultas': fakultas.nama_fakultas,
        'created_at': prodi.created_at,
        'updated_at': prodi.updated_at
    }
    return data


def addProdi():
    try:
        kode_prodi = request.form.get('kode_prodi')
        nama_prodi = request.form.get('nama_prodi')
        id_fakultas = request.form.get('id_fakultas')

        prodi = Prodi(kode_prodi=kode_prodi,
                      nama_prodi=nama_prodi, id_fakultas=id_fakultas)
        db.session.add(prodi)
        db.session.commit()

        return response.berhasil([], 'Berhasil Menambahkan Data Prodi')
    except Exception as e:
        return response.gagal([], "Gagal Menambahkan Data Prodi")
