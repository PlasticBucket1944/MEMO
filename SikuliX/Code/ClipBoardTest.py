# 指定したセルにジャンプ
def JumpTo(row, col):
    type(Key.F5)
    type(Key.DELETE)
    type(Key.DELETE)
    paste(col)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.DELETE)
    type(Key.DELETE)
    paste(row)
    type(Key.ENTER)
    type(Key.F5)
    
########################################################################
##########################ここからメインルーチン###########################
########################################################################
num = 0  # テスト番号初期値

for i in range(4, 10):
    print i
    JumpTo(str(i), "D")
    type("c", Key.CTRL)
    result = App.getClipboard()
    print result 
    # 合否書き込み
#    if val == sheet.cell(i, 3).value:
#        wt.get_sheet(0).write(i, 5, "OK")
#    else:
#        wt.get_sheet(0).write(i, 5, "NG")

