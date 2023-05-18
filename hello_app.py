from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloworld():
  return "Hello World!"

if __name__=='__main__':
  app.run(host="52.146.92.195", port=9000, debug=True)
