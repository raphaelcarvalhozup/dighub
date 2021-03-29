<p align="center">
<a href="https://github.com/raphaelcarvalhozup/dighub">
  <img src="./images/logo.png" width="250" />
</a>
<h1 align="center">
  DigHub - The patient GitHub leak hunter<br>
</h1>

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

DigHub is a tool that uses GitHub API to search through users/orgs for leaks and shows it to the user in a friendly way. You can use an Authentication Token your GitHub account to access private repos and it is possible to specify the repo that you want to search in.

---

## Installation
- You will need Python installed.
- Clone this repository and then, inside its folder, run:<br>
  ```pip install -r requirements.txt```
  
## Usage
- Inside the repository directory in your terminal, use this command:<br>
  ```python dighub.py -u "USER/ORG" -r "REPO_NAME" -t "YOUR_GITHUB_TOKEN"```

- As an secure measure, you can set your token as an environment variable, in a way that you do not need to have your GitHub token in your terminal everytime you use the tool, for example:
```TOKEN="YOUR_TOKEN_HERE"```

- Execution Line and Result Not Found example:
<img src="./images/dighubhead.PNG" width="400">

- Filename search result example:
<img src="./images/filenameexample.PNG" width="400">

- String search result example:
<img src="./images/resultexample.PNG" width="400">

## CLI Flags

-  ```-h, --help```   Show help message.
-  ```-u, --user```    User or organization to search in.
-  ```-t, --token```   Insert your GitHub Token if you want to do an authenticated search. *Optional
-  ```-r, --repo```    Insert a repo if you want to do a more specific search. *Optional

---

## Using your own Dorklist

- While there is not a very simple way to select custom Dorklists yet, you can access the ```searcher.py``` file and change it manually, choosing a file of your preference, in this line:<br>
```dorks = open('./small_dorklist.txt').read().splitlines()```

---

## Roadmap

- [x] MVP 
- [ ] Arg for dork list selection
- [ ] Improve search with strings that have more than 2 words.
- [ ] Return more than 1 snippet per code.
- [ ] Create a file output.
- [ ] Create a graphical output with HTML.

---

<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
The source code is licensed under [Apache-2.0](https://opensource.org/licenses/Apache-2.0).
