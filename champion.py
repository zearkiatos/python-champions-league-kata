# def total_goals()->int:

# def games_played()->int:

# def goals_team_lead()->str:
import random

range_goals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]


def extract_data_from_file(file_path: str, separate: str) -> dict:
    data_dictionary = {}
    file = open(file_path)
    file.readline().split(separate)
    line = file.readline()
    while len(line) > 0:
        data = line.split(separate)
        key = data[0]
        data_dictionary[key] = int(data[1])
        line = file.readline()
    file.close()
    return data_dictionary


def get_soccer_teams() -> dict:

    teams = extract_data_from_file('./data/teams.csv', ',')

    return teams


def get_goals_table(teams: dict) -> list:
    goals_table = []
    for i in range(0, len(teams)):
        goals_table.append([])
        for j in range(0, len(teams)):
            if (i == j):
                goals_table[i].append(-2)
            else:
                goals_table[i].append(-1)

    return goals_table


def run_goals_table(goals_table: list, teams: dict) -> list:
    teams_list = list(teams)
    for i in range(0, len(goals_table)):
        for j in range(0, len(goals_table[i])):
            if (goals_table[i][j] != -2 and goals_table[i][j] == -1):
                print('Game between: '+teams_list[i]+" vs "+teams_list[j]+"\n")
                goals_table[i][j] = random.randrange(0, 10)
                goals_table[j][i] = random.randrange(0, 10)
                input("The result was "+teams_list[i]+" "+str(goals_table[i][j])+" - " +
                      teams_list[j] + " "+str(goals_table[j][i])+"\n Press a key to continue...")


def get_total_goals(goals_table: list) -> int:
    total_goals = 0
    for i in range(0, len(goals_table)):
        for j in range(0, len(goals_table[i])):
            if (goals_table[i][j] != -2 and goals_table[i][j] != -1):
                total_goals += goals_table[i][j]

    return total_goals


def print_goals_table(goals_table: list, teams: dict) -> None:
    for team in teams:
        print("         ", team, end=" ")
    print("\n")
    for i in range(0, len(goals_table)):
        print(str(list(teams)[i])[0:4], end="")
        print("|           ", end="")
        for j in range(0, len(goals_table)):
            print(str(goals_table[i][j]), end="                 ")
        print("|\n")


def get_team_with_more_goals(goals_table: list, teams: dict) -> str:
    grantest_goal_team = ''
    number_of_goals = 0
    team_list = list(teams)
    goals_by_teams = {}
    for i in range(0, len(goals_table)):
        for j in range(0, len(goals_table[i])):
            goals_by_teams[team_list[i]] = 0
    for i in range(0, len(goals_table)):
        for j in range(0, len(goals_table[i])):
            if (goals_table[i][j] != -2 and goals_table[i][j] != -1):
                goals_by_teams[team_list[i]] += goals_table[i][j]

    for i in range(0, len(goals_by_teams)):
        if (goals_by_teams[team_list[i]] > number_of_goals):
            number_of_goals = goals_by_teams[team_list[i]]
            grantest_goal_team = team_list[i]

    return grantest_goal_team


get_soccer_teams()
