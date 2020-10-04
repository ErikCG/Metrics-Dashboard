import pytest
import Commits
from datetime import datetime

# to run: cd into Code folder and type into the command line-> pytest -v TestCommits.py

sample_data_dict = {
        'sha': '691dd7efce02ea932803ea2aea248af62aa98bc8', 
        'node_id': 'MDY6Q29tbWl0NjU1NjMxMTQ6NjkxZGQ3ZWZjZTAyZWE5MzI4MDNlYTJhZWEyNDhhZjYyYWE5OGJjOA==', 
        'commit': {
                'author': {'name': 'Steph99rod', 'email': 'steph99rodriguez@gmail.com', 'date': '2016-08-12T15:23:48Z'}, 
                'committer': {'name': 'GitHub', 'email': 'noreply@github.com', 'date': '2016-08-12T15:23:48Z'}, 
                'message': 'Add files via upload', 
                'tree': {'sha': '86ad0e52c078ba17cf0938a3cd84dc8ed7762515', 
                        'url': 'https://api.github.com/repos/Steph99rod/Overpriced-CollegeT/git/trees/86ad0e52c078ba17cf0938a3cd84dc8ed7762515'}, 
                'url': 'https://api.github.com/repos/Steph99rod/Overpriced-CollegeT/git/commits/691dd7efce02ea932803ea2aea248af62aa98bc8', 
                'comment_count': 0, 
                'verification': {'verified': False, 'reason': 'unsigned', 'signature': None, 'payload': None}
                }, 
        'url': 'https://api.github.com/repos/Steph99rod/Overpriced-CollegeT/commits/691dd7efce02ea932803ea2aea248af62aa98bc8', 
        'html_url': 'https://github.com/Steph99rod/Overpriced-CollegeT/commit/691dd7efce02ea932803ea2aea248af62aa98bc8', 
        'comments_url': 'https://api.github.com/repos/Steph99rod/Overpriced-CollegeT/commits/691dd7efce02ea932803ea2aea248af62aa98bc8/comments', 
        'author': {
                'login': 'Steph99rod', 
                'id': 20929268, 
                'node_id': 'MDQ6VXNlcjIwOTI5MjY4', 
                'avatar_url': 'https://avatars1.githubusercontent.com/u/20929268?v=4', 
                'gravatar_id': '', 
                'url': 'https://api.github.com/users/Steph99rod', 
                'html_url': 'https://github.com/Steph99rod', 
                'followers_url': 'https://api.github.com/users/Steph99rod/followers', 
                'following_url': 'https://api.github.com/users/Steph99rod/following{/other_user}', 
                'gists_url': 'https://api.github.com/users/Steph99rod/gists{/gist_id}', 
                'starred_url': 'https://api.github.com/users/Steph99rod/starred{/owner}{/repo}', 
                'subscriptions_url': 'https://api.github.com/users/Steph99rod/subscriptions', 
                'organizations_url': 'https://api.github.com/users/Steph99rod/orgs', 
                'repos_url': 'https://api.github.com/users/Steph99rod/repos', 
                'events_url': 'https://api.github.com/users/Steph99rod/events{/privacy}', 
                'received_events_url': 'https://api.github.com/users/Steph99rod/received_events', 
                'type': 'User', 'site_admin': False
                }, 
        'committer': {
                'login': 'web-flow', 
                'id': 19864447, 
                'node_id': 'MDQ6VXNlcjE5ODY0NDQ3', 
                'avatar_url': 'https://avatars3.githubusercontent.com/u/19864447?v=4', 
                'gravatar_id': '', 
                'url': 'https://api.github.com/users/web-flow', 
                'html_url': 'https://github.com/web-flow', 
                'followers_url': 'https://api.github.com/users/web-flow/followers', 
                'following_url': 'https://api.github.com/users/web-flow/following{/other_user}', 
                'gists_url': 'https://api.github.com/users/web-flow/gists{/gist_id}', 
                'starred_url': 'https://api.github.com/users/web-flow/starred{/owner}{/repo}', 
                'subscriptions_url': 'https://api.github.com/users/web-flow/subscriptions', 
                'organizations_url': 'https://api.github.com/users/web-flow/orgs', 
                'repos_url': 'https://api.github.com/users/web-flow/repos', 
                'events_url': 'https://api.github.com/users/web-flow/events{/privacy}', 
                'received_events_url': 'https://api.github.com/users/web-flow/received_events', 
                'type': 'User', 'site_admin': False}, 
        'parents': [{
        'sha': 'ec7b3d36efb4ae21e4e02ffc8b4b70b1904d704f', 
        'url': 'https://api.github.com/repos/Steph99rod/Overpriced-CollegeT/commits/ec7b3d36efb4ae21e4e02ffc8b4b70b1904d704f', 
        'html_url': 'https://github.com/Steph99rod/Overpriced-CollegeT/commit/ec7b3d36efb4ae21e4e02ffc8b4b70b1904d704f'}]}
sample_commit = Commits.Logic(gha=None, data=[sample_data_dict], responseHeaders=None,cursor=None, connection=None)

class TestCommits(object):

        # testing the Commits class
        def test_get_author_name(self):
                assert sample_commit.get_author_name(0) == "Steph99rod"

        def test_get_committer_name(self):
                assert sample_commit.get_committer_name(0) == "GitHub"

        def test_get_message(self):
                assert sample_commit.get_message(0)  == "Add files via upload"

        def test_get_comment_count(self):
                assert sample_commit.get_comment_count(0) == 0
        
        def test_get_commits_url(self):
                assert sample_commit.get_commits_url(0) == 'https://api.github.com/repos/Steph99rod/Overpriced-CollegeT/git/commits/691dd7efce02ea932803ea2aea248af62aa98bc8'

        def test_get_comments_url(self):
                assert sample_commit.get_comments_url(0) == 'https://api.github.com/repos/Steph99rod/Overpriced-CollegeT/commits/691dd7efce02ea932803ea2aea248af62aa98bc8/comments'
        
        def test_get_author_date(self):
                assert sample_commit.get_author_date(0) == datetime(2016, 8, 12, 15, 23, 48)
