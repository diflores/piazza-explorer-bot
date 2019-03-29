# Piazza Explorer Bot
A dead simple Telegram bot for sending periodic notifications.

## How to use

First, you will need a `.env` file with the following structure:

```
TOKEN=''
CHAT_ID=-1111111111111
```

You'll also need a Heroku app. After pushing the content of your repository to your Heroku app git repository, you have to run the following line:

```
heroku ps:scale bot=1
```

Then, you will be able to see your application logs using:

```
heroku logs
```

