class lists:
    def elo_dict(season):
        elo_list = [
            "ENG",'ESP',"DEU","FRA","ITA",
            "AUT","BEL","BGR","CZE","DNK",
            "POL","PRT","ROU","SCO","CHE",
            "NLD","TUR"
        ]
        
        return elo_list
    
    def competition_list(): #### WEB www.soccerstats.com
            comp_list = [
        'england','england2','england3','england4','england5',
        'france','france2',
        'france3',
        'spain','spain2','italy','italy2',
        'germany','germany2','germany3',
        'austria',
        'austria2',
        #'belgium',
        #'belgium2',
        'bulgaria','croatia','czechrepublic','denmark','denmark2',
        #'ireland','ireland2',
        'netherlands','netherlands2','poland','poland2','portugal','portugal2',
        #'romania',
        'scotland','scotland2','scotland3','scotland4',
        'switzerland','switzerland2','turkey','turkey2',
        #'wales'
        ]
            return comp_list
    
    def clubs_3():
        dc = ["AFC","SKN" ,"SKN","ACF","FSV","MSV","VfB","SBV","RCD","ŁKS","OKS","LKS","BBSK","MKE",
        'Vfl', 'VSG', 'SpVgg', 'TSV', 'BSC', 'FSV', 'OSC','OGC', 'HSC','SCO','FCO',"SSV", 'FKS',
        'USL','CFC', 'SCR', 'KAA', 'KRC','KAS', 'RFC', 'PFC',"VfL","SSC","TOP","GKS",
        'FCS',"SKN","SKU","PFC ","OFK","WSG","FCO","USL","KMSK","PFC","ESTAC"]
        dc2 = ['St.','Las', 'CFJ','St.','Aue','Lok','Rot','VfR','St.','VfV','DJK','SGV','Pau','Red','GFC','St.','KVC','RAA','FCV','KVK',
        'MAS','B&I','AIA','B&I','Gil','Rio','Ave','Pia','SAD','CFR','OSK',
        'UTA','Gaz','St.','St.','Ayr','St.','Wil','RKC','PEC','NEC',
        'ADO','PSV','HHC','Den','Oss','MVV','HFC','SVV','UNA','TEC']
        return dc
    def nums():
        dc = ["1846", "1913", "1914", "1919","07","1.","1. ","1929","1899","1912","1900"
              ]
        return dc
    def clubs_2():
        dc = ["AS","VV","OH","fB","IF","AS","AF","SD","AD","CE","FV","SG","HB",#"GI","AB"
        "RB","CA","SV","CA","CD" ,"UD","DC","SC","CF","SV","CF","IK",'RC',"SK",
         'AJ', 'EA', 'SM','US', 'LB','CS', 'SO', 'AK' ,'KV','VA','FC',"OC",
         'SK','FK', 'FF', 'BK', 'GF', 'KS', 'SL', 'CP','GD','CT',"AC"
        ]
        return dc
    def names():
        dc =  ["Olympique","Girondins","Stade","ESTAC","Foot","Rheindorf","Brussels","Varna","Virtus","Bielsko-Biala",
        "Calcio","Blagoevgrad","Çaykur","Izmir","Praia"]
        return dc    
    def teams(i, step):
        if step == 1:
            short = i.replace("(A)","II").replace("-"," ").replace("Saint-","St. ").replace('AaB',"Aalborg").replace("OB","Odense").replace("Calcio","")
        
            return short
        if step == 2:
            jong = i.replace("Jong Utrecht","Utrecht II").replace("Jong Ajax","Ajax II").replace("Jong PSV","PSV II").replace("Porto II","Porto B").replace("Jong AZ","AZ II").replace("Jong PSV","PSV II")
            
            return jong
        if step == 3:
            n1 = i.replace("LASK Linz","LASK").replace("Lommel United","Lommel").replace("Wattens","Tirol") 
            n2 = n1.replace("Oud-Heverlee Leuven","Leuven").replace("K Beerschot VA","Beerschot").replace("Union Saint-Gilloise","Union St. Gilloise")
            n3 = n2.replace("Aarhus GF","Aarhus").replace("AGF","Aarhus").replace("Paris St. Germain","PSG").replace("Paris Saint Germain","PSG").replace("Chamois Niortais","Niort")
            n4 = n3.replace("FC Ingolstadt 04","Ingolstadt").replace("Ingolstadt 04","Ingolstadt").replace("Aalborg BK","Aalborg").replace("SPG FC Pasching-LASK Juniors","Juniors OÖ")
            n5 = n4.replace("Admira Wacker","Admira").replace("Tychy 71","Tychy").replace("VVV-Venlo","Venlo").replace("VVV","Venlo").replace("Heracles Almelo","Heracles")
            n6 = n5.replace("Lazio Roma","Lazio").replace("Inter Milan","Inter").replace("SPAL 2013 Ferrara","SPAL").replace("S.P.A.L","SPAL")
            n7 = n6.replace("Roda JC Kerkrade","Roda").replace("Roda JC","Roda").replace("Excelsior Virton","Virton").replace("Borussia M'gladbach","Bor. Mönchengladbach")
            n8 = n7.replace("Tsarsko Selo Sofia","Tsarsko Selo").replace("Arda Kardzhali","Arda").replace("Aalborg BK","Aalborg").replace("Ludogorets Razgrad","Ludogorets")
            n9 = n8.replace("Oud-Heverlee Leuven","Leuven").replace("K Beerschot VA","Beerschot").replace("LASK Linz","LASK").replace("Lommel United","Lommel").replace("Wattens","Tirol")
            n10 = n9.replace("Jagiellonia Bialystok","Jagiellonia Białystok").replace("LALinz","LASK Linz")
            n11 = n10.replace("SPG FC Pasching LAJuniors", "Juniors OÖ").replace("Rheindorf Altach","Altach").replace("RWDM FC","RWDM").replace("Sint Truidense","St. Truidense")
            n12 = n11.replace("Oud-Heverlee Leuven","Leuven").replace("Beerschot Wilrijk","Beerschot").replace("K Beerschot","Beerschot").replace("Saint ","St. ")
            n13 = n12.replace("Cherno More Varna","Cherno More").replace("Paris Saint Germain","PSG").replace("Athletic Club Bilbao","Athletic Bilbao").replace("Celta de Vigo","Celta Vigo")
            n14 = n13.replace("Espanyol Barcelona","Espanyol").replace("Real Sociedad B", "Real Sociedad II").replace("Deportivo Alavés","Alavés").replace("Sint Truiden","Sint Truidense")
            n15 = n14.replace("Lyonnais", "Lyon").replace("Saint Étienne","St. Étienne").replace("sc Heerenveen","Heerenveen")
            n16 = n15.replace("Zaglebie Sosnowiec","Zagłębie Sosnowiec").replace("Chrobry Glogów","Chrobry Głogów").replace("Lódz","Łódź").replace("Widzew Lódz","Widzew Łódź")
            n17 = n16.replace("Puszcza Niepolomice","Puszcza Niepołomice").replace("Jastrzebie","Jastrzębie").replace("Wisla Plock","Wisła Płock")
            n18 = n17.replace("Bruk Bet Termalica Nieciecza","Nieciecza").replace("Zaglebie Lubin","Zagłębie Lubin").replace("Wisla Kraków","Wisła Kraków")
            n19 = n18.replace("Slask Wroclaw","Śląsk Wrocław").replace("Cracovia Kraków","Cracovia").replace("Jagiellonia Bialystok","Jagiellonia Białystok").replace("Górnik Leczna","Górnik Łęczna").replace("Leczna","Górnik Łęczna")
            n20 = n19.replace("Associação Académica de Coimbra OAF","Académica de Coimbra").replace("Académico de Viseu","Académico Viseu").replace("1846","")
            n21 = n20.replace("PII","PSV II").replace("Venlo Venlo","Venlo").replace("LASK Linz","LASK").replace("Grasshopper Club Zürich","Grasshopper")
            n22 = n21.replace("Oud Heverlee Leuven","Leuven").replace("PEindhoven","PSV").replace("Benfica B","Benfica II").replace("Sint Truidense","St. Truidense")
            n23 = n22.replace("Kelty Hearts","Hearts").replace("Gazişehir","Gaziantep").replace("Altınordu","Altinordu")
            n24 = n23.replace("Balıkesirspor","Balikesirspor").replace("Altinordu","Altinordu").replace("Bandırmaspor","Bandirmaspor").replace("Kasımpaşa","Kasimpaşa").replace("Gaziantep Gaziantep","Gaziantep")
            n24.rstrip().lstrip()
            
            return n24