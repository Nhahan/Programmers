def win_rate(win, lose):
    return win / (win + lose) if win + lose > 0 else 0


def solution(weights, head2head):
    weights_dict = {}
    for idx, weight in enumerate(weights):
        if weight not in weights_dict.keys():
            # 승리, 패배, 승률, 무거운 복서 이긴 횟수, 선수 번호
            weights_dict[weight] = [0, 0]
            weights_dict[weight].append(win_rate(weights_dict[weight][0], weights_dict[weight][1]))
            weights_dict[weight].append(0)
            weights_dict[weight].append(idx + 1)
        for i, head in enumerate(head2head):
            print(head)
            for h in head:

                if h == "W":  # 이겼을 떄
                    weights_dict[weight][0] += 1
                    print(weight, weights[i])
                    if weight < weights[i]:  # 상대보다 가벼우면
                        weights_dict[weight][3] += 1
                elif h == "L":  # 졌을 떄
                    weights_dict[weight][1] += 1

    print(weights_dict)


solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"])
