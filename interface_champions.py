import champion as champion
def main()->None:
    print("Simulation champions game 🏆⚽️")

    champion_results()


def champion_results()->None:
    teams = champion.get_soccer_teams()
    goals_table = champion.get_goals_table(teams)

    champion.print_goals_table(goals_table, teams)
    champion.run_goals_table(goals_table, teams)
    champion.print_goals_table(goals_table, teams)

    teams = champion.get_soccer_teams()
    print('\nThe total of goals was: '+str(champion.get_total_goals(goals_table)))

    print('\nTeam with more goals: '+str(champion.get_team_with_more_goals(goals_table, teams)))



main()

    