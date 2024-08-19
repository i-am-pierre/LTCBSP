def team_score (Threes: int, Twos: int, Free_throws: int ):
    # Calcualate score for a team
    score = Threes * 3 + Twos * 2 + Free_throws
    return score

def results (A:int, B:int):
    # provide A, B or T
    if A > B:
        return "A"
    elif A == B:
        return "T"
    else: 
        return "B"

team_A_threes = int(input())
team_A_twos = int(input())
team_A_FT = int(input())
team_B_threes = int(input())
team_B_twos = int(input())
team_B_FT = int(input())

team_score_A = team_score(team_A_threes, team_A_twos, team_A_FT)
team_score_B = team_score(team_B_threes, team_B_twos, team_B_FT)

# print(f"Team A:{team_score_A} - {team_score_B}:Team B")
print(f"{results(team_score_A, team_score_B)}")
