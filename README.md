---
title: avatar_kubica
emoji: 💻
colorFrom: indigo
colorTo: yellow
sdk: gradio
sdk_version: 5.38.0
app_file: app.py
pinned: false
---

# Avatar Kubica Deployment Guide

This repository contains a Gradio app defined in `app.py`, deployed to Hugging Face Spaces:

👉 [Live App](https://huggingface.co/spaces/kubicajuraj/avatar_kubica)

> **Note**: Ensure there is no existing `README.md` in the root directory before deployment. Hugging Face Spaces will automatically generate one for you.

---

## Prerequisites

Before setting up the project, make sure you have:

1. [UV installed](https://docs.astral.sh/uv/getting-started/installation/)
2. Installed all dependencies from `requirements.txt`  
   Run:
   ```bash
   uv pip install -r requirements.txt
   ```

---

## Account Setup

### 1. Resend

- Sign up at [resend.com](https://resend.com/)
- Generate your API key at [resend.com/api-keys](https://resend.com/api-keys)

### 2. Hugging Face

- Create an account at [huggingface.co](https://huggingface.co/)
- Go to your profile → **Access Tokens** → **Create New Token** with **WRITE** permissions

### 3. Open API

- Create an account at [openapi](https://platform.openai.com/docs/overview)
- In the [settings](https://platform.openai.com/settings/organization/api-keys) generate the API key which you will need later

### 4. Huggingface setup

- In your huggingface space setup the secrets:
  - `OPENAI_API_KEY`
  - `RESEND_API_KEY`
  - 
---

## Local Deployment

1. Create a `.env` file in the root directory with the following content:

    ```env
    OPENAI_API_KEY=<your-openai-api-key>
    HF_TOKEN=<your-huggingface-token>
    RESEND_API_KEY=<your-resend-api-key>
    ```

2. Run the following command from the project root:

    ```bash
    uv run gradio deploy
    ```

    If prompted again for your Hugging Face token, stop the process (`Ctrl + C`) and instead run:

    ```bash
    uv run dotenv -f ../.env run -- uv run gradio deploy
    ```

    This ensures all required secrets are loaded from your environment.

3. Follow the interactive deployment instructions:
    - App name: `avatar_kubica`
    - Entry file: `app.py`
    - Hardware: `cpu-basic`
    - Supply secrets: **Yes**
    - Provide API keys when prompted
    - GitHub Actions: **No**

---

## Automatic Deployment (via GitHub Actions)

This repo includes a GitHub Actions workflow named **Deploy Gradio App** that automatically deploys the app whenever changes are pushed to the `main` branch.

### Steps:

1. **One-time setup**: Add the following secrets to your GitHub repository:

    - `HF_TOKEN`

2. Push or merge your changes into the `main` branch.

3. GitHub Actions will trigger the **Deploy Gradio App** workflow automatically. Monitor it to ensure it completes successfully.

---

Happy deploying! 🚀
