id = input('IDを入力してください:')
print(id)

pwd = input('パスワードを入力してください:')
print(pwd)

# データファイル( aloha.txt )を開いて、データをもらう
file = open('fileio.txt', 'r')

# フラグ( flag )を準備する
flag = 0
  
# 1行ずつ、データをもらう & IDとパスワード確認する
for line in file:
    if id in line and pwd in line:
        # OKのとき
        flag = 1
        break			# OKなら、確認終わり！
    else:
          # 違う時
        flag = 0
  
  # 「OK」か、「違います」か、ここで、1回だけ、表示する
if flag==1:
    print('IDとパスワード、OKです。')
else:
    print('IDかパスワードが、違います!')
  
  # ファイルを閉じる
file.close()
  

