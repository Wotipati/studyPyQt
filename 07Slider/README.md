# 07Slider.py

#### QtWidgets.QSlider
- スライダーを実装するクラス

##### `QSlider()`
- 垂直方向のスライダーを作成

##### `QSlider(Qt.Horizontal)`
- 水平方向のスライダーを作成

##### `QSlider.valueChanged[int]`
- スライダーで設定された値を一緒に返すシグナル
- `[int]`で数字の型を設定

##### `Qslider.setRange(start, end)`
- スライダーの始点と終点の値を設定

##### `QSlider.setValue()`
- スライダーの位置を設定

##### `QSlider.setTickPosition(position)`
- スライダーのメモリの位置を設定
    - `QSlider.TicksBelow`
    - `QSlider.TicksAbove`
    - `QSlider.TicksBoth`
    - `QSlider.TicksRight`
    - `QSlider.TicksLeft`
    - `QSlider.NoTicks`

---

#### QtGui.QPixMap
- 画像を挿入するクラス

```
# 挿入する画像の選択
pixmap = QPixmap("path")

# 大きさの変更
pixmap_resized = pixmap.scaled(width, height)

# ラベルに画像を貼り付ける
label = QLabel
label.setPixmap(pixmap_resized)

# ラベルを配置する
main_layout.addWidget(label)
```
