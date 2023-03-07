import pandas as pd
from bs4 import BeautifulSoup
import requests

year1=1960
while(year1!=2022):
       year2=year1+1
       str_year=str(year1)+"-"+str(year2)[2:]
       webpage = f"https://en.wikipedia.org/wiki/{str_year}_La_Liga"
       content = requests.get(webpage).text
       soup = BeautifulSoup(content, "html.parser")
       tables = soup.find_all("table")
       for table in tables:
           if "Home \\ Away" in table.text:
               results_table = table
       results_table_rows = results_table.findChild().find_all("tr")
       away_teams = []
       home_teams = []
       away_teams_row = results_table_rows[0].find_all("th")
       for i in range(1, len(away_teams_row)):
        team_name = away_teams_row[i].findChild()
        team_name1=away_teams_row[i].findChild().findChild()
        if(team_name1==None):
          away_teams.append(team_name["title"])
        else:
          away_teams.append(team_name1["title"])     
       for i in range(1, len(results_table_rows)):
        team_name = results_table_rows[i].find("th").findChild()
        team_name1=team_name.findChild()
        if(team_name1==None):
           home_teams.append(team_name["title"])
        else:
           home_teams.append(team_name1["title"])
       
       teams_matches = {}
       for i in range(1, len(results_table_rows)):
           tds = results_table_rows[i].find_all("td")
           for j in range(len(tds)):
               if (len(tds[j].text.strip())==0 or tds[j].text.strip()=="—"):
                   continue
               try:
                   score = tds[j].find("a").text.strip()
                   original = teams_matches.get(home_teams[i - 1], [])
                   original.append([away_teams[j], score.strip()])
                   teams_matches[home_teams[i - 1]] = original
               except:
                   score = tds[j].text.strip()
                   original = teams_matches.get(home_teams[i - 1], [])
                   original.append([away_teams[j], score.strip()])
                   teams_matches[home_teams[i - 1]] = original
       df_dict = {"Home": [], "Away": [], "Score": []}
       for key, values in teams_matches.items():
           for value in values:
               df_dict["Home"].append(key)
               df_dict["Away"].append(value[0])
               df_dict["Score"].append(value[1])
       df = pd.DataFrame(df_dict)
       df.to_csv(f"./results/results_{str_year}.csv", index=False)   
       year1=year1+1                 