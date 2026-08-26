# Install Go 1.25, Git, and VS Code

**Pin Go 1.25.x from [go.dev/dl](https://go.dev/dl/).**  
Do **not** `sudo apt install golang-go`. The Ubuntu package is often years behind.

Check the exact filename on go.dev the morning you teach (for example `go1.25.0` vs `go1.25.1`).

Verify for everyone:

```bash
go version
# expect: go version go1.25.x linux/amd64   (or darwin/arm64 on Apple silicon)
```

---

## Ubuntu (lab default)

```bash
# 1. Download (match the name on go.dev/dl)
wget https://go.dev/dl/go1.25.0.linux-amd64.tar.gz

# 2. Install into /usr/local/go
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.25.0.linux-amd64.tar.gz

# 3. Put Go on PATH
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc

# 4. Check
go version
go env GOROOT GOPATH
which go
```

If `wget` is blocked: download the `.tar.gz` in Firefox, then:

```bash
cd ~/Downloads
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.25.0.linux-amd64.tar.gz
```

Git is usually already present:

```bash
sudo apt update
sudo apt install -y git
git --version
```

VS Code: https://code.visualstudio.com/docs/setup/linux (`.deb` for Ubuntu).

Then:

1. Extensions → **Go** (publisher: **Go Team at Google**)
2. Command Palette (`Ctrl+Shift+P`) → **Go: Install/Update Tools** → select all → OK
3. `Ctrl+Shift+P` → **Preferences: Open User Settings (JSON)** → paste `vscode-settings.json` from this folder

---

## Windows (WSL2 + Ubuntu)

Go for this course lives **inside Ubuntu**, not in PowerShell. (Native Windows `node_modules` / `.exe` binaries are a later headache; stay in WSL.)

1. In **PowerShell as Administrator**:

   ```powershell
   wsl --install -d Ubuntu
   ```

   Reboot if Windows asks.

2. Open **Ubuntu** from the Start menu. Create a UNIX username/password.

3. Follow the **Ubuntu** section above **inside that terminal**.

4. Install VS Code on Windows, then from Ubuntu:

   ```bash
   cd ~
   code .
   ```

   The first run may install the WSL helper. Install the **Go** extension **in WSL** (the bar at the bottom left should say **WSL: Ubuntu**).

**Wrong:** `go version` in PowerShell showing something else, while class commands are copied into Ubuntu. Pick one: Ubuntu.

---

## macOS

1. Download the **Apple silicon** or **Intel** `.pkg` from [go.dev/dl](https://go.dev/dl/) and run it.  
   Or Homebrew: `brew install go` — still confirm `go version` is 1.25.x.
2. New Terminal:

   ```bash
   go version
   echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.zprofile
   # Apple silicon Homebrew Go is often already on PATH
   ```

3. VS Code from https://code.visualstudio.com — same Go extension and format-on-save as Ubuntu.
4. Git: `xcode-select --install` or `brew install git`.

---

## After install, create the class folder

```bash
mkdir -p ~/epic-go/hello
cd ~/epic-go/hello
```

Open that folder in VS Code: **File → Open Folder**.
