class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Contamos la frecuencia de cada número
        # Resultado: {1: 3, 2: 2, 3: 1}
        counts = Counter(nums)
        
        # 2. Usamos un heap para extraer los k elementos con mayor frecuencia
        # nlargest mira el valor (frecuencia) y devuelve la llave (número)
        return heapq.nlargest(k, counts.keys(), key=counts.get)