from flask import Flask, render_template, request, redirect
import sql as SQL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET'])
def submit():
    if 'shorturl' in request.args and 'longurl' in request.args:
        shorturl = request.args['shorturl']
        longurl = request.args['longurl']
        data = {'shorturl': shorturl,
                'longurl': longurl }
        return SQL.add_url(data)
    else:
        return 'no urls received.'

@app.errorhandler(404)
def not_found_error(error):
    endpoint = request.path
    longurl = SQL.get_url(endpoint[1:])
    if longurl != 'No Results':
        return redirect(longurl)
    else:
        return render_template('no_results.html')

if __name__ == '__main__':
    app.run()