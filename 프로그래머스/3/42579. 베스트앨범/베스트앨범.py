def solution(genres, plays):
    answer = []
    dic = []
    genre_d = {}
    dic = [[genres[i], plays[i], i] for i in range(len(genres))]
    sorted_dic = sorted(dic, key=lambda x: (x[0], -x[1], x[2]))
    
    for g in sorted_dic :
        if g[0] not in genre_d:
            genre_d[g[0]] = g[1]
        else:
            genre_d[g[0]] += g[1]
    
    genre_d = sorted(genre_d.items(), key = lambda x: -x[1])
    
    for i in genre_d :
        count = 0
        for j in sorted_dic :
            if i[0] == j[0] :
                if count < 2 :
                    count += 1
                    answer.append(j[2])

    return answer