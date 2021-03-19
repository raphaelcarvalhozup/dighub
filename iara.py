import argparse
import searcher

parser = argparse.ArgumentParser(prog='toth', description='This tool uses GitHub API to do searchs hunting specific leaks. There are parameters that will really help to get a better search. Remember, authenticated searches take less time because you have more requests per minute.')
parser.add_argument('-user',
                    type=str,
                    required=True,
                    help='User or Organization to search in.')
parser.add_argument('-token',
                    action='store',
                    type=str,
                    required=False,
                    help='Insert your token if you want to do an authenticated search.')

parser.add_argument('-repo',
                    action='store',
                    type=str,
                    required=False,
                    help='Insert a repo if you want to do a more specific search.')

parsedArgs = parser.parse_args()

user = parsedArgs.user

token = parsedArgs.token

repo = parsedArgs.repo

if(token):
    searcher.search(user, token, repo)
else:
    searcher.search(user, None, repo)
