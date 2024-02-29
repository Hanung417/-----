def solution(n, words):
    answer = [0,0]
    use_word = []
    use_word.append(words[0])

    for i in range(1, len(words)) :
        if (words[i] in use_word) or (words[i-1][-1] != words[i][0]) :
            answer = [(i%n)+1,(i//n)+1]
            break
        use_word.append(words[i])
        
    return answer