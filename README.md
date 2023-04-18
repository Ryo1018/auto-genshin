# auto-genshin
This software automatically generates screenshot-like images of Genshin.  
  
  
  
## 作成した経緯
友人同士の遊びから

## 使用したライブラリ・環境
Windows10 21H1 64bit

Python 3.10.4  
PIL  
tkinter  

## 使用方法
autoGendhin.7zをダウンロードし解凍してください。この際に、picフォルダとautoGenshin.exeは同ディレクトリに配置してください。  
  
1.[OPEN FILE]をクリックしファイルを選択する  
2.[RUN]ボタンを押す  
3.[RUN]ボタンの上に「ProcessTime : 0.xxx sec」と出たら完了  

~~※ __[SAVE AS]ボタンはバグが有るため正常に動作しません。（後日改良予定）__~~  
※ __初期状態では/Users/<自分のユーザー名>/Picturesに保存されています。__  

### 追記
最初はPILではなく、OpenCVを使って画像の合成を行うつもりでしたが、原神のロゴがアルファチャンネル（透過画像）だったためコードの記述量が更に増えると思いPILに変更しました。
一応OpenCVで記述した部分は残しています。

### 最後に
main.py, controller.py, view.pyとあるように、本来はファイルを分けてメンテナンスしやすくする予定でしたが、過去に自分が作った時と違ってうまく動作できませんでした。
不具合の原因を見つけるのも勉強になるため取り掛かろうと思いましたが、まずはリリースしたほうが色々な人に使ってもらえて面白そうだと思ったため、このプロジェクトではこれ以上弄らずに自分自身の今後の課題にしようと思います。
