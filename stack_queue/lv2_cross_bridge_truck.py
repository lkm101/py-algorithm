# [문제 설명]
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

# 경과 시간   | 다리를 지난 트럭  | 다리를 건너는 트럭	 | 대기 트럭
#-----------+---------------+-----------------+-----------
# 0	        | []	          | []	            |  [7,4,5,6]
# 1~2	      | []	          | [7]   	        | [4,5,6]
# 3	        | [7]	          | [4]	            | [5,6]
# 4	        | [7]	          | [4,5]	          | [6]
# 5	        | [7,4]	        | [5]	            | [6]
# 6~7	      | [7,4,5]	      | [6]	            | []
# 8	        | [7,4,5,6]	    | []	            | []

# 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

# [제한 조건]
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.

# 입출력 예
# bridge_length	  | weight	| truck_weights	                    | return
# ----------------+---------+-----------------------------------+---------
# 2	              | 10	    | [7,4,5,6]	                        | 8
# 100	            | 100	    | [10]	                            | 101
# 100	            | 100	    | [10,10,10,10,10,10,10,10,10,10]	  | 110

def solution(bridge_length, weight, truck_weights):
    # 총 걸리는 시간
    time = 0
    # 주어지는 다리 길이 만큼 다리 배열 초기화
    bridge = [0] * bridge_length
    # sum(bridge)는 bridge_length가 길어질 수록 연산 속도 저하됨
    totalWeight = 0
    
    # 트럭이 모두 다리에 올라갈 때 까지
    while len(truck_weights) > 0:
        # 무조건 1초씩 흘러감
        time += 1
        
        # 다리 위 맨 앞 트럭 나감
        # 다리 위 무게에서 빼기
        totalWeight -= bridge.pop(0)
        
        # (다리 위 모든 트럭 무게) + 그 다음 지나가려는 트럭 무게 <= 버틸 수 있는 트럭 하중
        if totalWeight + truck_weights[0] <= weight:
            # 다리 위 무게에 더하기
            totalWeight += truck_weights[0]
            # 트럭이 다리 위로 올라감
            bridge.append(truck_weights.pop(0))
        else:
            # 트럭 못올라감
            bridge.append(0)
    
    # 트럭이 다리에 올라가고 while이 끝났으니까 다리 길이 만큼 기다리는 시간 더하기
    time += bridge_length
    
    return time

from collections import deque

# deque 버전 솔루션
# list를 사용할 때 보다 빠른 연산 가능
def solution2(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    totalWeight = 0
    while len(truck_weights)!=0:
        time+=1

        totalWeight -= bridge.popleft()

        if totalWeight + truck_weights[0] <= weight:
            totalWeight+= truck_weights[0]
            bridge.append(truck_weights.popleft())

        else: 
            bridge.append(0)
            
    time += bridge_length
    
    return time