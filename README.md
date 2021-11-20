# Hackathon: Junction 2021

## Supercell x Finnish Refugee Council

Almost all young people 15-29-year-olds play games, and majority of them have experienced or witnessed some hate speech, discrimination or harassment while playing games. At the same time games have a huge potential for increasing empathy as games trigger emotions. Join us to develop technical solutions that help to reduce hate and increase empathy in games and especially game chats.

## Project

KeepChat is a game chat service which utilises AI to moderate the chat space. This includes screening messages for hate speech and profanity, measuring and rewarding user sociability, and the ability to learn from new instances of inapproprite messages flagged by the community.

### Features

**Screening** is the detection of communications based on known instances of good/bad messages. The AI is able to continuously re-train itself based on what chat users are **flagging** as good or bad messages. Developers can choose whether this data comes from only their own chat rooms, or from the global pool of moderated chat messages.

After implementing the chat service into their application, developers can choose how their system **moderates** individual messages and users. For example, built-in functionality can automatically censor bad messages by **replacing** or **blocking** profanity and hate speech.

On the other hand, developers may wish to give **in-game benefits** to valuable members of the community, such as virtual currency or custom username styles.

Chat rooms are hosted on the cloud, meaning that screening, flagging and moderating are **built-in** to the service. You just need to configure your moderation settings and access chats through our simple API.

## Structure

This monorepo is composed of 3 core system components.

### Frontend

The `frontend/` contains a consumer web application which acts as an example chat room. It can be used to send a message, where it will be screened, or to flag an existing message within the chat room.

### Backend

The `backend/` handles the business logic of the consumer app. It stores users, messages and flags within a database, and exposes REST endpoints for sending and flagging messages.

### Data-Science

The `Data-Science/` directory contains the code necessary for training and deploying message screening models. The `backend/` uses these models to check if a message is profane, and the models can re-train on flagged messages within the database.
