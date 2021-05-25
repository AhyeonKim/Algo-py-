from collections import deque
def solution(bridge_length, weight, truck_weights):
    cur_weight=0
    t=0
    bridge=deque([])
    cnt=0
    truck_weights = deque(truck_weights)
    trucks = len(truck_weights)
    while cnt<trucks:
        if len(bridge)==bridge_length:
            exit = bridge.popleft()
            if exit:
                cur_weight-=exit
                cnt+=1
        if truck_weights:
            truck = truck_weights[0]
            if cur_weight+truck<=weight:
                cur_weight+=truck_weights.popleft()
                bridge.append(truck)
            else:
                bridge.append(0)
        else:
            bridge.append(0)
        t+=1
    return t