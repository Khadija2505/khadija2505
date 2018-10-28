def truncate_long_words(s, def truncate_long_words(s, num):
    """Splits long words in string"""
    words = s.split()
    for word in words:
        if len(word) > num:
            for i in xrange(0, len(word), num):
                yield word[i:i + num]
        else:
            yield word


for t in truncate_long_words(s):
    print t

def hello():
    print("Hello")