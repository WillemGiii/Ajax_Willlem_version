from flask import Flask, render_template
from routes.api import api_bp
# 建立Flask 物件
app = Flask(__name__)


@app.route('/home')
def index():
    return render_template('home.html')

# 註冊 Blueprint
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    # 啟動 Application
    app.run(debug=True)