from config import settings
from github.client import GithubClient
from models.manager import Manager
from models.member import Member
from repo.parser import RepoParser
from repo.reports.file_writer import ReportFileWriter2
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator
from repo.reports_generator import ReportsGenerator
from repo.writer import ReportWrite

if __name__ == '__main__':
    response = GithubClient.get_repos_by_user(settings.get('user', default=None))
    if response['status_code'] == 200:
        repos = RepoParser.parser(response['body'])
        html = ReportsGenerator.build(HTMLGenerator, repos)
        markdown = ReportsGenerator.build(MarkdownGenerator, repos)

        ReportWrite.write(html)
        ReportWrite.write(markdown, ReportFileWriter2)
        print(response['body'])
    else:
        print(response['body'])
