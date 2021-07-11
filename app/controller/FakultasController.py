from app.model.fakultas import Fakultas
from app import response, db
from flask import request


def getallFakultas():
    try:
        fakultas = Fakultas.query.all()
        data = formatarray(fakultas)
        return response.berhasil(data, "Berhasil Mendapatkan Data Fakultas")
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Fakultas")


def getoneFakultas(id_fakultas):
    try:
        fakultas = Fakultas.query.filter(Fakultas.id_fakultas == id_fakultas)
        data = formatarray(fakultas)
        return response.berhasil(data, "Berhasil Mendapatkan Data Fakultas")
    except Exception as e:
        return response.gagal([], "Gagal Mendapatkan Data Fakultas")


def updateFakultas(id_fakultas):
    try:
        kode_fakultas = request.form.get('kode_fakultas')
        nama_fakultas = request.form.get('nama_fakultas')

        datafakultas = [{
            'kode_fakultas': kode_fakultas,
            'nama_fakultas': nama_fakultas
        }]

        fakultas = Fakultas.query.filter_by(id_fakultas=id_fakultas).first()
        fakultas.kode_fakultas = kode_fakultas
        fakultas.nama_fakultas = nama_fakultas

        db.session.commit()

        return response.berhasil(datafakultas, "Berhasil Mengubah Data Fakultas")
    except Exception as e:
        return response.gagal([], "Gagal Mengubah Data Fakultas")


def deleteFakultas(id_fakultas):
    try:
        print("ID FAKULTAS")
        print(id_fakultas)
        fakultas = Fakultas.query.filter_by(id_fakultas=id_fakultas).first()
        if not fakultas:
            return response.gagal([], "Data Fakultas Tidak Ditemukan")

        db.session.delete(fakultas)
        db.session.commit()
        return response.berhasil([], "Berhasil Menghapus Data Fakultas")
    except Exception as e:
        return response.gagal([], "Gagal Menghapus Data Fakultas")


def formatarray(datas):
    dataarray = []
    for i in datas:
        dataarray.append(singleObject(i))
    return dataarray


def singleObject(data):
    data = {
        'id_fakultas': data.id_fakultas,
        'kode_fakultas': data.kode_fakultas,
        'nama_fakultas': data.nama_fakultas,
        'created_at': data.created_at,
        'updated_at': data.updated_at
    }
    return data


def addFakultas():
    try:
        kode_fakultas = request.form.get('kode_fakultas')
        nama_fakultas = request.form.get('nama_fakultas')

        fakultas = Fakultas(kode_fakultas=kode_fakultas,
                            nama_fakultas=nama_fakultas)
        db.session.add(fakultas)
        db.session.commit()

        return response.berhasil([], 'Berhasil Menambahkan Data Fakultas')
    except Exception as e:
        return response.gagal([], "Gagal Menambahkan Data Fakultas")
