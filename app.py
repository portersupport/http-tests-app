from flask import Flask, request, response

app = Flask(__name__)

@app.route('/')
def index():
    print(request.headers)
    response.text("Check the console!")

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)
