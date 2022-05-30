# auto-genshin
「ネットで有名な画像に原神のロゴを付け加えるとシュールさが増して面白い」という事に気づき、今まで友達と遊んでいましたが、せっかく情報系の学科にいるならと思い制作しました。嘘です。授業中にふと思いついて衝動的に作り始めました。
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
一応OpenCVで記述した部分は残していますが、制作する予定はありません。  

~~とりあえず完成させておきたい機能としましては、~~  
~~- SAVE ASボタンの修正~~  
~~- 出力ファイル名の変更~~  
~~- 出力ファイル拡張子の選択（jpg or png）~~  
~~- floatで記述されている処理時間の表示方法の変更~~  
  ~~- (例) 0.8129487239862　→　0.8 sec~~  

~~となっています。~~  
(5月30日現在)　すべて実装しました。
