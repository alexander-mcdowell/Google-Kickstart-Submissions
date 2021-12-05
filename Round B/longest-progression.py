def longest_progression(arr):
    diff = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    
    changed_diff_index = None
    changed_diff = None
    changed_arr = None
    changed = False
    
    best_count = 2
    count = 2
    
    i = 0
    while (not (i >= len(diff) - 1 and changed_diff_index == None)):
        if (i >= len(diff) - 1):
            # Update our current best length.
            if (count > best_count): best_count = count
            count = 2
                
            # Restore the changed values
            i = changed_diff_index
            diff[i] = changed_diff
            arr[i + 1] = changed_arr
            if (i + 2 < len(arr)): diff[i + 1] = arr[i + 2] - arr[i + 1]
            changed = False
            
            changed_diff_index = None
            changed_diff = None
            changed_arr = None
            continue
        
        if (diff[i + 1] != diff[i]):
            # Change a single value
            if (not changed):
                # Record the changed value and related variables
                changed_diff_index = i + 1
                changed_diff = diff[i + 1]
                changed_arr = arr[i + 2]
                
                # Change the arr value and update diff accordingly.
                arr[i + 2] = arr[i + 1] + diff[i]
                diff[i + 1] = diff[i]
                if (i + 3 < len(arr)): diff[i + 2] = arr[i + 3] - arr[i + 2]
                changed = True
                
                # Increase the count.
                count += 1
                i += 1
            else:
                # Update our current best length.
                if (count > best_count): best_count = count
                count = 2
                
                # Restore the changed values
                i = changed_diff_index
                diff[i] = changed_diff
                arr[i + 1] = changed_arr
                if (i + 2 < len(arr)): diff[i + 1] = arr[i + 2] - arr[i + 1]
                changed = False
                
                changed_diff_index = None
                changed_diff = None
                changed_arr = None
        else:
            count += 1
            i += 1

    if (count > best_count): best_count = count      
    return best_count

num_cases = int(input())
for i in range(1, num_cases + 1):
    _ = input()
    s = input()
    arr = [int(x) for x in s.split(" ")]
    # Dumb solution; might get the job done though.
    x = max(longest_progression(arr), longest_progression(arr[::-1]))
    print("Case #" + str(i) + ": " + str(x))