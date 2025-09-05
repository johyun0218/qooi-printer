from waitress import serve
from app import app   # app.py 에 Flask 객체가 app 으로 정의되어 있다고 가정

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5001)
