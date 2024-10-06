# JP-Missions-Creator-Bot

## Description
This bot is designed to create missions embeds for the game DCS (Digital Combat Simulator) and users can join the missions by selecting the role thet want to play and the aircraft they want to fly.

## Features
- Create missions embeds
- Modify missions embeds
- Delete missions embeds command
- Join missions by selecting the role and aircraft
- Leave missions

## Installation
1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. Create a .env file and add the following variables:
```env
DATABASE_URL="mysql+pymysql://your_username:your_password@ip:port/your_database" # Replace the placeholders with your database credentials # Example: mysql+pymysql://root:password@localhost:3306/jp_missionsdb
DISCORD_TOKEN="your_discord_token"
``` 
5. Run the bot