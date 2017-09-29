# 01Window.py

### QtWidgets
- Widgetを管理するモジュール
  - WidgetはGUIのインターフェース部分の総称

#### `QApplication(sys.argv)`
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
