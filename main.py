import os
from app import app

# Explicitely set the secret key to fix the session issue
app.secret_key = os.environ.get("SESSION_SECRET", "moroccan-accounting-secure-key")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
