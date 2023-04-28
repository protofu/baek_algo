def solution(user_id, banned_id):
    from itertools import permutations

    def match(user, ban):
        if len(user) != len(ban):
            return False
        for u, b in zip(user, ban):
            if b == '*':
                continue
            if u != b:
                return False
        return True

    matches = [[] for _ in range(len(banned_id))]
    for i, ban in enumerate(banned_id):
        for user in user_id:
            if match(user, ban):
                matches[i].append(user)

    perms = set()
    def dfs(idx, curr):
        if idx == len(banned_id):
            perms.add(tuple(sorted(curr)))
            return
        for user in matches[idx]:
            if user not in curr:
                curr.append(user)
                dfs(idx+1, curr)
                curr.pop()

    dfs(0, [])
    return len(perms)
