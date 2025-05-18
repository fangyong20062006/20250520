from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('FLASK_DB_USER', 'flask_app')}:{os.getenv('FLASK_DB_PASSWORD', 'strong_password')}@localhost:5432/{os.getenv('FLASK_DB_NAME', 'testdb')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/add_user/')
def add_user():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': '请提供 name 参数'}), 400
    try:
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'status': 'ok',
            'user_id': user.id,
            'created_at': user.created_at.isoformat()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'数据库操作失败：{str(e)}'}), 500


if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("数据库初始化完成")
        except Exception as e:
            print(f'初始化数据库失败：{str(e)}')
    app.run(host='0.0.0.0', port=5000,debug=True,threaded=True)