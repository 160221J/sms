# Day 1 troubleshooting

Walk the room with this page. Most failures are PATH, the distro Go package, or GitHub login.

| What they see | Likely cause | What you do |
| --- | --- | --- |
| `go: command not found` | PATH not loaded, or they used a **new** terminal after edit | `source ~/.bashrc` or close terminal and open again. `echo $PATH` should contain `/usr/local/go/bin`. `which go` |
| `go version` is 1.18 / 1.21 / `gccgo` | `apt install golang-go` | `sudo apt remove golang-go gccgo-go` then install from go.dev. `which go` must be `/usr/local/go/bin/go` |
| `wget` 403 / hang | lab firewall | USB tarball or browser download into `~/Downloads` |
| Permission denied on `/usr/local/go` | forgot `sudo` | repeat `sudo rm` / `sudo tar` |
| VS Code has no format on save | settings not saved, or folder not opened | Open **folder** `~/epic-go/hello`, not a single file. Paste `vscode-settings.json`. Status bar should say **Go** |
| `Could not import fmt` / gopls red squiggles | tools not installed | Command Palette → **Go: Install/Update Tools** |
| `undefined: fmt.println` | lowercase `p` | Teaching moment: **exported names are Capitalised**. `Println` |
| `go build` / `go run` : `package . is not in std` or module errors | they ran `go build .` with no `go.mod` | Today: `go run hello.go` and `go build -o hello hello.go` only |
| `./hello: No such file` | `go build` failed or they are in another directory | `ls`; `cd ~/epic-go/hello` |
| Git: `Please tell me who you are` | no identity | `git config --global user.name` and `user.email` |
| `git push` 403 / auth | HTTPS without token | GitHub → Settings → Developer settings → PAT, or `gh auth login` |
| `failed to push` unrelated histories | they created a README on GitHub | empty repo on GitHub, **no** README, **no** .gitignore on the website |
| Binary on GitHub (`hello` several MB) | `.gitignore` missing | add `hello` to `.gitignore`, `git rm --cached hello`, commit, push |
| Windows: works in Ubuntu, `go` missing in PowerShell | expected | Stay in **Ubuntu (WSL)** for all course commands |
| Dual-boot: project on `D:\` | later weeks | Day 1 keep `~/epic-go` **on the Linux home**, not the Windows NTFS drive |

## Nuclear reinstall (Ubuntu)

```bash
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf ~/Downloads/go1.25.0.linux-amd64.tar.gz
export PATH=/usr/local/go/bin:$PATH
go version
```

Add PATH to `~/.bashrc` if it is not already there.
