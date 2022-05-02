s = 	"(()("
while s.count("()") != 0:
    s = s.split("()")
    s = ''.join(s)
    s = s.lstrip("(").rstrip(")")
    print(s)
if s == "":     print(True)
else:   print(False)