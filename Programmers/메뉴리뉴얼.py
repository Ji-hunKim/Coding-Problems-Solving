from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for order in orders:
            for combi in combinations(order, k):
                combined = ''.join(sorted(combi))
                candidates.append(combined)

        sorted_candidates = Counter(candidates).most_common()

        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)