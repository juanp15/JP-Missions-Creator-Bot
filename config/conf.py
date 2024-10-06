prefix = "!" # The prefix used to call the bot commands.

lang = "en" # "en" or "es"

allowedGuildId = 1111111111111111111 # Your server ID # Example: 1111111111111111111
missionsTextVoiceChannel = "" # ID Missions channel and briefing channel # Example: "<#1111111111111111111> | <#1111111111111111111>"
editorRoleId = 1111111111111111111 # Role id required for commands bot # Example: 1111111111111111111
usersRoleId = "" # Mention a user role # Example: "<@&111111111111111111>""

# Aircraft or helicopters for each class
aircraftByClass = {
    "CAP": [
        "F-14 Tomcat", 
        "F/A-18C Hornet", 
        "F-16C Viper", 
        "Dassault Mirage 2000C", 
        "JF-17 Thunder", 
        "F-86F Sabre", 
        "F-5E Tiger II", 
        "Mitsubishi F-1", 
        "MiG-19P Farmer"
    ],
    "TASMO": [
        "F/A-18C Hornet", 
        "F-16C Viper", 
        "F-14 Tomcat", 
        "JF-17 Thunder", 
        "Dassault Mirage 2000C"
    ],
    "STRIKE": [
        "F/A-18C Hornet", 
        "F-16C Viper", 
        "Su-25T Frogfoot", 
        "MiG-15Bis Fagot", 
        "JF-17 Thunder", 
        "AV-8B Harrier II", 
        "F-15E Strike Eagle", 
        "F-5E Tiger II", 
        "F-4 Phantom II", 
        "A-10C Thunderbolt II", 
        "OH-58D Kiowa Warrior", 
        "Mi-24P Hind", 
        "Mi-8MTV2 Hip", 
        "Ka-50 Black Shark", 
        "AH-64D Apache"
    ],
    "CAS": [
        "F/A-18C Hornet", 
        "F-16C Viper", 
        "Su-25T Frogfoot", 
        "MiG-15Bis Fagot", 
        "AV-8B Harrier II", 
        "F-15E Strike Eagle", 
        "F-5E Tiger II", 
        "F-4 Phantom II", 
        "A-10C Thunderbolt II", 
        "OH-58D Kiowa Warrior", 
        "Mi-24P Hind", 
        "Mi-8MTV2 Hip", 
        "Ka-50 Black Shark", 
        "AH-64D Apache"
    ],
    "SEAD": [
        "F/A-18C Hornet", 
        "F-16C Viper", 
        "AV-8B Harrier II", 
        "JF-17 Thunder", 
        "F-4 Phantom II"
    ],
    "RIO": [
        "F-14 Tomcat", 
        "F-15E Strike Eagle", 
        "F-4 Phantom II", 
        "UH-1H Huey", 
        "SA342 Gazelle", 
        "OH-58D Kiowa Warrior", 
        "Mi-24P Hind", 
        "Mi-8MTV2 Hip", 
        "CH-47F Chinook", 
        "AH-64D Apache"
    ],
    "PILOT": [
        "SA342 Gazelle", 
        "UH-1H Huey", 
        "Mi-24P Hind", 
        "Mi-8MTV2 Hip", 
        "CH-47F Chinook"
    ],
    "CPG": [
        "Mi-8MTV2 Hip", 
        "AH-64D Apache", 
        "CH-47F Chinook", 
        "UH-1H Huey"
    ]
}

# Emojis used in the bot. Example: "<:emoji_name:emoji_id>"
emojis = {
    "CAP": "<:emoji_name:emoji_id>",
    "TASMO": "",
    "STRIKE": "",
    "CAS": "",
    "SEAD": "",
    "RIO": "",
    "PILOT": "",
    "CPG": "",
    "Inscriptions": "",
    "Date": "",
    "StartFinish": "",
    "TimeToStart": "",
    "AJS 37 Viggen": "",
    "Su-25T Frogfoot": "",
    "Su-27 Flanker": "",
    "Su-33 Flanker-D": "",
    "Su-57 Felon": "",
    "MiG-19P Farmer": "",
    "MiG-15Bis Fagot": "",
    "Dassault Mirage 2000C": "",
    "JF-17 Thunder": "",
    "AV-8B Harrier II": "",
    "F-86F Sabre": "",
    "F/A-18C Hornet": "",
    "F-16C Viper": "",
    "F-15E Strike Eagle": "",
    "F-14 Tomcat": "",
    "F-5E Tiger II": "",
    "F-4 Phantom II": "",
    "Mitsubishi F-1": "",
    "A-10C Thunderbolt II": "",
    "UH-1H Huey": "",
    "SA342 Gazelle": "",
    "OH-58D Kiowa Warrior": "",
    "Mi-24P Hind": "",
    "Mi-8MTV2 Hip": "",
    "Ka-50 Black Shark": "",
    "CH-47F Chinook": "",
    "AH-64D Apache": ""
}

