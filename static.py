class statistic:
    def home_team_table(df): # ds = dataframe t = team name
        global home_table
        home_table = df[['team_name', 'matches_played_home', 'wins_home', 'draws_home','losses_home', 'points_per_game_home',
        'goals_scored_home', 'goals_conceded_home', 'goal_difference_home','goals_scored_per_match_home','goals_conceded_per_match']]
        return home_table    

    def team_goals_home(df, t: str, sc: str): # df - dataFrame, t = team name sc - scored/conc
        a = teams[['team_name','goals_scored_per_match_home','goals_conceded_per_match_home']] 
        c = a.loc[a['team_name']==t].values
        if sc == 'scored':
            return float(c[0][1])
        if sc == 'conc':
            return float(c[0][2])

    def away_team_table(df): # ds = dataframe t = team name
        global away_table
        away_table = df[['team_name', 'matches_played_away', 'wins_away', 'draws_away','losses_away', 'points_per_game_away',
        'goals_scored_away', 'goals_conceded_away', 'goal_difference_away','goals_scored_per_match_away','goals_conceded_per_away']]
        return away_table    

    def team_goals_away(df, t: str, sc: str): # df - dataFrame, t = team name ha - home/away
        a = teams[['team_name','goals_scored_per_match_away','goals_conceded_per_match_away']] 
        c = a.loc[a['team_name']==t].values
        if sc == 'scored':
            return float(c[0][1])
        if sc == 'conc':
            return float(c[0][2])

    def goals_avg(df, t: str, ha: str, sc: str):
        if ha == 'home':
            if sc == 'scored':
                a = df[['team_name','goals_scored_per_match_home','goals_conceded_per_match_home']] 
                c = a.loc[a['team_name']==t].values
                return float(c[0][1])
            if sc == 'conc':
                a = df[['team_name','goals_scored_per_match_home','goals_conceded_per_match_home']] 
                c = a.loc[a['team_name']==t].values
                return float(c[0][2])
        if ha == 'away':
            if sc == 'scored':
                a = df[['team_name','goals_scored_per_match_away','goals_conceded_per_match_away']] 
                c = a.loc[a['team_name']==t].values
                return float(c[0][1])
            if sc == 'conc':
                a = df[['team_name','goals_scored_per_match_away','goals_conceded_per_match_away']] 
                c = a.loc[a['team_name']==t].values
                return float(c[0][2])

