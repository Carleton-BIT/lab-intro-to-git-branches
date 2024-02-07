# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request
app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html', comments=comments)


comments = [{"user_name": "applefan", "user_comment": "I like apples more"},
            {"user_name": "jimmy", "user_comment": "This is banana propaganda #cherriesrule"}]

if __name__ == '__main__':
    app.run(debug=True)