def solution(record):

    Change = "Change"

    entry = {"Enter": " entered .",
             "Leave": " left." }

    recs = []

    for r in record:
        r = r.split(" ")
        recs.append(r)

    # Change user id for all record first. 
    for r in recs:
        uid = ""
        nickname = ""
        if (Change in r):
            uid = r[1]
            nickname = r[2]
        for r in recs:
            if (uid in r):
                r[2] = nickname

    # Create user data db - {"uid": "nickname"}
    user_db = {}
    for r in recs:
        user_db[r[1]] = r[-1]

    answer = []

    for r in recs:
        if (Change not in r):
            message = ""
            message = f"{user_db[r[1]]}{entry[r[0]]}"
            answer.append(message)
            print(message)

    return answer
