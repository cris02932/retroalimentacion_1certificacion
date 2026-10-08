from flask_app import app

@app.route("/cine"):
def cine():
    return render_template('cine.html')