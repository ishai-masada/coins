from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "dudu"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        session['user'] = user
        return redirect('/')
    if session.get("user") is not None:
        return redirect("/")
    return render_template('login.html')

@app.route('/me')
def me():
    if session.get("user") is None:
        return 'go away'
        return redirect('/login')
    return f'hello, {session.get("user")}'

@app.route('/logout')
def logout():
    session['user'] = None
    return 'logged out'
        
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup', methods=["POST"])
def signup():
    if request.method == "POST":
        return redirect('/signupsuccess')
    return render_template('signup.html')

@app.before_request
def before_request():
    session.permanent = True
    print(session.get('user'))

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
