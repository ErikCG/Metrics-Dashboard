from libs.collector import Collector_4


class Commits(Collector_4):
    """Handels data referring to commits. Inherits from Collector_4"""

    def insertData(self, dataset: dict) -> None:
        """Takes in data identifying commits and inserts it into the database.

        Iterates through the dataset, assigns an id num and executes sql to insert data into
        the database in a for loop. Will ignore the data if it is duplicated.

        Parameters:
            dataset (dict): nested dictionary containing data to be inserted into database

        Note:
            dataset should include: the commit hash, author's name, commit date, tree hash
            and comment count

        Returns:
            No return value
        """

        id = 0
        for dataPoint in range(len(dataset)):
            sha = dataset[dataPoint]["sha"]
            author = dataset[dataPoint]["commit"]["author"]["name"]
            date = dataset[dataPoint]["commit"]["committer"]["date"]
            treeSHA = dataset[dataPoint]["commit"]["tree"]["sha"]
            commentCount = dataset[dataPoint]["commit"]["comment_count"]

            sql = "INSERT OR IGNORE INTO Commits (ID, Commit_SHA, Branch, Author, Commit_Date, Tree_SHA, Comment_Count) VALUES (?,?,?,?,?,?,?);"

            self.connection.executeSQL(
                sql,
                (self.id, sha, self.sha, author, date, treeSHA, commentCount),
                True,
            )

            self.id += 1