# Intents configuration
confIntents = {
    "intents": {
        "auto_moderation": False,  # Enables automatic moderation to prevent unwanted behavior.
        "auto_moderation_configuration": False,  # Allows the bot to access automatic moderation settings.
        "auto_moderation_execution": False,  # Allows the bot to execute automatic moderation actions.
        "bans": False,  # Allows access to the list of banned users in the server.
        "dm_messages": True,  # Enables handling of direct messages (DMs) received.
        "dm_polls": True,  # Enables handling of polls in direct messages.
        "dm_reactions": True,  # Allows seeing reactions to direct messages.
        "dm_typing": False,  # Allows detecting if a user is typing in a direct message.
        "emojis": True,  # Allows the use of emojis in the bot.
        "emojis_and_stickers": True,  # Allows the use of emojis and stickers in messages.
        "guild_messages": True,  # Enables handling of messages sent in servers (guilds).
        "guild_polls": True,  # Enables handling of polls in server messages.
        "guild_reactions": True,  # Allows seeing reactions to messages in servers.
        "guild_scheduled_events": True,  # Allows handling scheduled events in the server.
        "guild_typing": False,  # Allows detecting if a user is typing in a server channel.
        "guilds": True,  # Allows the bot to access information about the servers it's in.
        "integrations": False,  # Allows the bot to access third-party integrations in the server.
        "invites": False,  # Allows the bot to access information about server invites.
        "members": True,  # Allows the bot to access the member list of the server.
        "message_content": True,  # Allows the bot to access the content of messages.
        "messages": True,  # Allows the bot to handle messages sent in servers.
        "moderation": False,  # Allows the bot to access moderation features in the server.
        "polls": True,  # Allows the bot to handle polls in general.
        "presences": False,  # Allows the bot to see the presence status (online/offline) of users.
        "reactions": True,  # Allows seeing reactions to messages (without specifying if they are in DMs or servers).
        "typing": False,  # Allows detecting if a user is typing in general (in DMs or in servers).
        "value": False,  # This intent is undocumented and could be a placeholder.
        "voice_states": False,  # Allows the bot to access information about users' voice states.
        "webhooks": False  # Allows the bot to handle webhooks in the server.
    },

    "intentValues": {
        "guilds": 1,  # discord.Intents.guilds
        "members": 2,  # discord.Intents.members
        "moderation": 4,  # discord.Intents.moderation
        "bans": 4,  # discord.Intents.bans
        "emojis": 8,  # discord.Intents.emojis
        "emojis_and_stickers": 8,  # discord.Intents.emojis_and_stickers
        "integrations": 16,  # discord.Intents.integrations
        "webhooks": 32,  # discord.Intents.webhooks
        "invites": 64,  # discord.Intents.invites
        "voice_states": 128,  # discord.Intents.voice_states
        "presences": 256,  # discord.Intents.presences
        "messages": 4608,  # discord.Intents.messages
        "guild_messages": 512,  # discord.Intents.guild_messages
        "dm_messages": 4096,  # discord.Intents.dm_messages
        "reactions": 9216,  # discord.Intents.reactions
        "guild_reactions": 1024,  # discord.Intents.guild_reactions
        "dm_reactions": 8192,  # discord.Intents.dm_reactions
        "typing": 18432,  # discord.Intents.typing
        "guild_typing": 2048,  # discord.Intents.guild_typing
        "dm_typing": 16384,  # discord.Intents.dm_typing
        "message_content": 32768,  # discord.Intents.message_content
        "guild_scheduled_events": 65536,  # discord.Intents.guild_scheduled_events
        "auto_moderation": 3145728,  # discord.Intents.auto_moderation
        "auto_moderation_configuration": 1048576,  # discord.Intents.auto_moderation_configuration
        "auto_moderation_execution": 2097152,  # discord.Intents.auto_moderation_execution
        "polls": 50331648,  # discord.Intents.polls
        "guild_polls": 16777216,  # discord.Intents.guild_polls
        "dm_polls": 33554432,  # discord.Intents.dm_polls
    }
}
