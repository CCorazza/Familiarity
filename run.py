# Run a test server.
from Flaskapp import app
app.run(host='localhost', port=5000, debug=True)