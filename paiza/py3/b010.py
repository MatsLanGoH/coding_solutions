# coding: utf-8
# 自分の得意な言語で
# b010 サッカーのオフサイド判定

# off_team, pass_player = input().split()
# team_a = [int(i) for i in input().split()]
# team_b = [int(i) for i in input().split()]

off_team, pass_player = "B 8".split()
team_a = [int(i) for i in "86 36 55 88 10 82 53 107 83 22 15".split()]
team_b = [int(i) for i in "69 38 48 73 21 50 27 1 41 24 103".split()]

offside_players = []


if (off_team == "A"):  # check right side of field
    passer_num = team_a[int(pass_player)-1]
    last_player = sorted(team_b)[-2]
    last_num = team_b.index(last_player)

    for player in team_a:
        if (player > 55 and player > passer_num and player > last_player):
            offside_players.append(team_a.index(player)+1)

else:    # check left side of field
    passer_num = team_b[int(pass_player)-1]
    last_player = sorted(team_a)[1]
    last_num = team_a.index(last_player)

    for player in team_b:
        if (player < 55 and player < passer_num and player < last_player):
            offside_players.append(team_b.index(player)+1)


if (len(offside_players) == 0):
    print(None)
else:
    for player in sorted(offside_players):
        print(player)
