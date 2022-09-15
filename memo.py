import os
  
# ファイルを開く;  もし失敗したとき、早くエラーがわかるから。
filename = 'memo.txt'
f = open(filename,'w')
  
# 「入力してください」メッセージを表示する & メモを入力する
memo = 'ALOHA！\n僕たちはIG12クラスです。\nよろしく。\n'
# ファイルにメモを書く
f.write(memo)
  	
# ファイルを保存する
f.close()	