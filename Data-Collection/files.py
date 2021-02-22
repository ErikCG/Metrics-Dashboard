from libs.collector import Collector_CommitWebScraper


class Files(Collector_CommitWebScraper):
    def insertData(self) -> int:
        self.getPage()

        data = self.getData()

        for info in data:
            sql = "INSERT OR IGNORE INTO Files (ID, Commit_SHA, Branch, File_Tree, Status, Raw_URL, Lines_Of_Code) VALUES (?,?,?,?,?,?,?)"

            self.connection.executeSQL(
                sql,
                (
                    self.id,
                    self.commitSHA,
                    self.branch,
                    info[0],
                    info[1],
                    info[2],
                    self.getLOC(rawURL=info[2]),
                ),
                True,
            )
            self.id += 1
