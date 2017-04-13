from flask import Flask, url_for,render_template
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello World!'

@app.route('/dashboard', methods=['GET'])
def showDashboard():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()