import os
  
# ファイルを開く
filename = 'memo.txt'
f = open(filename, 'w')
  
# 「入力してください」( = input memo> )　を表示する
memo = input('input memo> ')
  
# ファイルに、メモを書く
f.write(memo)
  
# ファイルを保存する
f.close()