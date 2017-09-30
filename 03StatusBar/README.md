# 03StatusBar.py

#### QMainWindow.statusBar
- widgetのステータスバー領域に関するクラス

##### .showMessage(str)
- 設置されたステータスバーに文字を表示する

---

#### QtCore
- コアとなるGUI向け以外のクラスを保持する

#### QtCore.QTimer
- タイマーイベントに関するクラス

##### `.timeout`
- タイマーのカウントが終わった時にシグナルを発生させる関数

##### `.start(msec)`
- タイマーをスタートさせる関数
- 引数の単位はミリ秒
