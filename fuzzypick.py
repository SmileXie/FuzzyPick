
"""
FuzzyPick
Author: smilexie1113@gmail.com

"""

import operator


def levenshtein_distance(s1, s2, costs=(1, 1, 1)):
    """
        levenshtein_distance(s1, s2) -> Levenshtein distance

        For all i and j, dist[i,j] will contain the Levenshtein
        distance between the first i characters of s1 and the
        first j characters of s2

        costs: a tuple with three integers (d, i, s)
        where d, i, s, define the costs for a deletion, insertion, and
        substitution  respectively
    """

    rows = len(s1)+1
    cols = len(s2)+1
    d_cost, i_cost, s_cost = costs

    dist = [[0 for x in range(cols)] for x in range(rows)]

    for row in range(1, rows):
        dist[row][0] = row * d_cost

    for col in range(1, cols):
        dist[0][col] = col * i_cost

    for col in range(1, cols):
        for row in range(1, rows):
            if s1[row-1] == s2[col-1]:
                cost = 0
            else:
                cost = s_cost
            dist[row][col] = min(dist[row-1][col] + d_cost,
                                 dist[row][col-1] + i_cost,
                                 dist[row-1][col-1] + cost)  # substitution

    return dist[row][col]


def match_score(s1, s2, costs=(1, 1, 1)):
    dist = levenshtein_distance(s1, s2, costs)
    # if s1 = 'xyz' s2 = 'abcdefg' cost=(1, 0, 1)
    # the dist would be 3, and the cost would be 10 - 3 / 10 = 70%
    # which is not appropriate
    # so use cost as a weight
    sum_len = len(s1) * costs[0] + len(s2) * costs[1]
    return (sum_len - dist) / sum_len * 100


def pick(query, candicates):
    scores = []
    for cdd in candicates:
        s = match_score(query, cdd)
        scores.append(s)
    rst = dict(zip(candicates, scores))
    sorted_rst = sorted(rst.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_rst


def match_score_weights(s1, s2, s2_weights, costs=(1, 1, 1)):
    return match_score(s1, s2, costs) * s2_weights


def pick_with_weights(query, candicates, costs=(1, 1, 1)):
    # candicates: {'string1': value1, 'string2': value2}
    scores = []
    for cdd in candicates.keys():
        s = match_score_weights(query, cdd, candicates[cdd], costs)
        scores.append(s)
    rst = dict(zip(candicates.keys(), scores))
    sorted_rst = sorted(rst.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_rst


# some words are exactly matched in a long sentence, the match_score
# would be very low, but it should be picked.
# this method is designed to applied in this scenario.
# cut down the 'deletion cost'
def pick_adaptive(query, candicates):
    pick_with_weights(query, candicates, costs=(1, 0.1, 1))
