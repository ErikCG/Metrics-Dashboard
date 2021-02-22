from bs4 import BeautifulSoup

import re

import requests
from requests import Response


class GitHubConnector:
    """Class to access the GitHub API."""

    def __init__(self, oauthToken: str = None) -> None:
        """Initalizes the class.

        Parameters:
            oauthToken (str): The personal access token needed to access the GitHub API.

        Returns:
            None: The class is initalized.
        """
        self.token = oauthToken

    def openConnection(self, url: str) -> Response:
        """Sends a request to a GitHub API endpoint.

        Configures all of the headers prior to sending the request.

        Parameters:
            url (str): The GitHub API endpoint that is to be accessed.

        Returns:
            Reponse: The response data sent back to the application from the GitHub API endpoint.
        """
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Metrics-Dashboard",
            "Authorization": "token {}".format(self.token),
        }

        return requests.get(url=url, headers=headers)

    def parseResponseHeaders(self, response: Response) -> dict:
        """Get specific information from the response headers.

        The data that is carred about is the rate limit and reset, as well as  the next and last pages of the request if the response has been truncated.

        Parameters:
            response (Response): The response object sent back to the application from a request.

        Returns:
            dict: A dictionary of key-value pairs that only has the important information needed for the application to function properly.
        """

        def _findLastPage() -> int:
            """Finds the last page within the header data.

            Returns:
                int: Returns the value of the last page of a request.
            """
            try:
                links = response.headers["Link"].split(",")
                for link in links:
                    if link.find('rel="last"') != -1:
                        try:
                            return int("".join(re.findall("&page=([0-9]+)>", link)))
                        except ValueError:
                            return int("".join(re.findall("&page=([0-9]+)&", link)))
                return -1
            except KeyError:
                return -1

        return {
            "Status-Code": response.status_code,
            "X-RateLimit-Limit": response.headers["X-RateLimit-Limit"],
            "X-RateLimit-Remaining": response.headers["X-RateLimit-Remaining"],
            "X-RateLimit-Reset": response.headers["X-RateLimit-Reset"],
            "Last-Page": _findLastPage(),
        }

    def returnRateLimit(self) -> int:
        """Gets the current rate limit of the oauthToken.

        Returns:
            int: The current rate limit of the oauthToken provided to the application.
        """
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Metrics-Dashboard",
            "Authorization": "token {}".format(self.token),
        }

        data = requests.get(
            url="https://api.github.com/rate_limit", headers=headers
        ).json()

        return data["resources"]["core"]["remaining"]


class GitHubCommitWebScraper:
    """Class to scrape HTML content from GitHub commit pages."""

    def __init__(self) -> None:
        """Initalizes the class."""
        pass

    def openConnection(self, url: str) -> BeautifulSoup:
        """Creates a BeautifulSoup object that is stored as a class variable.

        Parameters:
            url: A string that is formatted: https://github.com/{user}/{repo}/{commit}. Will be accessed via a GET request and its HTML content will be made availible as a BeautifulSoup object accessible via the *soup* class variable.

        Returns:
            An instance of a BeautifulSoup Web Scraper.
        """
        resp = requests.get(url=url).text
        return BeautifulSoup(markup=resp, features="html.parser")
