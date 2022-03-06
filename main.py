from flask import Flask
from flask import render_template
from flask import request
import summa.summarizer as sumtx


# only for development purposes
def shutdown_server():
    func = request.environ["werkzeug.server.shutdown"]
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('summa_main.html')


@app.route('/result', methods=['POST'])
def submit():
    summa_res_in  = request.form['text_to_short']
    lang          = request.form['options']
    percentage    = float(request.form['points'])
    summa_res_out = sumtx.summarize(summa_res_in, language=lang, ratio=percentage)
    return render_template('summa_result.html', output=summa_res_out, language=lang, percent=percentage)


#@app.route('/shutdown')
#def shutdown():
#    shutdown_server()
#    return 'Server shutting down...'


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
