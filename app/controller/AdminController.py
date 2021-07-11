from datetime import timedelta
from app.model.admin import Admin
from app import response, app, db, uploadconfig
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
import uuid
from werkzeug.utils import secure_filename
import os


def setAdmin():
    try:
        username_admin = "admin"
        password_admin = "admin"
        nama_admin = "Admin"
        foto_admin = "admin/admin.jpg"

        admin = Admin(username_admin=username_admin,
                      nama_admin=nama_admin, foto_admin=foto_admin)
        admin.setPassword(password_admin)
        db.session.add(admin)
        db.session.commit()
        return response.berhasil([], "Berhasil Menambah Akun Admin")
    except Exception as e:
        print(e)
        return response.gagal([], "Gagal Menambah Akun Admin")


def loginAdmin():
    try:
        username_admin = request.form.get('username_admin')
        password_admin = request.form.get('password_admin')

        admin = Admin.query.filter_by(username_admin=username_admin).first()
        if not admin:
            return response.gagal([], "Username Tidak Terdaftar")

        if not admin.checkPassword(password_admin):
            return response.gagal([], "Kata Sandi Salah")

        data = singleObject(admin)

        masa_aktif_token = timedelta(days=7)
        masa_refresh_token = timedelta(days=7)

        token = create_access_token(
            data, fresh=True, expires_delta=masa_aktif_token)
        refresh_token = create_refresh_token(
            data, expires_delta=masa_refresh_token)

        return response.berhasil({
            "data": data,
            "token": token,
            "refresh_token": refresh_token
        }, "Berhasil Login Admin")
    except Exception as e:
        print(e)
        return response.gagal([], "Gagal Login Admin")


def updateProfile():
    try:
        data_token_admin = get_jwt_identity()
        id_admin = data_token_admin.get('id_admin')
        username_admin = data_token_admin.get('username_admin')

        admin = Admin.query.filter_by(
            id_admin=id_admin, username_admin=username_admin).first()

        nama_admin = request.form.get('nama_admin')
        foto_admin = request.form.get('foto_admin')

        admin.nama_admin = nama_admin
        admin.foto_admin = foto_admin

        db.session.commit()

        return response.berhasil([], "Berhasil Mengubah Profil Admin")
    except Exception as e:
        return response.gagal([], "Gagal Mengubah Profil Admin")


def updatePassword():
    try:
        password_admin_lama = request.form.get('password_admin_lama')
        password_admin_baru = request.form.get('password_admin_baru')
        password_admin_baru2 = request.form.get('password_admin_baru_2')

        if password_admin_baru != password_admin_baru2:
            return response.gagal([], "Pastikan Password Baru Sama")

        data_token_admin = get_jwt_identity()
        id_admin = data_token_admin.get('id_admin')
        username_admin = data_token_admin.get('username_admin')

        admin = Admin.query.filter_by(
            id_admin=id_admin, username_admin=username_admin).first()

        if not admin.checkPassword(password_admin_lama):
            return response.gagal([], "Pastikan Kata Sandi Lama Benar")

        admin.setPassword(password_admin_baru)
        db.session.commit()

        return response.berhasil([], "Berhasil Mengubah Kata Sandi Admin")
    except Exception as e:
        print(e)
        return response.gagal([], "Gagal Mengubah Kata Sandi Admin")


def singleObject(admin):
    data = {
        'id_admin': admin.id_admin,
        'username_admin': admin.username_admin,
        'nama_admin': admin.nama_admin,
        'foto_admin': admin.foto_admin,
        'created_at': admin.created_at,
        'updated_at': admin.updated_at
    }
    return data


def uploadFile():
    try:
        if 'file' not in request.files:
            return response.gagal([], "Pastikan File Sudah Dipilih")

        file = request.files['file']

        if file.filename == '':
            return response.gagal([], "Pastikan File Sudah Dipilih")

        if file and uploadconfig.cek_ekstensi(file.filename):
            uid = uuid.uuid4()
            namafile = secure_filename(file.filename)
            ubah_namafile = "Flask-"+str(uid)+namafile

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], ubah_namafile))

        return response.berhasil({"nama_file": ubah_namafile}, "Berhasil Mengupload File")
    except Exception as e:
        return response.gagal([], "Gagal Mengupload File")
