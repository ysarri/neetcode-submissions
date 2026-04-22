class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1: return stones[0]
        stones.sort();
        while stones[-2]>0:
            print(stones)
            x, y = stones[n - 2], stones[n - 1]
            if x == y:
                stones[n - 1], stones[n - 2] = 0, 0
                # i+=2
            elif x < y:
                diff = y - x
                stones[n - 1], stones[n - 2] = 0, diff
            stones.sort();
        return stones[-1]

    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            diff = stones.pop() - stones.pop()
            stones.append(diff)
        return stones[0]


    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        print(stones)

        return abs(stones[0])



    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        
        # 1. Crear el bucket con las frecuencias
        max_weight = max(stones)
        bucket = [0] * (max_weight + 1)
        for s in stones:
            bucket[s] += 1

        # 2. Recorrer de mayor a menor peso
        current_weight = max_weight
        first_stone = 0 # Para guardar la piedra que está "esperando" pareja
        
        while current_weight > 0:
            if bucket[current_weight] == 0:
                current_weight -= 1
                continue
            
            # Si ya tenemos una piedra grande esperando de un nivel superior
            if first_stone > 0:
                bucket[current_weight] -= 1 # Usamos una de este peso para el choque
                diff = first_stone - current_weight
                bucket[diff] += 1           # El resto va al bucket
                
                # El nuevo peso a revisar podría ser el 'diff' o seguir bajando
                # Para no saltarnos el resto, volvemos a poner el puntero arriba
                first_stone = 0
                current_weight = max(current_weight, diff) 
                
            else:
                # Si no hay piedra esperando, miramos cuántas hay de este peso
                # Si son pares, se anulan todas (no hacemos nada).
                # Si son impares, sobra una que se queda esperando pareja.
                if bucket[current_weight] % 2 != 0:
                    first_stone = current_weight
                
                current_weight -= 1

        return first_stone