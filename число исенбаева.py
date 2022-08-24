players = {}
n = int(input())
first = False
f = ""
for i in range(n):
    pls = input().split(" ")
    if first is False:
        f = pls[0]
        first = True
    if pls[0] not in players.keys():
        players[pls[0]] = []
    if pls[1] not in players[pls[0]]:
        players[pls[0]].append(pls[1])
    if pls[2] not in players[pls[0]]:
        players[pls[0]].append(pls[2])
 
    if pls[1] not in players.keys():
        players[pls[1]] = []
    if pls[0] not in players[pls[1]]:
        players[pls[1]].append(pls[0])
    if pls[2] not in players[pls[1]]:
        players[pls[1]].append(pls[2])
 
    if pls[2] not in players.keys():
        players[pls[2]] = []
    if pls[1] not in players[pls[2]]:
        players[pls[2]].append(pls[1])
    if pls[0] not in players[pls[2]]:
        players[pls[2]].append(pls[0])
isen = True
if "Isenbaev" not in players.keys():
    players["Isenbaev"] = []
    isen = False
dist = {}
for i in players.keys():
    dist[i] = -1
used = {}
for i in players.keys():
    used[i] = False
used["Isenbaev"] = True
dist["Isenbaev"] = 0
q = []
q.append("Isenbaev")
while len(q) != 0:
    u = q.pop(0)
    for v in players[u]:
        if used[v] is False:
            used[v] = True
            dist[v] = dist[u] + 1
            q.append(v)
p_alf = players.keys()
players_alf = []
for i in p_alf:
    players_alf.append(i)
players_alf.sort()
for i in players_alf:
    if i == "Isenbaev" and isen == False:
        pass
    elif dist[i] == -1:
        print(i, "undefined")
    else:
        print(i, dist[i])