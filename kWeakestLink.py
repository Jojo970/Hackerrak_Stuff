class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        map_of_indices = {}
        lst_to_return = []
        count = 0
        
        for row in mat:
            map_of_indices[count] = sum(row)
            count+=1
        
        count = 0
        for item in sorted(map_of_indices.items(), key = lambda x: x[1]):
            if count == k:
                break
            lst_to_return.append(item[0])
            count+=1

        return lst_to_return