def solution(my_string):
    a = ['a','e','i','o','u']
    # for i in a: # 이건 안되더라
    #     while i in list(my_string):
    #         list(my_string).remove(i)

    return ''.join([i for i in list(my_string) if i not in a])