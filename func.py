class functions:
    def loop_tables(tables):
        n = 0
        for j in tables:
            if 'W' in j.keys():
                return n
            n = n+1
            
    def loop_elos(tables):
        n = 0
        for j in tables:
            if '#' in j.keys():
                return n
            n = n+1
    def loop_matches(tables):
        n=0
        for j in tables:
            if 'Local' in j.keys():
                return n
            n = n+1