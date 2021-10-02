def solution(table, languages, preference):
    language_scores = {}
    for i in range(len(languages)):
        language_scores[languages[i]] = preference[i]
    table_dict = {}
    for t in table:
        tmp = t.split(" ")
        table_dict[tmp[0]] = tmp[1:]
    key_list = list(table_dict.keys())
    score_dict = {}
    max_score = 0
    for key in key_list:
        value_sum = 0
        for language in languages:
            if language in table_dict[key]:
                value_sum += (5 - table_dict[key].index(language)) * language_scores[language]
        score_dict[key] = value_sum
        if value_sum > max_score:
            max_score = value_sum
    answer_list = []
    for key in key_list:
        if score_dict[key] == max_score:
            answer_list.append(key)
    answer_list = sorted(answer_list)
    return answer_list[0]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#",
                "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"],
               ["PYTHON", "C++", "SQL"],
               [7, 5, 5]))
