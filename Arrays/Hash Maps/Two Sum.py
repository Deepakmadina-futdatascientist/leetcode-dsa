def twoSums(nums,target):
    seen={}
    for i,current in enumerate(nums):
        
        required=target-current
        if(required  in seen):
            return[seen[required],i]
        else:
            seen[current]=i

            
