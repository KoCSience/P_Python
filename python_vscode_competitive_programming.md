# Pythonで競技プログラミングをするためのVS Code環境構築

## 1. 結論

Pythonで競技プログラミングをするなら、まずは次の構成が最も安定します。

| 項目 | 推奨 |
|---|---|
| エディタ | VS Code |
| Python | AtCoder合わせならPython 3.13系 |
| 速度対策 | PyPy 3.11を追加できるとよい |
| VS Code拡張 | Python、Pylance |
| 実行方法 | VS Code内ターミナルで `python Main.py < input.txt` |
| 自動テスト | 慣れてから `online-judge-tools` と `atcoder-cli` |

AtCoderの2025/10言語一覧では、CPythonは `Python (CPython 3.13.7)`、PyPyは `Python (PyPy 3.11-v7.3.20)`、提出ファイル名はいずれも `Main.py` とされています。

- 出典：AtCoder「使用できる言語とライブラリの一覧 2025/10」
  - https://img.atcoder.jp/file/language-update/2025-10/language-list.html

## 2. 環境構築の方針

### 2.1 最初は標準ライブラリ中心にする

PythonはNumPyやpandasなども使えますが、競プロ対策や就活コーディングテストでは、標準ライブラリだけで書ける力が重要です。

最初に使えるようにするべきものは次です。

- `sys.stdin.readline`
- `collections.deque`
- `collections.Counter`
- `collections.defaultdict`
- `heapq`
- `bisect`
- `itertools`
- `math`

### 2.2 CPythonとPyPyの使い分け

| 実行環境 | 使いどころ |
|---|---|
| CPython 3.13系 | ローカル確認、標準的な提出、NumPy等を使う問題 |
| PyPy 3.11 | 純粋Pythonのループが多く、速度が厳しい問題 |

まずはCPythonで解き、TLEしそうなときにPyPy提出も試す方針で十分です。

## 3. インストール手順

### 3.1 Pythonを入れる

- Python公式
  - https://www.python.org/downloads/

Windowsではインストール時に必ず次を有効にします。

```text
Add python.exe to PATH
```

確認します。

```powershell
python --version
py --version
pip --version
```

複数バージョンを確認する場合は次です。

```powershell
py -0p
py -3.13 --version
```

### 3.2 VS Codeを入れる

- VS Code公式
  - https://code.visualstudio.com/

### 3.3 Python拡張を入れる

VS Code公式ドキュメントでは、Python拡張を使うにはPythonインタプリタを別途インストールする必要があると説明されています。また、Python拡張はIntelliSense、デバッグ、整形、リファクタリングなどを提供します。

- Python in Visual Studio Code
  - https://code.visualstudio.com/docs/languages/python
- Python Extension for VS Code
  - https://marketplace.visualstudio.com/items?itemName=ms-python.python
- Pylance
  - https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance

入れる拡張は次で十分です。

- Python
- Pylance
- Japanese Language Pack for Visual Studio Code。任意。

## 4. フォルダ構成

```text
competitive-programming/
  atcoder/
    abc001/
      a/
        Main.py
        input.txt
      b/
        Main.py
        input.txt
  leetcode/
    two_sum.py
```

AtCoderでは `Main.py`、LeetCodeでは問題ごとの指定形式に合わせます。

## 5. 実行方法

### 5.1 PowerShellでの手動実行

```powershell
python Main.py < input.txt
```

Python 3.13を明示する場合です。

```powershell
py -3.13 Main.py < input.txt
```

PyPyを入れている場合です。

```powershell
pypy3 Main.py < input.txt
```

macOS/Linuxでも基本は同じです。

```bash
python3 Main.py < input.txt
```

## 6. 最小テンプレート

```python
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    print(sum(a))


if __name__ == "__main__":
    main()
```

再帰を使う場合は、必要に応じて次を追加します。

```python
sys.setrecursionlimit(10**7)
```

ただし、Pythonの深い再帰は環境差や速度の問題が出やすいため、DFSはスタックで書く選択肢も持つと安全です。

## 7. 入力パターン集

### 整数1個

```python
n = int(input())
```

### 整数2個

```python
a, b = map(int, input().split())
```

### 配列

```python
a = list(map(int, input().split()))
```

### N行の整数

```python
n = int(input())
a = [int(input()) for _ in range(n)]
```

### N行2列

```python
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
```

## 8. VS Codeの任意設定

`.vscode/settings.json` の例です。

```json
{
  "python.defaultInterpreterPath": "python",
  "python.analysis.typeCheckingMode": "basic",
  "editor.formatOnSave": true
}
```

ただし、競プロでは整形・型チェックを強くしすぎるより、提出可能なコードを素早く書けることを優先します。

`.vscode/tasks.json` の例です。

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Python: run with input.txt",
      "type": "shell",
      "command": "python Main.py < input.txt",
      "problemMatcher": [],
      "options": {
        "cwd": "${fileDirname}"
      }
    }
  ]
}
```

## 9. 自動テストを入れる場合

慣れてきたら、次の2つを入れるとサンプル取得とローカルテストが楽になります。

- online-judge-tools
  - https://github.com/online-judge-tools/oj
- atcoder-cli
  - https://github.com/Tatamo/atcoder-cli

導入例です。

```powershell
pip install online-judge-tools
npm install -g atcoder-cli
```

使い方例です。

```powershell
acc new abc467
cd abc467/a
oj test -c "python Main.py" -d tests
```

PyPyでテストする場合です。

```powershell
oj test -c "pypy3 Main.py" -d tests
```

## 10. NumPyについて

AtCoderのCPython環境にはNumPyなど多くのライブラリが入っています。ただし、就活コーディングテストではNumPyが使えないこともあります。

| 方針 | 判断 |
|---|---|
| 初期学習 | NumPyなしで標準ライブラリ中心 |
| AtCoderの特殊問題 | 必要ならNumPyを検討 |
| LeetCode等 | 標準Python中心が安全 |

最初からNumPy前提にすると、アルゴリズムやデータ構造の理解が弱くなる可能性があります。

## 11. 妥当性の検討

| 観点 | 判断 |
|---|---|
| AtCoderとの整合性 | Python 3.13系とPyPy 3.11を用意すれば現行環境に近い |
| 学習効率 | VS Codeは軽く、単一ファイル運用に向く |
| コーディングテスト適性 | 標準ライブラリ中心なら応用しやすい |
| 保守性 | `Main.py` と `input.txt` だけなら壊れにくい |
| リスク | Pythonバージョン混在、PyPy未導入、NumPy依存に注意 |

結論として、Python競プロでは `VS Code + Python 3.13系 + Pylance + ターミナル実行` が最も扱いやすい構成です。

## 12. 今来三行

Python競プロは、VS Codeで `Main.py` を書き、`python Main.py < input.txt` で回すのが安定です。  
AtCoderに合わせるならPython 3.13系を基本にし、速度が厳しければPyPy 3.11を試します。  
NumPyや自動テスト環境は最初から必須ではなく、標準ライブラリと手動実行に慣れてから追加するのが安全です。
