from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def get_count():
    if "count" not in session:
        session["count"] = 0   
    else:
        session['count'] += 1
    return render_template("index.html")


@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] +=1
    return redirect('/')

#wasn't able to get the custom value but gave it a shot!
# @app.route('/custom_value')
# def custom(input):
#     if "count" not in session:
#         session["count"] = 0
#     else:
#         session["count"] += input
#     return redirect('/',input={})

if __name__=="__main__":
    app.run(debug=True)