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
# Deployment

This code is in `app.py`

We will deploy to HuggingFace Spaces.

Also check that there's no README file within the main directory. If there is one, please delete it. The deploy process creates a new README file in this directory for you.

1. Visit https://huggingface.co and set up an account  
2. From the Avatar menu on the top right, choose Access Tokens. Choose "Create New Token". Give it WRITE permissions.
3. Take this token and add it to your .env file: `HF_TOKEN=hf_xxx` and see note below if this token doesn't seem to get picked up during deployment  
4. From the main folder, enter: `uv run gradio deploy` and if for some reason this still wants you to enter your HF token, then interrupt it with ctrl+c and run this instead: `uv run dotenv -f ../.env run -- uv run gradio deploy` which forces your keys to all be set as environment variables   
5. Follow its instructions: name it "career_conversation", specify app.py, choose cpu-basic as the hardware, say Yes to needing to supply secrets, provide your openai api key, your pushover user and token, and say "no" to github actions.  

#### Extra note about the HuggingFace token

A couple of students have mentioned the HuggingFace doesn't detect their token, even though it's in the .env file. Here are things to try:   
1. Restart Cursor   
2. Rerun load_dotenv(override=True) and use a new terminal (the + button on the top right of the Terminal)   
3. In the Terminal, run this before the gradio deploy: `$env:HF_TOKEN = "hf_XXXX"`  
Thank you James and Martins for these tips.  

#### More about these secrets:

If you're confused by what's going on with these secrets: it just wants you to enter the key name and value for each of your secrets -- so you would enter:  
`OPENAI_API_KEY`  
Followed by:  
`sk-proj-...`  

And if you don't want to set secrets this way, or something goes wrong with it, it's no problem - you can change your secrets later:  
1. Log in to HuggingFace website  
2. Go to your profile screen via the Avatar menu on the top right  
3. Select the Space you deployed  
4. Click on the Settings wheel on the top right  
5. You can scroll down to change your secrets, delete the space, etc.