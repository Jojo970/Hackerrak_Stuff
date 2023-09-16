def migratoryBirds(arr):
    # Write your code 
    bird_count = {}
    unique_birds = list(set(arr))
    
    for x in unique_birds:
        bird_count[x] = arr.count(x)
        
    return max(bird_count, key=bird_count.get)