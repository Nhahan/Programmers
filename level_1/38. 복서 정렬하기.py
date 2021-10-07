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
        answer_list[i].append(key[0])
        answer_list[i].append(key[1])
    # < list >.sort(key= < function >, reverse = < bool >)
    print(answer_list)
    answer_list.sort(key=lambda answer: answer[2])
    answer_list.sort(key=lambda answer: answer[3])
    answer_list.sort(key=lambda answer: answer[0] / (answer[0] + answer[1]) )


solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"])
