"""Given an array, you need to print all possible subarrays, where each subarray is printed on a new line."""

arr = [1,2,3,4]

# brute force

for i in range(len(arr)):
 

    for j in range(i+1, len(arr)):
        
        for k in range(i, j+1):
            print(arr[k], end=" ")
        print("")


print("-------------------------------------")


#  all subarray sum
# brute force

ans = 0
for i in range(len(arr)):
    ans+=arr[i]
    for j in range(i+1, len(arr)):
        for k in range(i, j+1):
            ans+=arr[k]
        
print(ans)



# optimization -1  (using prefix sum)
print("optimization -1  (using prefix sum)")

prefix_sum = []
prefix_sum.append(arr[0])
for i in range(1, len(arr)):
    prefix_sum.append(prefix_sum[i-1] + arr[i])


ans = 0
for i in range(len(arr)):
    ans+=arr[i]
    for j in range(i+1, len(arr)):
       if i==0: 
           ans+=prefix_sum[j]
       else:
            ans+=prefix_sum[j]-prefix_sum[i-1]


print(ans)



# optimization 2  - using carry forward technique (withou using prefix sum)
print("----------------------------------")

ans = 0
for i in range(len(arr)):
    ans+=arr[i]
    run_sum = arr[i]
    for j in range(i+1, len(arr)):
       run_sum+=arr[j]
       ans+=run_sum


print(ans)


# optimization 3  - using contribution technique

ans = 0
n = len(arr)
for i in range(n):
    

    freq = (i+1)*(n-i)

    ans += arr[i] * freq

print(ans, "contribution ans:")