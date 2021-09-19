def solution(strings, n):
    answer_list = []
    answer_dict = {}
    for string in strings:
        if string[n] not in answer_dict.keys():
            answer_dict[string[n]] = []
        answer_dict[string[n]].append(string)
    for key in sorted(answer_dict.keys()):
        answer_dict[key].sort()
        for value in answer_dict[key]:
            answer_list.append(value)
    return answer_list