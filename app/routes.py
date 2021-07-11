from flask import request
from app import app, response
from app.controller import FakultasController, ProdiController, DosenController, MahasiswaController, TugasakhirController, AdminController
from flask_jwt_extended import get_jwt_identity, jwt_required

prefix = '/api/'

# Endpoint Utama


@app.route(prefix)
@jwt_required()
def index():
    try:
        return response.berhasil([], "Endpoint Utama Restful API Informasi Tugas Akhir")
    except Exception as e:
        return response.gagal([], "Gagal Melihat Info Restful API")


# Endpoint Fakultas
routefakultas = prefix + 'fakultas/'


@app.route(routefakultas, methods=['GET', 'POST'])
@jwt_required()
def getpostfakultas():
    if request.method == 'GET':
        return FakultasController.getallFakultas()
    elif request.method == 'POST':
        return FakultasController.addFakultas()


@app.route(routefakultas + '<id_fakultas>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def getputdeletefakultas(id_fakultas):
    if request.method == 'GET':
        return FakultasController.getoneFakultas(id_fakultas)
    elif request.method == 'PUT':
        return FakultasController.updateFakultas(id_fakultas)
    elif request.method == 'DELETE':
        return FakultasController.deleteFakultas(id_fakultas)


# Endpoint Prodi
routeprodi = prefix + 'prodi/'


@app.route(routeprodi, methods=['GET', 'POST'])
@jwt_required()
def getpostprodi():
    if request.method == 'GET':
        return ProdiController.getallProdi()
    elif request.method == 'POST':
        return ProdiController.addProdi()


@app.route(routeprodi + '<id_prodi>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def getputdeleteprodi(id_prodi):
    if request.method == 'GET':
        return ProdiController.getoneProdi(id_prodi)
    elif request.method == 'PUT':
        return ProdiController.updateProdi(id_prodi)
    elif request.method == 'DELETE':
        return ProdiController.deleteProdi(id_prodi)


# Endpoint Dosen
routedosen = prefix + 'dosen/'


@app.route(routedosen, methods=['GET', 'POST'])
@jwt_required()
def getpostdosen():
    if request.method == 'GET':
        return DosenController.getallDosen()
    elif request.method == 'POST':
        return DosenController.addDosen()


@app.route(routedosen + '<id_dosen>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def getputdeletedosen(id_dosen):
    if request.method == 'GET':
        return DosenController.getoneDosen(id_dosen)
    elif request.method == 'PUT':
        return DosenController.updateDosen(id_dosen)
    elif request.method == 'DELETE':
        return DosenController.deleteDosen(id_dosen)


# Endpoint Mahasiswa
routemahasiswa = prefix + 'mahasiswa/'


@app.route(routemahasiswa, methods=['GET', 'POST'])
@jwt_required()
def getpostmahasiswa():
    if request.method == 'GET':
        return MahasiswaController.getallMahasiswa()
    elif request.method == 'POST':
        return MahasiswaController.addMahasiswa()


@app.route(routemahasiswa + '<id_mahasiswa>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def getputdeletemahasiswa(id_mahasiswa):
    if request.method == 'GET':
        return MahasiswaController.getoneMahasiswa(id_mahasiswa)
    elif request.method == 'PUT':
        return MahasiswaController.updateMahasiswa(id_mahasiswa)
    elif request.method == 'DELETE':
        return MahasiswaController.deleteMahasiswa(id_mahasiswa)


# Endpoint Tugas Akhir
routetugasakhir = prefix + 'tugasakhir/'


@app.route(routetugasakhir + 'cari/' + '<judul_tugasakhir>', methods=['GET'])
def gettugasakhirclient(judul_tugasakhir):
    return TugasakhirController.getTugasakhirclient(judul_tugasakhir)


@app.route(routetugasakhir, methods=['GET', 'POST'])
@jwt_required()
def getposttugasakhir():
    if request.method == 'GET':
        return TugasakhirController.getallTugasakhir()
    elif request.method == 'POST':
        return TugasakhirController.addTugasakhir()


@app.route(routetugasakhir + '<id_tugasakhir>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def getputdeletetugasakhir(id_tugasakhir):
    if request.method == 'GET':
        return TugasakhirController.getoneTugasakhir(id_tugasakhir)
    elif request.method == 'PUT':
        return TugasakhirController.updateTugasakhir(id_tugasakhir)
    elif request.method == 'DELETE':
        return TugasakhirController.deleteTugasakhir(id_tugasakhir)


# Endpoint Autentikasi
routeadmin = prefix + 'admin/'


# Untuk Inisialisasi Akun Admin Pertama Kali
@app.route(routeadmin + 'setadmin', methods=['GET'])
def setAdmin():
    return AdminController.setAdmin()


@app.route(routeadmin + 'loginadmin', methods=['POST'])
def loginAdmin():
    return AdminController.loginAdmin()


@app.route(routeadmin + 'updateprofile', methods=['POST'])
@jwt_required()
def updateProfile():
    return AdminController.updateProfile()


@app.route(routeadmin + 'updatepassword', methods=['POST'])
@jwt_required()
def updatePassword():
    return AdminController.updatePassword()


@app.route(routeadmin + 'uploadfile', methods=['POST'])
@jwt_required()
def uploadFile():
    return AdminController.uploadFile()
