from flask import jsonify, make_response

def berhasil(values, message):
    respon = {
        'data' : values,
        'message' : message
    }

    return make_response(jsonify(respon)), 200

def gagal(values, message):
    respon = {
        'data' : values,
        'message' : message
    }

    return make_response(jsonify(respon)), 400