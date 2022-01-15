from flask import Flask
app = Flask(__name__)
# Now define the basic route / and its corresponding request handler:

@app.route("/")
def main():
    return "Welcome!"
# Next, check if the executed file is the main program and run the app:

if __name__ == "__main__":
    app.run()

Priya@180420