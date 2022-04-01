import json
import sqlite3
import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import api
db = SQLAlchemy()


class Departamento(db.Model):
    __tablename__ = "departamento"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    currency_id = db.Column(db.String)
    city = db.Column(db.String)
    condition = db.Column(db.String)
    location = db.Column(db.String)

    def __repr__(self):
        return f"Propiedad [Precio: {self.price}, Moneda: {self.currency_id}, Ciudad: {self.city}, Condicion {self.condition}, Direccion {self.location}]\n"


def insertar_depto(provincia):
    data = api(provincia)
    
    for i in data:
        depto = Departamento(price=i["price"], currency_id=i["currency_id"], city=i["address"]["city_name"], condition=i["condition"], location=i["location"]["address_line"])
                                                                                                                                     
        db.session.add(depto)
        db.session.commit()


def total_alquileres(limit=0, offset=0):
    query = db.session.query(Departamento)
    if limit > 0:
        query = query.limit(limit)
        if offset > 0: 
            query = query.offset(offset)

    json_list = []
    # Armar el diccionario
    for departamento in query:
        result = {"id":departamento.id, "price":departamento.price, "currency_id":departamento.currency_id, "city":departamento.city, "location":departamento.location, "condition":departamento.condition}
        json_list.append(result)
    return json_list


def total_por_moneda(currency, limit=0, offset=0):
    query = db.session.query(Departamento).filter(Departamento.currency_id == currency)
    if limit > 0:
        query = query.limit(limit)
        if offset > 0: 
            query = query.offset(offset)

    json_list = []
    # Armar el diccionario
    for departamento in query:
        result = {"id":departamento.id, "price":departamento.price, "currency_id":departamento.currency_id, "city":departamento.city, "location":departamento.location, "condition":departamento.condition}
        json_list.append(result)
    return json_list


def reporte():
    x = {}
    
    result = db.session.query(Departamento).filter(Departamento.currency_id == "ARS").count()
    x["En pesos"] = result

    result = db.session.query(Departamento).filter(Departamento.currency_id == "USD").count()
    x["En dolares"] = result

    return x


def reporte_pesos():
    query = db.session.query(Departamento).filter(Departamento.currency_id == "ARS")
    a = [depto.price for depto in query if depto.price > 90000]
    b = [depto.price for depto in query if 35000 < depto.price < 90000]
    c = [depto.price for depto in query if depto.price < 35000]
    
    comparacion = {"Mas de $90.000": len(a), "Entre $90.000 y $35.000": len(b), "Menos de $35.000": len(c)}

    return comparacion
    
def reporte_dolares():
    query = db.session.query(Departamento).filter(Departamento.currency_id == "USD")
    a = [depto.price for depto in query if depto.price > 3500]
    b = [depto.price for depto in query if depto.price < 3500 ]
    
    comparacion = {"Mas de 3.500 USD": len(a), "Menos de 3.500 USD": len(b)}

    return comparacion
    
    
if __name__ == "__main__":
    insertar_depto()
    cantidad_deptos()