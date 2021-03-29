#!/usr/bin/env python3

import argparse
import searcher


def main():
    parser = argparse.ArgumentParser(prog='dighub',
                                     description='This tool uses GitHub API to do searchs hunting specific '
                                                 'leaks. There are parameters that will really help to get a '
                                                 'better search. Remember, authenticated searches take less '
                                                 'time because you have more requests per minute.')

    parser.add_argument('--user','-u',
                        type=str,
                        required=True,
                        help='User or Organization to search in.')

    parser.add_argument('--token','-t',
                        action='store',
                        type=str,
                        required=False,
                        help='Insert your token if you want to do an authenticated search.')

    parser.add_argument('--repo','-r',
                        action='store',
                        type=str,
                        required=False,
                        help='Insert a repo if you want to do a more specific search.')

    parsed_args = parser.parse_args()

    user = parsed_args.user
    token = parsed_args.token
    repo = parsed_args.repo

    if token:
        searcher.search(user, token, repo)
    else:
        searcher.search(user, None, repo)


if __name__ == '__main__':
    main()
