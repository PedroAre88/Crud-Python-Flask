from app import app
from contacts import contacts

app.register_blueprint(contacts)

# Iniciar app
if __name__ == "__main__":
    app.run(port=5000, debug=True)