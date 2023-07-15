<p align="center">
  IPL Trivia Game. Built with OpenAI Functions and Kaggle IPL Dataset. 
</p>

## Introduction

This is an open-source AI trivia game that uses [OpenAI Functions](https://platform.openai.com/docs/guides/gpt/function-calling) and the [Kaggle IPL dataset](https://www.kaggle.com/datasets/purnend26/ipl-2023-dataset) to generate trivia questions for users.

https://github.com/sidPhoenix17/drd-trivia-backend/assets/16644933/b5b0175b-28cf-4b91-9b3f-fe1166bdf1ce


## Deploy your own

You can deploy your own version of the trivia game.

Backend code: https://github.com/droid-mohit/drd-trivia-backend
Frontend code: https://github.com/droid-mohit/IPLQuizApp/
Process we followed: https://notes.drdroid.io/create-a-trivia-game-about-a-random-topic-in-2-hours


## Setting Up Locally

To set up the game locally, you'll need to set up the following environment variables:

- `OPENAI_KEY` – your OpenAI_API key (you can get one [here](https://platform.openai.com/account/api-keys))

Note: The openai_key variable you might see in code is non-functional and you need to put one in env variables.

## Tech Stack

The quiz is built on the following stack:
- OpenAI [Function Calling](https://platform.openai.com/docs/guides/gpt/function-calling)
- Kaggle Dataset — [IPL 2023](https://www.kaggle.com/datasets/purnend26/ipl-2023-dataset)
- Code Stack: ReactJS, Python
- Infra Stack: Docker Compose + AWS EC2 + gunicorn (nightmare to deploy full stack application as a side project)
