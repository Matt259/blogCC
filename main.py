from flask import Flask, render_template
#from werkzeug.exceptions import HTTPException
app = Flask(__name__)

@app.route('/')
def Index():
    #try:
    return render_template("index.html")
    #except Exception as e:
       # return "no work"
if __name__ == "__main__":
    
    app.run()