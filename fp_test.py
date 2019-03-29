import fuzzypick as fp


def main():
    # main is only for test
    d1, s1 = fp.levenshtein_distance('你好', '你好'),\
        fp.match_score('你好', '你好')
    d2, s2 = fp.levenshtein_distance('你好', '你123好吗'), \
        fp.match_score('你好', '你123好吗')
    d3, s3 = fp.levenshtein_distance('abcdef', 'acbdefg'), \
        fp.match_score('abcdef', 'acbdefg')
    print('d1 d2 d3: %d %d %d' % (d1, d2, d3))
    print('s1 s2 s3: %d %d %d' % (s1, s2, s3))

    q = 'hello world'
    can = ('hewlo world', 'happy new year', 'hello world', 'adfafadfiasdf')
    s = fp.pick(q, can)
    print('sorted %s' % s)


if __name__ == "__main__":
    main()
