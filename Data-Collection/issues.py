from libs.collector import Collector_3


class Issues(Collector_3):
    """Handels data referring to issues. Inherits from Collector_3 class"""

    def insertData(self, dataset: dict) -> None:
        """Takes in data identifying commits and inserts it into the database.

        Iterates through the dataset and executes sql to insert required data into the database in a
        for loop. Will ignore the data if it is duplicated.

        Parameters:
            dataset (dict): nested dictionary containing data to be inserted into database

        Note:
            dataset should include: id num, count, issue title, author name, assignees, labels,
            creation date, update date, closed date.

        Returns:
            No return value
        """

        def _labelCollection(
            index: int,
        ) -> str:
            """Joins labels together into one string

            Uses a for loop to take labels from dataset and append them to an array.
            Then uses .join() to join on the array to create one string and return.

            Paramaters:
                index (int): index num of entry in dataset to pull labels from

            Returns:
                str: string of labels joined together with ', '
            """

            labelNames = []
            for label in dataset[index]["labels"]:
                labelNames.append(label["name"])
            return ", ".join(labelNames)

        def _asigneeCollection(
            index: int,
        ) -> str:
            """Joins asignees together into one string

            Uses a for loop to take asignees from dataset and append them to an arry.
            Then uses .join() on the array to create one string and return.

            Paramaters:
                index (int): index num of entry in dataset to pull asignees from

            Returns:
                str: string of asignees joined together with ', '
            """

            labelNames = []
            for assignee in dataset[index]["assignees"]:
                labelNames.append(assignee["login"])
            return ", ".join(labelNames)

        for dataPoint in range(len(dataset)):
            id = dataset[dataPoint]["id"]
            count = dataset[dataPoint]["number"]
            title = dataset[dataPoint]["title"]
            author = dataset[dataPoint]["user"]["login"]
            assignees = _asigneeCollection(index=dataPoint)
            labels = _labelCollection(index=dataPoint)
            state = dataset[dataPoint]["state"]
            createdAt = dataset[dataPoint]["created_at"]
            updatedAt = dataset[dataPoint]["updated_at"]
            closedAt = dataset[dataPoint]["closed_at"]

            sql = "INSERT OR IGNORE INTO Issues (ID, Count, Title, Author, Assignees, Labels, State, Created_At_Date, Updated_At_Date, Closed_At_Date) VALUES (?,?,?,?,?,?,?,?,?,?);"

            self.connection.executeSQL(
                sql,
                (
                    id,
                    count,
                    title,
                    author,
                    assignees,
                    labels,
                    state,
                    createdAt,
                    updatedAt,
                    closedAt,
                ),
                True,
            )
