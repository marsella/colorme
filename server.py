from flask import Flask
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
app = Flask(__name__)

@app.route('/')
def start():
  return artist('beyonce')

@app.route('/<string:artist>')
def artist(artist):
  return render_template('index.html', artist=artist)


if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')


