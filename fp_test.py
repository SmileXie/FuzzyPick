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

    d1, s1 = fp.levenshtein_distance('hello world', 'Spencer, hello world'), \
        fp.match_score('hello world', 'Spencer, hello world')
    d2 = fp.levenshtein_distance(
        'hello world', 'Spencer, hello world', costs=(1, 0, 1)
    )
    s2 = fp.match_score('hello world', 'Spencer, hello world', costs=(1, 0, 1))

    print('d1 d2: %d %d' % (d1, d2))
    print('s1 s2: %d %d' % (s1, s2))

    keywords = 'aaaaaaaaaaa'
    summary = '【RCC_V3.6_R1P4T1.70】【在线播放器】进土豆网页，打开一个视频，点击网页的\
        “跳过广告”，再点击播放器的“加载前一个页面”返回刚才的视频链接，出现：之后点击“播放”\
        ，播放器的内容是一片白色'
    score = fp.match_score_weights(keywords, summary, 1.0,
                                   costs=(1, 0, 1))
    print('score: ' + str(score))

    query = 'asdf'
    test_str = 'qerfaas9iqfasdfkllkj'
    print(fp.highlight_query(query, test_str))


if __name__ == "__main__":
    main()
