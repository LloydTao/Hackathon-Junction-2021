# Hackathon: Junction 2021

## Supercell x Finnish Refugee Council

Almost all young people 15-29-year-olds play games, and majority of them have experienced or witnessed some hate speech, discrimination or harassment while playing games. At the same time games have a huge potential for increasing empathy as games trigger emotions. Join us to develop technical solutions that help to reduce hate and increase empathy in games and especially game chats.

## Project

KeepChat is an in-game chat service with superpowers, making the chat space friendly for everyone. Our vision is to keep chat safe and inclusive, without requiring constant attention from moderators.

Messages sent to a chat room are screened for hate speech, profanity and otherwise malicious messages, before being delivered to other users. Our AI is able to learn what it should filter by looking at messages flagged by users within the chat. This allows it to continuously adapt to harmful language as it evolves, blocking euphemisms, dog whistles. and variations of slurs.

KeepChat also measures user sociability by looking at the content of messages, and how other chat users reply or react to their messages. Based on this social score, developers may wish to give in-game benefits to valuable members of the community, such as virtual currency, chat privileges or custom username styles.

The power of KeepChat comes from the fact it is completely plug-and-play. Your team doesn’t need to worry about servers, storage, collecting bad messages or re-configuring the filter. Everything is hosted on our cloud. Integrating your application with our chat service is seamless through our simple yet powerful API.

## Structure

This monorepo is composed of 3 core system components.

### Frontend

The `frontend/` contains a consumer web application which acts as an example chat room. It can be used to send a message, where it will be screened, or to flag an existing message within the chat room.

### Backend

The `backend/` handles the business logic of the consumer app. It stores users, messages and flags within a database, and exposes REST endpoints for sending and flagging messages.

### Data-Science

The `Data-Science/` directory contains the code necessary for training and deploying message screening models. The `backend/` uses these models to check if a message is profane, and the models can re-train on flagged messages within the database.
