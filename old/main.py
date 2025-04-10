# flask run --debug --port 5001
from flask import Flask

# 입구 파일을 하나 만들어줍니다.
app = Flask(__name__)



if __name__ == '__main__' :
    app.run(debug=True, port=5001)