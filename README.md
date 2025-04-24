# 🛡️ GitHub Bot Blocker

A Python script to detect and block mass-following bot accounts from your GitHub profile. This script is designed to run daily via GitHub Actions.

---

## 🚀 Features
- Scans your followers
- Detects accounts following over a threshold (default: 1000)
- Blocks suspected bots
- Automates daily cleanup using GitHub Actions

---

## 🔧 Setup

### 1. Clone the Repo
```bash
git clone https://github.com/michaelachrisco/anti-mass-follow-bot.git
cd block-github-bots
```

### 2. Set Up GitHub Token
- Go to [GitHub Developer Settings](https://github.com/settings/tokens)
- Create a token with the following scopes:
  - `read:user`
  - `user:follow`
- Save this token as a GitHub Secret named `GH_TOKEN`

### 3. Update GitHub Actions Workflow
- Edit `.github/workflows/bot-blocker.yml`
- Replace `your-github-username` with your actual GitHub username

---

## 🛠️ Running Manually

You can also run the script locally:
```bash
export GITHUB_USERNAME=your-username
export GH_TOKEN=your-token
python main.py
```
### Example first run:
```
Scanning followers of @michaelachrisco...
Found 182 followers.
Neustradamus is a suspected bot. Blocking...
Blocked Neustradamus
...
LinuxJS is a suspected bot. Blocking...
Blocked LinuxJS
```


---

## 🕒 Automation via GitHub Actions

This project includes a workflow that runs daily at 2 AM UTC to:
- Fetch followers
- Identify suspected bots
- Block them automatically

You can trigger the workflow manually via the GitHub Actions tab as well.

---

## 📜 License
[GPL3.0](https://opensource.org/license/gpl-3-0)

---

