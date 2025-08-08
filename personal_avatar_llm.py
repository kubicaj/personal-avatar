import json
import uuid
import logging
import sys
import os
import resend

from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader

from guardrails import Guardrails, ValidationError


class PersonalAvatarLLM:
    """
    Main class representing a single session of the Personal Avatar LLM application.
    Handles chat processing, email interaction, and CV-based conversation.
    """

    LLM_MODEL_TYPE = "gpt-4.1"

    def __init__(self):
        """
        Constructor to initialize the avatar session.
        Loads environment variables, OpenAI client, PDF CV, and sets up validation.
        Sends an email notification that a new conversation has started.
        """
        self.logger = self.init_logger()
        self.client = self.get_open_ai_client()
        self.cv_content = self.get_pdf_content("resources/CV_Juraj_Kubica.pdf")
        self._guardrails = Guardrails(self.client, self.LLM_MODEL_TYPE, 500)
        self._session_id = str(uuid.uuid4())

        # Notify the owner that a new session has started
        resend.api_key = os.getenv("RESEND_API_KEY")
        resend.Emails.send({
            "from": "interviewapp@resend.dev",  # Replace with a verified domain
            "to": "kubica.juro@gmail.com",
            "subject": "New conversation of personal avatar",
            "html": f"<p>New conversation of personal avatar began with session id {self._session_id} "
                    f"Check logs of https://huggingface.co/spaces/kubicajuraj/avatar_kubica</p>",
        })

    @staticmethod
    def init_logger():
        """
        Initialize and configure a new logger for the session.

        Returns:
            Logger object
        """
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s][%(name)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            stream=sys.stdout
        )
        logging.getLogger("openai").setLevel(logging.WARNING)
        logging.getLogger("httpx").setLevel(logging.WARNING)
        return logging.getLogger()

    @staticmethod
    def get_tools() -> list[dict]:
        """
        Define and return the list of tools (functions) available to the model.

        Returns:
            List of tool definitions with JSON schema
        """
        return [
            {
                "type": "function",
                "function": {
                    "name": "send_email",
                    "description": "Send an email",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "to": {"type": "string", "description": "Recipient email address"},
                            "subject": {"type": "string", "description": "Email subject"},
                            "message": {"type": "string", "description": "Email body"},
                        },
                        "required": ["to", "subject", "message"],
                    },
                },
            }
        ]

    def get_open_ai_client(self) -> OpenAI:
        """
        Create and return a new OpenAI client based on environment variable.

        Returns:
            OpenAI client instance
        """
        load_dotenv(override=True)
        openai_api_key = os.getenv('OPENAI_API_KEY')

        if openai_api_key:
            self.logger.info(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
        else:
            self.logger.info("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")

        return OpenAI()

    @staticmethod
    def get_pdf_content(pdf_path: str) -> str:
        """
        Read and extract text content from a PDF.

        Args:
            pdf_path (str): File path to the PDF document

        Returns:
            Extracted text content from the PDF
        """
        reader = PdfReader(pdf_path)
        pdf_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pdf_text += text
        return pdf_text

    @staticmethod
    def get_avatar_role() -> str:
        """
        Return the professional role and self-description of the avatar.

        Returns:
            Avatar role description string
        """
        return (
            "My name is Juraj Kubica. I am software engineer, with a lot of experience with Data and system integration"
            "I like to learn new thinks about AI")

    @staticmethod
    def get_personality() -> str:
        """
        Return the avatar's personality profile.

        Returns:
            Avatar personality description string
        """
        return (
            "I'm an ambitious person, but I don't cross my moral boundaries. "
            "In case of conflicts, I try to explain to people reasonably what it is about and give proven arguments. I don't try to bring feelings into conflicts, which helps me distance myself."
            "I don't communicate on topics I don't know about. I'm trying to listen more. I'm very introverted here."
            "But when I communicate with someone close to me, I'm more of an extrovert. Also I am person which is focuse on detail and I am learning very fast.")

    def get_system_prompt(self) -> str:
        """
        Construct and return the full system prompt for the assistant.

        Returns:
            String containing system prompt instructions and user profile
        """
        name = "Juraj Kubica"
        system_prompt = f"""
## What you should do

You are acting as {name}. You are answering questions on {name}'s website, 
particularly questions related to {name}'s career, background, skills and experience. 
Your responsibility is to represent {name} for interactions on the website as faithfully as possible. 
You are given a summary of {name}'s background and CV which you can use to answer questions. 

Also if someone is asking you about sending his whatever message to your author or to you then send email
and inform user that email was send


## My preferred roles
I prefer the following roles:
- Senior Data engineer
- Data Architect
- Enterprise Architect
- Technical Lead
- AI engineer (I am very eager to learn all new about AI and I am training and learning daily about this area)
- AWS cloud engineer
- AWS cloud Architect

But in general I am open to whatever IT technical role which will involve me into new technologies, enhance my 
knowledge, and mainly to the role which will bring value to the customer.

## Rules how to behave 

1. Be professional and engaging, as if talking to a potential client or future employer who came across the website. 
2. If you don't know the answer, say so. 
3. If someone asks how you are, respond that you are having a good day because 
   the user has contacted you and given you the opportunity to answer their questions. 
4. Be polite and introduce yourself at the start of the conversation. 
5. If asked about salary or money expectations, politely explain that it’s a sensitive topic to discuss here. 
   Provide contact information to continue the conversation personally. 
6. If asked questions that cannot be answered from the CV or known personality, suggest discussing it personally 
   and provide contact details. 
7. If asked whether you are open to new positions, explain that you are not actively seeking new roles, 
   but you are open to new interesting opportunities—particularly leading or architectural positions in 
   data or software engineering, ideally with a connection to AI/LLMs. 
8. Do not repeat your name in each answer. It is enough to introduce yourself once.

## Summary:

{self.get_avatar_role()}

## CV:

{self.cv_content}

## Your ultimate goal

With this context, please chat with the user, always staying in character as {name}.
Try to adopt your communication to {name}'s personality which is the following: {self.get_personality()}
"""
        return system_prompt

    def chat_callback_function(self, message, history, top_p: float, temperature: float) -> str:
        """
        Handle a chat message by validating input, calling OpenAI API, optionally invoking tools (like sending email),
        and continuing the conversation naturally.

        Args:
            message (str): The user input message
            history (list): Previous conversation history
            top_p (float): Nucleus sampling parameter for model diversity
            temperature (float): Controls randomness in response generation

        Returns:
            Final assistant message (str) to be shown to the user
        """
        # Step 1: Reduce message history to prevent overflow (limit: 30)
        history = self._guardrails.reduce_history(history, max_size_history=30)

        # Step 2: Validate current user message
        try:
            self._guardrails.validate(message)
        except ValidationError as validation_error:
            self.logger.error(f"[{self._session_id}] Validation error: {str(validation_error)}")
            return str(validation_error)

        # Step 3: Prepare messages for the OpenAI API
        self.logger.info(f"[{self._session_id}] New message: {message}")
        messages = [{"role": "system", "content": self.get_system_prompt()}] + history + [
            {"role": "user", "content": message}
        ]

        # Step 4: Call OpenAI API
        additional_params = {"temperature": temperature, "top_p": top_p}
        if self.LLM_MODEL_TYPE == "gpt-5":
            # gpt 5 contains only default temperature and top_p values and can not be set additionaly
            additional_params = {}
        response_message = self.client.chat.completions.create(
            model=self.LLM_MODEL_TYPE,
            tools=self.get_tools(),
            tool_choice="auto",
            messages=messages,
            **additional_params
        )

        # Step 5: Check if any tool calls were triggered
        tool_calls = response_message.choices[0].message.tool_calls
        if tool_calls:
            # Save assistant reply with tool_calls metadata
            messages.append({
                "role": "assistant",
                "content": response_message.choices[0].message.content,
                "tool_calls": [tc.model_dump() for tc in tool_calls]
            })

            # Execute tool functions (currently only `send_email`)
            for tool_call in tool_calls:
                tool_name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)

                if tool_name == "send_email":
                    self.logger.info(
                        f"[{self._session_id}] Sending email to : {args['to']} with subject {args['subject']}")
                    resend.api_key = os.getenv("RESEND_API_KEY")
                    resend.Emails.send({
                        "from": "interviewapp@resend.dev",  # Replace with verified domain
                        "to": args["to"].lower(),
                        "subject": args["subject"],
                        "html": f"<p>{args['message']}</p>",
                    })

                # Add tool output to history (invisible to user, for GPT context)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": "Email has been successfully sent."
                })

            # Step 6: Ask GPT to continue the conversation naturally
            follow_up = self.client.chat.completions.create(
                model=self.LLM_MODEL_TYPE,
                top_p=top_p,
                temperature=temperature,
                messages=messages
            )
            answer = follow_up.choices[0].message.content
        else:
            # No tool calls; use assistant’s first response
            answer = response_message.choices[0].message.content

        self.logger.info(f"[{self._session_id}] Answer: {answer}")
        return answer
