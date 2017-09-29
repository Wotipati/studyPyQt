# 01Window.py

### QtWidgets
- Widgetを管理するモジュール
- Widgetはウィンドウ、ボタン、スライドバーなどGUIのインターフェース部分の総称
- Widgetの中にWidjetを埋め込める
    - ウィンドウのWidjetにさらにボタンのWidjetを埋め込んでGUIを作成できる

#### `QApplication(sys.argv)`
- アプリケーションオブジェクトを作成
- QtのGUIプログラム全体をコントロール
- コマンドライン引数を要求するので`sys.argv`を渡す

#### `QWidget()`
- Widget object（画面）を作成する

#### `resize(width, height)`
- windowの横幅、高さの設定

#### `setWindowTitle()`
- ウィンドウタイトルの設定

#### `show()`
- 画面表示

#### `exit(app.exec_())`
- ウィンドウが閉じられた時に、プログラムをクリーンに終了する
