# KeepChat - Managed Chat API with Adaptive Hate Speech Filtering

[Project submission](https://app.hackjunction.com/projects/junction-2021/view/61981367f4f3a100cb609452) | [Challenge specification](https://www.junction2021.com/challenges/supercell)

## Project

KeepChat is an in-game chat service with superpowers, making the chat space friendly for everyone. Our vision is to keep chat safe and inclusive, without requiring constant attention from moderators.

At a high level, KeepChat consists of a three-tier architecture.

![KeepChat architecture](assets\keepchat-architecture.png)

At the core of the system is the **chat API**, which handles the business logic of the chat rooms. This includes storing messages, processing new messages from users, and processing flags.

When a new message is processed, the chat API asks the **training and screening API** whether the message should be filtered. The AI responds with a `True` or `False`, and the backend will filter the message accordingly before storing it.

![KeepChat admin panel](assets\keepchat-admin-panel.png)

When a flag is processed, the chat API tells the AI to add the flagged message to its bank of harmful messages, and then **re-train** on this data. We envision expanding on this by requiring a certain number of flags or total user sociability score in order to add the message to the training data.

In order to demonstrate this functionality, a frontend **consumer application** communicates with the backend by using its chat endpoints.

This demonstrates the plug-and-play nature of the application; integrating KeepChat into an existing application is incredibly simple, as screening messages and re-training on flagged messages is built-in to the service.

## Teamwork

By splitting the project into the architecture mentioned prior, we were able to divide our team effectively. This involved giving individual team members ownership over some part of the system, and then exposing each part through a REST API, which kept the system loosely coupled.

The end result was a high development velocity within the team.

We leveraged Git and GitHub in order to distribute code between team members. It's important to prevent code-breaking changes from being pushed in a time-critical project, as these can block an entire team while the bug is fixed.

Therefore, any code changes went through a pull request, and we leveraged GitHub Actions in order to run quick code quality checks before accepting a PR.

![KeepChat pull requests](assets\keepchat-pull-requests.png)

## Results

We didn't bring home the bacon this time. Interestingly, the winner of our challenge also built a chat service with adaptive filtering, including the ability to re-train on reported messages.

However, they managed to deploy their system to Google Cloud Platform, and provided a link to use their application. Considering the product-focused nature of the hackathon, we should have aimed to put our application online.

Results aside, I would definitely call this weekend a success. We managed to effectively execute on an identical product scope to the challenge winners, which validates our project on both the technical and product level.

![KeepChat team photo](assets\keepchat-team-photo.png)

Go KeepChat!

## Structure

This monorepo is composed of 3 core system components.

### Frontend

The `frontend/` contains a consumer web application which acts as an example chat room. It can be used to send a message, where it will be screened, or to flag an existing message within the chat room.

### Backend

The `backend/` handles the business logic of the consumer app. It stores users, messages and flags within a database, and exposes REST endpoints for sending and flagging messages.

### Data science

The `data_science/` directory contains the code necessary for training and deploying message screening models. The `backend/` uses these models to check if a message is profane, and the models can re-train on flagged messages within the database.
