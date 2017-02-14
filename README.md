# contribution-alarm

> Daily Github-contribution Alarm on Twitter

## Install and Set Up

### 1. Create and run virtual environment

```bash
$ python3 -m venv env
$ source env/bin/activate
```

### 2. Install python packages

```bash
$ pip install -r requirements.txt
```

### 3. Set up config file.

```bash
$ ./install.sh
[Github]
Username: <github-username>
Password: <github-username>

[Twitter Application]
Consumer Key: <twitter-consumer-key>
Consumer Secret: <twitter-consumer-secret>
Access Token: <twitter-access-token>
Access Token Secret: <twitter-access-token-secret>

[Twitter Account]
username_to_mention: <twitter-username-to-mention>

Done.

```

## Deploy using Heroku Git

### 1. Add config file to git

Delete `*.ini` in `.gitignore` to deploy in Heroku. **Note that you should add `*.ini` again when you upload on github.**


### 2. Deploy on Heroku

```bash
$ heroku login
$ heroku git:remote -a <heroku-app-name>

$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

---

#### Other version
- Slack: [commit-alarm](https://github.com/geekhub-lab/commit-alarm)
- Telegram: [commit-telegram-bot](https://github.com/MuhunKim/commit-telegram-bot)


