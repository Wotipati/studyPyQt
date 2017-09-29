# 02Button.py

###  QtWidgets

#### sender
- 'QMainWindow.sender()'で直前のシグナルを送ったwidgetを返す
- 返り値はそのオブジェクトのインスタンス
- sender.text()でそのインスタンスのtextプロパティ（ボタンならボタンに表示された文字列）を取得できる

#### QMainWindow
- ウィンドウの構造を持ったクラス
- 以下の5つの領域を持っている
  - MenuBar  
    メニューバーを設置する領域  

  - StatusBar  
    ステータスバーを設置する領域

  - ToolBar  
    アイコンで構成されるようなツールバーを設置する領域

  - DockWidget  
    元のウィンドウの中に設置される補助的なウィンドウのこと

  - CenterWidget  
    GUI部品を設置する領域

---

#### QPushButton
- ボタンのGUIに関するクラス
- QPushButton("button name", ボタンを配置するwidget)でボタンを作成

##### `.setText("new name")`
- 文字の変更

#### `.resize()`
- ボタンのサイズを設定
- 引数を`"buttonName".sizeHint()`とすると、対象のボタンに合わせて大きさを自動で設定してくれる

##### `.clicked`
- ボタンがクリックされた時に呼ばれるSIGNAL

> ##### シグナルとスロットについて
> コールバック関数に変わる新しいオブジェクト間通信の仕組み
>
> ###### シグナルとは  
> 何かが発生したことを他のオブジェクトに通知するための関数のこと  
> - `.clicked`
>   - ボタンがクリックされた際に発生するシグナル
>
> ###### スロットとは
> シグナルに反応して実行される関数
> - `QCoreApplication.instance().quit`
>   - プログラムを終了する関数
>
> 自分で関数を設計してスロットとして設定することもできる
> - `statusButtonClicked()`(自作)
>   - statusBarに、どのボタンが押されたかを表示する関数
>   
> ######  シグナルとスロットの使用
> - `SIGNAL.connect(SLOT)`で実装する  
>   - Qtではシグナルとスロットを`connect`を使って接続する  
>   - これによってシグナルが発生した際に自動でスロットが実行される

---

#### QToolTip
- 吹き出しを追加するクラス
- `"Widget".setToolTip("表示内容")`で設定可能

##### `.setFont(QFont(font, font size))`
- 吹き出しとして表示される文章のフォントと大きさを設定
