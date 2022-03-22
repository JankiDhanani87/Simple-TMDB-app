# pylint: disable=invalid-name
from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000, host='0.0.0.0')
