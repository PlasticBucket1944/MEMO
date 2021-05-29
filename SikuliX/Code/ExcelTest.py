import  xlrd # excel読み込み用
import  xlwt # excel書き込み用
from xlutils.copy import copy # excelコピー用

# フォーマット情報を引き継いでexcelファイルを呼び出し
base_book = xlrd.open_workbook("C:\SikuliX2.0.4\ExcelTest\sikuliX_test.xlsx", formatting_info=True)

# 書き込み用Workbookオブジェクト作成しベースファイルからコピーする
wt = xlwt.Workbook()
wt = copy(base_book)

# 読み込み用Workbookオブジェクト作成し、シートを指定する
sheet = base_book.sheet_by_name('Sheet1')

num = 0  # テスト番号初期値

for i in range(3, 9):
    print i
    # テスト番号が変更された場合変数に保持する
    if sheet.cell(i, 7).value == 1:
        num = sheet.cell(i, 1).value
    
    # テスト対象ではない場合スキップ
    if sheet.cell(i, 6).value != 1:
        continue

    # 実測値算出
    val = sheet.cell(i, 2).value * 100 * num
    # 実測値書き込み
    wt.get_sheet(0).write(i, 4, val)
    
    # 合否書き込み
    if val == sheet.cell(i, 3).value:
        wt.get_sheet(0).write(i, 5, "OK")
    else:
        wt.get_sheet(0).write(i, 5, "NG")

# 保存処理
wt.save("C:\SikuliX2.0.4\ExcelTest\sikuliX_test_result.xlsx")
