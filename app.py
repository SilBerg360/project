import os
from flask import Flask, redirect, render_template, request, jsonify # type: ignore
from sqlalchemy import create_engine, MetaData, Table, Select, bindparam, select # type: ignore

app = Flask(__name__)

engine = create_engine("sqlite:///brein.db", echo=True)

metadata = MetaData()
brein_table = Table("brein", metadata, autoload_with=engine)
stmt = select(brein_table).where(brein_table.c.name.like(bindparam("name"))).limit(5)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    name = request.args.get("name")
    if name:
        with engine.connect() as conn:
            result = conn.execute(stmt, {"name": f"%{name}%"}).all()
            brains = [row[1] for row in result]
    else:
        brains = []
    return jsonify(brains) 

@app.route("/fijnd")
def fijnd():
    name = request.args.get("name")
    if name:
        with engine.connect() as conn:
            result = conn.execute(stmt, {"name": f"%{name}%"}).mappings().first()
            if result:
                brain = dict(result)
            else:
                return render_template("error.html", reason="Invalid input")
        return render_template("fijnd.html", brain=brain)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    