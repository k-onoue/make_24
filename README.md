# 24 を親ノードにしたほうがよい

- 24 を親ノードにして，3, 3, 8, 8, と演算子４つを下に追加して depth が 9 になったら一度に評価し ＝＝ 0 なら成功

# 条件の整理

- nums は縦バインド + 同親横バインド
- ops は同親横バインドのみ

# そもそも移動は上か下かしかないのかも（右はなし）

- 下に移動（自然に addnode）
- 上に移動（addnode できないので上に移動，そこでもできないのであればまた上に移動）

# addnode 不可能の条件とは

- 最深部にいる
- 

もしくは tree_sub は deepcopy と 参照渡し を上手に使い分ける

ー＞ tree_sub のノードが空リストならば ＝＞ 上に移動
ー＞ tree_sub 要らないかも ~~リストだけでいけそう~~ スタックでリストを積み上げるべきじゃないか
ー＞ tree_counter は必要

# 副作用の出る書き方を避けないと処理の理解が追いつかなくなる

# 1 ステップ下に動かすとはどういうことか

- tree_main ノードが１つ増える．
- tree_counter のノードが１つ増える．
- stack に１つのせる
- location のサイズが１つ増える

入力 

# グローバル変数を有効的に使うと関


[24, 5, 6, 7, 8] {+, -, *, /}


24, ([5, 6, 7, 8], []), 1
24 -> 5, ()


# やはり ツリーが ３つ要る
tree_main の n 階層目のノード要素 イコール tree_sub の n-1 階層目のノード

# 先幅優先でツリーの構築をすればよいかも

# ツリーは一つでよい。代わりに属性をもたせる（カウンターと残りの値）


```
class SimpleStack:
  maxsize = 100 #default stack size
  def __init__(self):
    self.top=0
    self.body=[None] * self.maxsize # Make list of 'None' with maxsize

  def push(self,val):
    self.body[self.top]=val
    self.top = self.top + 1 # increment stack pointer.
    return self

  def pop(self):
    if self.top == 0:
      return None # Stack is already empty
    self.top = self.top -1 # decrement stack pointer.
    return self.body[self.top]
# class end

# Let's test our 'SimpleStack'
s = SimpleStack()
for i in range(100):
  s.push(i)

print(s.pop(),s.pop(),s.pop(),s.pop(),s.pop(),s.pop())
```

return self

# 特定の親を持つノード同士で互いに参照できると便利かもしれない


# データ構造とアルゴリズムに詳しくなってから再チャレンジする


https://zenn.dev/fjnkt98/articles/1324f0ef26a093






