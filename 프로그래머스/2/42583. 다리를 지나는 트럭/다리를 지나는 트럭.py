from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * (bridge_length))
    truck_weights = deque(truck_weights)
    running_trucks = 0

    while bridge :
        time += 1
        running_trucks -= bridge.popleft()
        if truck_weights:
            running_trucks += truck_weights[0]
            if running_trucks <= weight:
                bridge.append(truck_weights.popleft())
            else:
                running_trucks -= truck_weights[0]
                bridge.append(0)
    return time