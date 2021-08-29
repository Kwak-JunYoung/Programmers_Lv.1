def solution(table, languages, preference):
    scores = []
    d = {}
    
    for t in table:
        l = t.split()
        d[l[0]] = l[1:]
    
    sk = sorted(d.keys())
    
    for key in sk:
        dummy = 0
        for language in languages:
            if language in d[key]:
                dummy += (5 - d[key].index(language)) * preference[languages.index(language)]
        scores.append(dummy)
    
    return (sk[scores.index(max(scores))])
