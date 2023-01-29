def solution(id_pw, db):
    dic = {a[0]: a[1] for a in db}
    if id_pw[0] in dic:
        if id_pw[1] == dic[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"