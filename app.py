from website import *

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8000)