#!/bin/sh

# github configuration
echo "[Github Account]"
while [[ -z "$username" ]]
do
    read -p "Username: " username
done

while [[ -z "$password" ]]
do
    read -s -p "Password: " password
done

# twitter configuration
echo "\n\n[Twitter Application]"
while [[ -z "$consumer_key" ]]
do
    read -p "Consumer Key: " consumer_key
done

while [[ -z "$consumer_secret" ]]
do
    read -p "Consumer Secret: " consumer_secret
done

while [[ -z "$access_token" ]]
do
    read -p "Access Token: " access_token
done

while [[ -z "$access_token_secret" ]]
do
    read -p "Access Token Secret: " access_token_secret
done

echo "\n[Twitter Account]"
while [[ -z "$username_to_mention" ]]
do
    read -p "Username to mention: @" username_to_mention
done

touch bot/config.ini

cat << EOF > bot/config.ini
[github]
username: $username
password: $password
[twitter_application]
consumer_key: $consumer_key
consumer_secret: $consumer_secret
access_token: $access_token
access_token_secret: $access_token_secret
[twitter_account]
username_to_mention: $username_to_mention
EOF

echo "\nDone."