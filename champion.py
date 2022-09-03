# def total_goals()->int:

# def games_played()->int:

# def goals_team_lead()->str:

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

    goals_table = get_goals_table(teams)

    print_goals_table(goals_table)

    return {}


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


def print_goals_table(goals_table: dict) -> None:
    for i in range(0, len(goals_table)):
        print("|", end="")
        for j in range(0, len(goals_table)):
            print(str(goals_table[i][j]), end=" ")
        print("|\n")


get_soccer_teams()
