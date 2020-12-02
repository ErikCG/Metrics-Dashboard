from datetime import datetime, timedelta
import sqlite3
import sqlite_database
from sqlite3 import Cursor, Connection
import sys, os
import pandas as pd


# def main():
#     # cs371f20p3-stephanie-matt-jakob
#     args = sys.argv[1:]
#     cwd = os.getcwd()
#     print("Database name that was entered: ", args[0])
#     db= cwd + "/metrics/cs371f20p3-stephanie-matt-jakob.db"
#     print(db)
#     conn = sqlite3.connect("/metrics/" + str("cs371f20p3-stephanie-matt-jakob") + ".db")
#     exit()
#     dbCursor, dbConnection = sqlite_database.open_connection(args[0]) 
#     cc = CommitsCalculations(dbCursor, dbConnection)
#     cc.calc_average_time_between_commits()


class CommitsCalculations:

    def __init__(self, dbCursor, dbConnection) -> None:
        '''
        Initialize class variables
        :param dbCursor: The db cursour used in Master.py
        :param dbConnection: The db connection used in Master.py
        '''
        self.dbCursor = dbCursor
        self.dbConnection = dbConnection

    def list_to_string(self, x_list, combinator) -> str:
        combinator= ", "
        combinator = combinator.join(x_list)
        return combinator
    
    def insert_calc_into_table(self, calc_name, value, unit) -> None:
        '''
        parameter: calc_name - name of the calculation to be entered into the database
        parameter: value - number associated with the calculation 
        paamterer: unit - the unit of the calculated number 
        '''
        # Stores the data into a SQL database
        sql = "INSERT INTO COMMITS_CALCULATIONS (calc_name, value, unit) VALUES (?,?, ?);"
        self.dbCursor.execute(sql, (
            str(calc_name),
            str(value),
            str(unit)),)
        self.dbConnection.commit()
    
    def insert_calc_into_table_and_column(self, date, hour, no_of_committs, person) -> None:
        '''
        parameter: calc_name - name of the calculation to be entered into the database
        '''
        # Stores the data into a SQL database
        sql = "INSERT INTO COMMITS_CALCULATIONS_HOURLY (commiter_calendar_date, committer_hour, count_of_committs_per_hour, top_committer_per_hour) VALUES (?,?,?,?);"
        self.dbCursor.execute(sql, (
            str(date),
            str(hour),
            str(no_of_committs),
            str(person)),)
        self.dbConnection.commit()

    def calc_average_time_between_commits(self) -> None:
        '''
        Pulls all the dates of commits from the COMMITS table and find the average difference. 
        Pushes information to the COMMITS_CALCULATIONS table 
        '''
        # get all the times from the commits table
        self.dbCursor.execute(
            "SELECT committer_date FROM COMMITS;")
        date_rows = self.dbCursor.fetchall()
        # calculate average time between commit
        total_times = []
        total_time_differences = []
        for row in date_rows:
            date = datetime.strptime(
            row[0], "%Y-%m-%d %H:%M:%S")
            total_times.append(date)

        # only if the list is greater than two 
        if len(total_times) >= 2:
            for t in range(len(total_times)-1):
                time_difference  = abs(total_times[t] - total_times[t+1])
                total_time_differences.append(round(time_difference.total_seconds() / 60,2))
            
            value = str(round(sum(total_time_differences) / len(total_time_differences),2))
        else:
            value = "N/A"
        # average time between commits
        calc_name = "Average Time Between Commits"
        unit = "minutes"

        # insert into COMMITS_CALCULATION table 
        self.insert_calc_into_table(calc_name, value, unit)

    def calc_commits_per_hour(self) -> None:

        # get all the times from the commits table
        self.dbCursor.execute(
            "SELECT committer, committer_date FROM COMMITS;")

        date_df = pd.DataFrame(self.dbCursor.fetchall())
        date_df.columns = ['committer', 'committer_date']
        date_df['committer_date'] = pd.to_datetime(date_df['committer_date'])
        date_df.sort_values(by=['committer_date'], inplace=True)
        date_df['commiter_calendar_date'] = date_df['committer_date'].apply(lambda x: x.date())
        date_df['committer_hour'] = date_df['committer_date'].apply(lambda x: x.hour)
        date_df.reset_index(inplace=True, drop=True)

        self.dbCursor.execute(
            "ALTER TABLE COMMITS_CALCULATIONS_HOURLY ADD count_of_committs_per_hour varchar(3000);")
        self.dbConnection.commit()
        self.dbCursor.execute(
            "ALTER TABLE COMMITS_CALCULATIONS_HOURLY ADD top_committer_per_hour varchar(3000);")
        self.dbConnection.commit()

        unique_dates = pd.unique(date_df['commiter_calendar_date'])

        for date in unique_dates: 
            one_date_df  = date_df.loc[date_df['commiter_calendar_date']== date]
            for hour in range(24):
                one_hour_df  = one_date_df.loc[one_date_df['committer_hour'] == hour]
                if one_hour_df.shape[0]>0:
                    no_of_committs = one_hour_df.shape[0]
                    top_committers_list = one_hour_df.committer.mode().tolist()
                    top_committer= ", "
                    top_committer = top_committer.join(top_committers_list)
                else:
                    no_of_committs = 0
                    top_committer = "None"
                self.insert_calc_into_table_and_column(date, hour, no_of_committs, top_committer)

        overall_top_committer_list = date_df.committer.astype(str).mode().tolist()
        overall_top_committer = self.list_to_string(overall_top_committer_list, ", ")

        date_most_active_list = date_df.commiter_calendar_date.astype(str).mode().tolist()
        date_most_active = self.list_to_string(date_most_active_list, ", ")

        self.insert_calc_into_table("Overall Project Top Committer", overall_top_committer, "")
        self.insert_calc_into_table("Date With Most Committs", date_most_active, "")

    





        




# main()