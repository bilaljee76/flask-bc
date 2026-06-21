from flask import Flask

from routes.main_route import main
from routes.student_route import student
from routes.predict_route import predict

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(student)
app.register_blueprint(predict)

if __name__ == "__main__":
    app.run(debug=True)