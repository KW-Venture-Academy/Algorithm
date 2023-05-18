#다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)  # 다리를 나타내는 데크 생성
    truck_weights = deque(truck_weights)  # 트럭 리스트를 데크로 변환
    bridge_weight = 0  # 현재 다리에 올라간 무게

    while bridge:
        answer += 1
        bridge_weight -= bridge.popleft()  # 다리에서 가장 앞에 있는 트럭의 무게를 빼줌

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck_weight = truck_weights.popleft()
                bridge_weight += truck_weight
                bridge.append(truck_weight)
            else:
                bridge.append(0)  # 다리에 트럭이 올라갈 수 없는 경우 0을 추가
    return answer