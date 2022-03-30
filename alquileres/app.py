
import traceback
from flask import Flask, request, jsonify, render_template, Response, redirect
import departamentos
import graficos

# Crear app
app = Flask(__name__)

# De donde leer la BD
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///departamentos.db"
# Asociar controlador de la BD con la aplicación
departamentos.db.init_app(app)
app.app_context().push()

@app.route("/")
def index():
    try:

        return render_template("index.html")

    except:
        return jsonify({"trace": traceback.format_exc()})


@app.route("/alquileres", methods=["GET", "POST"])
def alquileres():
    if request.method == "GET":
        try:
            limit_str = str(request.args.get("limit"))
            offset_str = str(request.args.get("offset"))

            limit = 0
            offset = 0

            if (limit_str is not None) and (limit_str.isdigit()):
                limit = int(limit_str)

            if (offset_str is not None) and (offset_str.isdigit()):
                offset = int(offset_str)

            data = departamentos.total_alquileres(limit, offset) 
            
            return render_template("tabla.html", data=data)

        except:
            return jsonify({"trace": traceback.format_exc()})
    
    if request.method == "POST":
        try:
            ciudad = str(request.form.get("ciudad"))
            departamentos.db.drop_all()
            departamentos.db.create_all() 
            departamentos.insertar_depto(ciudad) 

            data = departamentos.total_alquileres()

            return render_template("tabla.html", data=data)

        except:
            return jsonify({"trace": traceback.format_exc()})


@app.route("/alquileres/en_pesos")
def alquileres_en_pesos():
    try:
        limit_str = str(request.args.get("limit"))
        offset_str = str(request.args.get("offset"))

        limit = 0
        offset = 0

        if (limit_str is not None) and (limit_str.isdigit()):
            limit = int(limit_str)

        if (offset_str is not None) and (offset_str.isdigit()):
            offset = int(offset_str)

        data = departamentos.total_por_moneda("ARS", limit, offset)

        return render_template("tabla.html", data=data)

    except:
        return jsonify({"trace": traceback.format_exc()})

@app.route("/alquileres/en_dolares")
def alquileres_en_dolares():
    try:
        limit_str = str(request.args.get("limit"))
        offset_str = str(request.args.get("offset"))

        limit = 0
        offset = 0

        if (limit_str is not None) and (limit_str.isdigit()):
            limit = int(limit_str)

        if (offset_str is not None) and (offset_str.isdigit()):
            offset = int(offset_str)

        data = departamentos.total_por_moneda("USD", limit, offset)

        return render_template("tabla.html", data=data)
    except:
        return jsonify({"trace": traceback.format_exc()})


@app.route("/comparativa")
def comparativa():
    try:
        x = departamentos.reporte()
        image_html = graficos.graficar(x)
        return Response(image_html.getvalue(), mimetype="image/png")
    except:
        return jsonify({"trace": traceback.format_exc()})


@app.route("/comparativa/pesos")
def comparativa_pesos():
    try:
        x = departamentos.reporte_pesos()
        image_html = graficos.graficar(x)
        return Response(image_html.getvalue(), mimetype="image/png")
    except:
        return jsonify({"trace": traceback.format_exc()})

@app.route("/comparativa/dolares")
def comparativa_dolares():
    try:
        x = departamentos.reporte_dolares()
        image_html = graficos.graficar(x)
        return Response(image_html.getvalue(), mimetype="image/png")
    except:
        return jsonify({"trace": traceback.format_exc()})


@app.before_first_request
def before_first_request():
    # Borrar y crear la BD
    departamentos.db.drop_all()
    departamentos.db.create_all() 
    # Completar BD
    departamentos.insertar_depto("Argentina")  
    print("Base de datos generada") 



if __name__ == "__main__":
    # Lanzar server
    app.run(host="127.0.0.1", port=5000)