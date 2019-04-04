## FuzzyPick
A fuzzy string matcher based on [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance). It provides the calculation of the differences between strings through some simple API.

## Usage
```python
import fuzzypick as fp
```

**Levenshtein Distance Calculation**
```python
>>> fp.levenshtein_distance('hello world', 'hello wrold')
2
```
**Match Score** The more similar pair gets a higher socre.
```python
>>> fp.match_score('abcdef', 'acbdefg')
76.92307692307693
>>> fp.match_score('abcdef', 'abcdef')
100.0
```
Calculate the match-scores bewteen one query string and some candidates, sorted in descending order.
```python
>>> q = 'hello world'
>>> candidates = ('hewlo world', 'happy new year', 'hello world', 'adfafadfiasdf')
>>> fp.pick(q, candidates)
[('hello world', 100.0), ('hewlo world', 95.45454545454545), ('happy new year', 56.00000000000001), ('adfafadfiasdf', 50.0)]
```
Non-ASCII characters can be supported as well.
```python
>>> q = '明天8点来上班'
>>> candidates = ('明天九点来上班', '明天别来上班了', '后天十二点来上班', '明天8点来上班')
>>> fp.pick(q, candidates)
[('明天8点来上班', 100.0), ('明天九点来上班', 92.85714285714286), ('后天十二点来上班', 80.0), ('明天别来上班了', 78.57142857142857)]
```
The candidates can be assigned with a weight
```python
>>> q = 'hello world'
>>> can = {'hewlo world': 0.9, 'happy new year': 0.1, 'hello world': 0.8, 'adfafadfiasdf': 0.2}
>>> s = fp.pick_with_weights(q, can)
>>> s
[('hewlo world', 85.9090909090909), ('hello world', 80.0), ('adfafadfiasdf', 10.0), ('happy new year', 5.600000000000001)]
```