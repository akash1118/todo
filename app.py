from flask import Flask, render_template
app = Flask(__name__)
# Now define the basic route / and its corresponding request handler:

@app.route("/")
def main():
    return render_template('index.html')
# Next, check if the executed file is the main program and run the app:

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug = True)

