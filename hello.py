from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    name='SkillChen'
    stuff = 'This is <bold>Bold</bold>'
    fp = ['Pepperoni','Cheese','Orange']
    return render_template('index.html',name=name,stuff=stuff,fp=fp)

@app.route("/user/<name>")
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(errmsg):
    return render_template("error/404.html", errmsg=errmsg)
@app.errorhandler(500)
def page_not_found(errmsg):
    return render_template("error/500.html", errmsg=errmsg)    

if __name__ == '__main__':
    app.run(debug=True)


