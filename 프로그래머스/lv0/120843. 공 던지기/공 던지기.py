def solution(numbers, k):
    # players = numbers[0::2] if len(numbers) % 2 ==0 else numbers[0::2] + numbers[1::2]
    return numbers[2 * (k - 1) % len(numbers)]