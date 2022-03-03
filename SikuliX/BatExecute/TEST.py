import sys
arg = sys.argv

type("r", Key.WIN)
paste("chrome")
type(Key.ENTER)
wait(2)
paste(arg[1])
paste(u"こんにちは")
paste(arg[2])
