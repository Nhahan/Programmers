def win_rate(win, lose):
    return win / (win + lose) if win + lose > 0 else 0


def solution(weights, head2head):
    weights_dict = {}
    for idx, weight in enumerate(weights):  # [50, 82, 75, 120]
        if (weight, idx) not in weights_dict.keys():
            # 승리, 패배, 무거운 복서 이긴 횟수
            weights_dict[(weight, idx)] = [0, 0, 0]
        for i, heads in enumerate(head2head):  # ["NLWL", "WNLL", "LWNW", "WWLN"]
            for j, head in enumerate(heads):  # NLWL
                if idx != i:
                    break
                if head == "W":  # 이겼다면
                    weights_dict[(weight, idx)][0] += 1
                    if weights[j] > weight:  # 상대방의 몸무게가 무겁다면
                        weights_dict[(weight, idx)][2] += 1
                elif head == "L":  # 졌다면
                    weights_dict[(weight, idx)][1] += 1
    answer_list = []
    for i, key in enumerate(weights_dict.keys()):
        answer_list.append(weights_dict[key])
        tmp = int(answer_list[i][0] * 100000000 / (answer_list[i][0] + answer_list[i][1])) if (answer_list[i][0] +
                                                                                               answer_list[i][
                                                                                                   1]) != 0 else 0
        answer_list[i].append(tmp)
        answer_list[i].append(key[0])
        answer_list[i].append(key[1] + 1)

    answer_list.sort(key=lambda a: (-a[3], -a[2], -a[4], a[5]))
    return [i[5] for i in answer_list]


print(solution([145, 92, 86], ["NLW", "WNL", "LWN"]))
print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))
