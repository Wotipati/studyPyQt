# 04MenuBarToolBar.py

#### QtWidgets.QAction
- トリガー/チェック可能なUI要素を抽象化したもの
- 通常メニューバーやツールバーに配置する
- ユーザの操作により`triggered()`や`toggled()`などのシグナルを発生させる
- QActionオブジェクトには以下のような属性を設定可能
  - `QAction("icon", "name", self)`
    - `"icon"`...アイコンを設定
    - `"name"`...テキスト
    - `self`...配置先のwidget

  - ``.setShortcut(`keymap`)``
    - ショートカットキーを設定
    - ex) ``.setShortcut(`Ctrl+Q`)``

  - ``.setStatusTip(`Tips`)``
    - ステータスバーに表示するTipsを設定
    - カーソルが上に来た時にTipsがステータスバーに表示される

  - ``.triggered.connect(`SLOT`)``
    - クリックされた時に発生するシグナル

  - ``.toggled.connect(`SLOT`)``
    - トグルされた時に発生するシグナル


##### MenuBarへの配置
```py3:sample
  from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QStyle
  from PyQt5.QtCore import QCoreApplication


  # アイコンの設定
  exit_gui = QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton)
  # QActionオブジェクトの作成
  exit_action = QAction(exit_gui, '&Exit', self)
  # シグナルとスロットの連携
  exit_action.triggered.connect(QCoreApplication.instance().quit)

  # メニューバーの作成
  menubar = self.menuBar()
  # メニューバーに"File"という名前のメニューを追加
  file_menu = menubar.addMenu('&File')
  # "File"メニューに上で設定したQActionオブジェクト(exit_action)を追加
  file_menu.addAction(exit_action)
```


##### ToolBarへの配置
```python3:sample
  from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QStyle
  from PyQt5.QtCore import QCoreApplication


  exit_gui = QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton)
  exit_action = QAction(exit_gui, '&Exit', self)
  exit_action.triggered.connect(QCoreApplication.instance().quit)

  qt_info_gui = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
  qt_info_action = QAction(qt_info_gui, '&about Qt', self)
  qt_info_action.triggered.connect(QCoreApplication.instance().quit)

  # ツールバーの作成
  toolbar = self.addToolBar('&toolbar')
  # ツールバーに上で設定したQActionオブジェクト(exit_action)を追加
  toolbar.addAction(exit_action)

  # 別のツールバーの作成
  toolbar2 = self.addToolBar('&tooooolbar')
  # ツールバーに上で設定したQActionオブジェクト(qt_info_action)を追加
  toolbar2.addAction(qt_info_action)
```
