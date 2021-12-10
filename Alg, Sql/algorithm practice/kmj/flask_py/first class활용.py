def html_creater(tag):
    def text_wrapper(mag):
        print("<{0}>{1}</{2}>".format(tag,mag))
    return text_wrapper
h1_html_creater = html_creater('h1')
print(h1_html_creater)
h1_html_creater("h1 태그는 타이틀을 표시하는 태그입니다")
