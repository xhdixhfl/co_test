def solution(numbers, k):
    # answer = 0
    # if len(numbers) % 2 == 0:
    #     if len(numbers) // 2 < k:
    #         answer = (k - (len(numbers)/2)) + 1
    #     else:
    #         answer = ((len(numbers)/2) - k) + 1
    # else:
    #     if k > len(numbers):
    #         a = k % len(numbers)
    #     k % 2 == 1:
    #         answer = 2 * (k//2)
    #     else
    #     while k > len(numbers):
    #         k -= len(numbers)
    #         answer = ((len(numbers)//2) - k) + 1
              
    return ((k-1)*2) % len(numbers)