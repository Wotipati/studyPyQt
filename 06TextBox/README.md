#06TextBox.py

#### QtWidgets.QLineEdit
- テキストボックスを実装するクラス

##### `.text()`
- テキストボックスの中身(str)を返す

##### `.textchanged`
- テキストボックスの中身が書き換えられた時に中身の文字列(str)を返すシグナル

##### `.setText(str)`
- テキストボックスに文字を表示させる

##### `.clear()`
- テキストボックスの内容を削除


#### QtWidgets.QTextEdit
- 複数行のテキストボックスを実装するクラス

#### `.append(str)`
- 改行し，テキストボックスに引数の文字列を書き加える
