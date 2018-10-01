from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
	return redirect(url_for('index'))

if __name__ == "__main__":
	# app.debug = True
	app.run()