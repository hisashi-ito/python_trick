### モジュールのロードを相対パスでうまくやる 
よくモジュール、ここでは１つのクラスを実装したりする場合にそのクラスから更に別のクラスを `import` することが多い。

実装が完了して、いざ作ったクラスで動作確認したい場合とかはそのクラスの下にUT用の簡単なコードを書いて試したりすることが多いと思う（俺はやる）

単体の動作確認ができて、いざ本番としてそのクラスが上位のプログラムから`import` される場合は pythonの場合はloadされるパスの記述方法に差がでてくる。どこがcurrentになるかが違うわけだ。(これがめんどい）

そこで、単一のクラスのデバッグ時と上位のコマンドから利用される場合でloadパスを変更したりして対応することがあったのだが、以下のように記述することで問題が解決するtrickを紹介。（ソースを触らない）

#### ディレクトリ構造
今のディレクトリ構造を以下のように定める。
```text
.
|-- main.py
`-- module
    |-- child.py
    `-- parent.py
```
#### child.py
module 配下に保存された child.py が今作ったプログラムである。ここで
```python
try:
    from . parent import Parent
    print(". のほうが呼ばれたよ")
except:
    print(".なしが呼ばれたよ")
    from parent import Parent

class Child(Parent):
    def __init__(self):
        super().__init__()


# 作ったクラスのファイルをそのまま起動した場合
# UTとかでよく利用する
if __name__ == '__main__':
    Child()
```
のように記述する。import のところがtrick。UTを実施したい場合は　Parent が 同階層として扱われる。
```bash
$ cd module/
$ python3 ./child.py
.なしが呼ばれたよ
```
#### main.py
メイン関数として `main.py` として以下のように実装する。この場合は、相対パス記述で呼ばれる。
```python
from module.child import Child
Child()
```
```bash
$ python3 ./main.py
. のほうが呼ばれたよ
```
このように２種だけであるが、`child.py` の自分自身を実行する場合と `main.py` のように外部から呼ばれる場合でフレキシブルに記述できる。（便利）
