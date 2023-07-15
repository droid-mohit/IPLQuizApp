<p align="center">
  IPL Trivia Game. Built with OpenAI Functions and Kaggle IPL Dataset. 
</p>

## Introduction

This is an open-source AI trivia game that uses [OpenAI Functions](https://platform.openai.com/docs/guides/gpt/function-calling) and the [Kaggle IPL dataset](https://www.kaggle.com/datasets/purnend26/ipl-2023-dataset) to generate trivia questions for users.

https://github.com/sidPhoenix17/drd-trivia-backend/assets/16644933/b5b0175b-28cf-4b91-9b3f-fe1166bdf1ce


## Deploy your own

You can deploy your own version of the trivia game.

Backend code: https://github.com/droid-mohit/drd-trivia-backend
Frontend code: https://github.com/droid-mohit/drd-trivia-backend
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


## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.
