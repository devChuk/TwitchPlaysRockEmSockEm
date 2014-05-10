from flask import Flask, redirect, url_for, render_template, request, session
app = Flask(__name__)
app.secret_key = 'rockemsockem'

@app.route('/')
def main():
    if 'username' in session:
        name = session['username']
        return render_template('main.html', name=name)
    else:
        return redirect(url_for('login'))

@app.route('/red')
def red():
    return render_template('red.html')

@app.route('/blue')
def blue():
    return render_template('blue.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('main'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug = True)

