import sqlite3 
from sqlite3 import Cursor, Connection
from IssuesCalculation import Calculations
import sys
def main():
    db_file = sys.argv[1]
    calc = Calculations(db_file)
    conn = calc.create_connection(db_file)
    cursor= conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS ISSUES_CALCULATIONS (calc_name VARCHAR(3000), value VARCHAR(3000));"
    )
    data = [
        ('closed to open ratio',calc.get_closed_to_open_ratio(conn)),
        ('closing efficiency (%)',calc.get_closing_efficiency(conn)),
        ('average days to close issues',calc.get_avg_days_to_close_issue(conn)),
    ]
    sql = 'insert into ISSUES_CALCULATIONS(calc_name,value) VALUES(?,?);'
    cursor.executemany(sql,data)
    conn.commit()
    # insert calculations into table
    print("Inserted calculations into table")

if __name__ == '__main__':
    main()
