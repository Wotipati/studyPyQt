# 05Layout.py

#### ウィジェットのレイアウトについて
- Qtでは絶対位置を指定せずに、自動でウィジェットを配置することが可能
- 配置の仕方は縦方向に並べる`QHBoxLayout()`と横方向に並べる`QVBoxLayout()`の2種類がある。
- これらを組み合わせることで複雑な配置も可能

#### レイアウトの流れ
##### 1 配置するウィジェットを作成
```
main_widget = QWidget(self)
self.setCentralWidget(self.main_widget)
```

##### 2 レイアウト用のオブジェクトを作成
```
# 縦方向に並べる場合
layout = QHBoxLayout()
# 横方向に並べる場合
layout = QVBoxLayout()
```

##### 3 レイアウトオブジェクトにウィジェットを追加
```
layout.addWidget(button1)
layout.addWidget(button2)
```

##### 4 メインのウィジェットにレイアウトを追加
```
main_widget.addLayout(layout)
```

---

#### 少し複雑にした場合
```
main_widget = QWidget(self)
self.setCentralWidget(self.main_widget)

# 横方向のレイアウトオブジェクトを作成
layout_row = QVBoxLayout()

# 縦方向のレイアウトオブジェクトを作成
layout_line = QHBoxLayout()

# button1とbutton2を縦方向に配置
layout_line.addWidget(button1)
layout_line.addWidget(button2)

# 上で作成したレイアウト(button1とbutton2が縦に並んだもの)を配置
layout_row.addLayout(layout_line)

# その横にbutton3を配置
layout_row.addWidget(button3)

# それらをwindowに配置
main_widget.addLayout(layout_row)
```
配置の結果

```
button1  
               button3
button2
```
みたいな並びになる
