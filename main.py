from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_sqlalchemy import SQLAlchemy



#html path
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')




app = Flask(__name__, template_folder=template_path)


app.secret_key = os.urandom(12)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#table creation class
class Data(db.Model):
    
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    fullname = db.Column(db.String(100))
    date = db.Column(db.Date())
    picture_url = db.Column(db.String(100))
    comment = db.Column(db.String(500))
    
    def __init__(self, fullname, date, picture_url, comment):
        self.fullname=fullname 
        self.date=date 
        self.picture_url=picture_url 
        self.comment=comment 



@app.route('/')
def return_index():
    all_data = Data.query.all()
    return render_template("index.html", blogs = all_data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        fullname = request.form['fullname']
        name_validation = len(fullname.split()) #validates that the username input has atleast 2 names
        if name_validation >= 2:
            date = request.form['date']
            pic_url = request.form['pictureURL']
            comment = request.form['comment']
            blog = Data(fullname, date, pic_url, comment)
            db.session.add(blog)
            db.session.commit()
            flash("Blog saved", "info")
            return redirect(url_for('return_index'))
        else:
            flash("Both names are required")
            return redirect(url_for('return_index'))

@app.route('/delete/<int:id>/')
def delete(id):
    data = Data.query.get(id)
    db.session.delete(data)
    db.session.commit()
    flash("Blog deleted")
    return redirect(url_for('return_index'))

@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        print(id)
        my_data = Data.query.get(id)
        my_data.fullname = request.form['edit-fullname']
        my_data.date = request.form['edit-date']
        my_data.picture_url = request.form['edit-pictureURL']
        my_data.comment = request.form['edit-comment']
        
        db.session.commit()
        flash("Updated")
        return redirect(url_for('return_index'))
        
        
if __name__ == "__main__":
    app.run()
    