import sys
arg = sys.argv

type("r", Key.WIN)
paste("chrome")
type(Key.ENTER)
wait(2)
paste(arg[1])
paste(u"こんにちは") # 日本語対応
str = arg[2].encode('string-escape').decode('string-escape') # 日本語対応
paste(str)
