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

##### MenuBarへの配置
