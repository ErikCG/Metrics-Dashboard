from libs.collector import Collector_3


class Forks(Collector_3):
    """Handels data referring to branches. Inherits from Collector_3 class"""

    def insertData(self, dataset: dict) -> None:
        """Takes in data identifying commits and inserts it into the database.

        Iterates through the dataset and executes sql to insert data into the database in a
        for loop. Will ignore the data if it is duplicated.

        Parameters:
            dataset (dict): nested dictionary containing data to be inserted into database

        Note:
            dataset should include: id num, fork name, owner name, creation date update date,
            pushed date, size, num of forks, and num of open issues.

        Returns:
            No return value
        """
        for fork in dataset:
            id = fork["id"]
            name = fork["name"]
            owner = fork["owner"]["login"]
            createdAt = fork["created_at"]
            updatedAt = fork["updated_at"]
            pushedAt = fork["pushed_at"]
            size = fork["size"]
            forks = fork["forks_count"]
            openIssues = fork["open_issues_count"]

            sql = "INSERT OR IGNORE INTO Forks (ID, Name, Owner, Created_At_Date, Updated_At_Date, Pushed_At_Date, Size, Forks, Open_Issues) VALUES (?,?,?,?,?,?,?,?,?)"

            self.connection.executeSQL(
                sql,
                (
                    id,
                    name,
                    owner,
                    createdAt,
                    updatedAt,
                    pushedAt,
                    size,
                    forks,
                    openIssues,
                ),
                True,
            )
