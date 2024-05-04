from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test3')
def hello_vct():
    name = 'md'

    return render_template('index.html', index_variable=name)

app.run(debug=True)