from flask import Flask, render_template, request

#appを作る
app = Flask(__name__)

#routeを作る
@app.route('/')
def start():
    return 'Hi MU'

#メッセージを入力するページのrouteを作る
@app.route('/msg')
def msg():
    return render_template('msg.html')

#もらったメッセージを、表示するためのrouteを作る
@app.route('/output', methods=['POST'])
def output():
    #データをもらう；名前はmsg
    msg = request.form['msg']

    #データについて考える; もし Hello だったら、日本語で表示する
    if msg=='Hello':
        kekka = 'こんにちは'
    else:
        kekka = msg


    #データを出力する
    return kekka




#実行する（必ず、一番下に書く）
if __name__=='__main__':
    app.run(debug=True)
