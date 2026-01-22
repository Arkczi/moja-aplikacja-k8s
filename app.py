from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <center>
        <h1>Hello World! Pipeline CI/CD dziala poprawnie!</h1>
        <h2>Status projektu: Aktywny (Wersja 2.0)</h2>
        <p>Aplikacja zostala zbudowana przez GitHub Actions i wdrożona w klastrze Kubernetes.</p>
        <hr width="50%">
        <p><i>Ostatnia aktualizacja: 22 stycznia 2026</i></p>
    </center>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
