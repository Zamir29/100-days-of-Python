from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cv/zamir')
def cv():
    return render_template('cv/zamir.html')

def main():
    app.run(debug=True) #, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()