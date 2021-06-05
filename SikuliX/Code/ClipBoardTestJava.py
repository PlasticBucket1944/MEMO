# -*- coding: utf-8 -*-
from java.awt import Toolkit
from java.awt.datatransfer import Clipboard
from java.awt.datatransfer import DataFlavor
from java.awt.datatransfer import StringSelection

# クリップボード操作用インスタンス作成
toolkit = Toolkit.getDefaultToolkit()
clipboard = toolkit.getSystemClipboard()

# クリップボードの値取得
contents = clipboard.getContents(None)
hoge = contents.getTransferData(DataFlavor.stringFlavor)
print hoge.encode('utf_8') # 日本語を出力できるようにエンコード

# クリップボードに値を設定 日本語は無理
clipboard.setContents(StringSelection('hoge'), None)
