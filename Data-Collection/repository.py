from libs.collector import Collector_3


class Repository(Collector_3):
    """Handels data referring to repositories. Inherits from Collector_3 class"""

    def insertData(self, dataset: dict) -> None:
        """Takes in data identifying commits and inserts it into the database.

        Iterates through the dataset and executes sql to insert required data into the database in a
        for loop. Will ignore the data if it is duplicated.

        Parameters:
            dataset (dict): nested dictionary containing data to be inserted into database

        Note:
            dataset should include: id num, repo name, owner name, private bool, fork bool, creation date
            update date, pushed date, size, num of forks, and num of open issues.

        Returns:
            No return value
        """
        id = dataset["id"]
        name = dataset["name"]
        owner = dataset["owner"]["login"]
        private = str(dataset["private"])
        fork = str(dataset["fork"])
        createdAt = dataset["created_at"]
        updatedAt = dataset["updated_at"]
        pushedAt = dataset["pushed_at"]
        size = dataset["size"]
        forks = dataset["forks_count"]
        openIssues = dataset["open_issues_count"]

        sql = "INSERT OR IGNORE INTO Repository (ID, Name, Owner, Private, Fork, Created_At_Date, Updated_At_Date, Pushed_At_Date, Size, Forks, Open_Issues) VALUES (?,?,?,?,?,?,?,?,?,?,?)"

        self.connection.executeSQL(
            sql,
            (
                id,
                name,
                owner,
                private,
                fork,
                createdAt,
                updatedAt,
                pushedAt,
                size,
                forks,
                openIssues,
            ),
            True,
        )
