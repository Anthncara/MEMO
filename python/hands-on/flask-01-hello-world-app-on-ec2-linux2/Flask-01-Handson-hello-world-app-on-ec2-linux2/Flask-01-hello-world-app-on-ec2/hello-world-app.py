from Flask import Flask

app = Flask(__name__)

@approute("/")
def hello():
    return "Hello World !"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=80)
