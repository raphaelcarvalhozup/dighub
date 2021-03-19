<p align="center">
</p>
<h1 align="center">
  Iara
</h1>
<p>
Iara is a tool that uses GitHub API to search through users/orgs for leaks and show it to the user in a friendly way. You can use an Authentication Token your GitHub account to access private repos and it is possible to specify the repo that you want to search in.
</p>

## CLI Flags

-  <b>-h, --help</b>   Show help message
-  <b>-u, -user</b>    User or organization to search in.
-  <b>-t, -token</b>   Insert your GitHub Token if you want to do an authenticated search.
-  <b>-r, -repo</b>    Insert a repo if you want to do a more specific search.

## Roadmap

- [x] MVP 
- [ ] Arg for dork list selection
- [ ] Improve search with strings that have more than 2 words.
- [ ] Return more than 1 snippet per code.
- [ ] Create a file output.
- [ ] Create a graphical output with HTML.
