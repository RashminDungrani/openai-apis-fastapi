<h1 align="center">OpenAI APIs with FastAPI application</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/RashminDungrani/openai-apis-fastapi/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Integrate OpenAI APIs into FastAPI applications for easier consumption using Swagger UI, feel free to use and modify.</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Authors](#authors)
- [Screenshots](#screenshots)

## 🧐 About <a name = "about"></a>

This project involves integrating OpenAI APIs into FastAPI applications to facilitate calling them using the Swagger UI. FastAPI is a modern Python web framework for building APIs quickly and efficiently. By leveraging FastAPI's features and integrating OpenAI's APIs, developers can build applications with powerful AI capabilities such as language translation, sentiment analysis, text summarization, question-answering, and more. The project may involve designing and implementing RESTful API endpoints that interact with the OpenAI APIs, configuring authentication and security measures, and documenting the APIs for consumption using the Swagger UI.

## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites

To work on a FastAPI project, you'll need to ensure that your environment is set up with the following prerequisites:

- Python 3.10 or higher installed
- Poetry package manager installed

### Installation

1. Activate virtual environment
    ```shell
    poetry shell
    ```
1. Install dependencies
    ```shell
    poetry install
    ```
1. Setup your env file that is under `envs` directory
    - duplicate `dev.example.env` file in `envs` directory and rename it `dev.env`
    - Sign up to openai website and get free API token and paste it in `OPENAI_API_KEY` as value
1. Run FastAPI app
    ```shell
    python -m app
    ```
    OR use make command
    ```shell
    make run
    ```

## ✍️ Authors <a name = "authors"></a>

- [@rashmin](https://github.com/rashmindungrani) - Idea & Initial work

## 📄 Screenshot <a name = "screenshots"></a>

![OpenAI APIs - Swagger UI](screenshots/OpenAI%20APIs%20-%20Swagger%20UI.png)

### Show some 💗 and star the repo to support the project