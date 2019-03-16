import os
from flask import send_from_directory

from . import app


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static(path):
    if path != '' and os.path.exists(f'{app.static_folder}/{path}'):
        return app.send_static_file(path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
