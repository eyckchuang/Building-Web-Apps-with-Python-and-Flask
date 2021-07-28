from flask.views import MethodView
from flask import Flask, request, jsonify
from models import Books, db


class BookAPI(MethodView):

    def get(self, id):
        if id is None:
            res = Books.query.all()
            lb = []
            for i in res:
                s = i.serialize()
                lb.append(s)
            return jsonify({"books": lb})
        else:
            res = Books.query.filter_by(bookID=id).first()
            book = res.serialize()
            return jsonify({"book": book})

    def post(self):
        book = Books(request.json['bookID'], request.json['title'], request.json['Author'], request.json['price'])
        db.session.add(book)
        db.session.commit()
        res = Books.query.all()
        lb = []
        for i in res:
            s = i.serialize()
            lb.append(s)
        return jsonify({"books": lb})

    def delete(self, id):
        res = Books.query.filter_by(bookID=id).first()
        db.session.delete(res)
        db.session.commit()
        res = Books.query.all()
        lb = []
        for i in res:
            s = i.serialize()
            lb.append(s)
        return jsonify({"books": lb})

    def put(self, id):
        id = request.json['bookID']
        price = request.json['price']
        res = Books.query.filter_by(bookID=id).first()
        res.price = price
        db.session.commit()
        book = res.serialize()
        return jsonify({'book': book})
