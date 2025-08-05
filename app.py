import uuid
import gradio as gr

from personal_avatar_llm import PersonalAvatarLLM  # Your avatar logic with LLM, tools, etc.


class MyPersonalAvatarApp:
    """
    This class encapsulates the full application logic for Juraj Kubica's Personal Avatar.
    """

    def chat(self, message, history, top_p: float, temperature: float, personal_avatar_app: PersonalAvatarLLM) -> str:
        """
        Core chat function that sends user input and history to the avatar's LLM logic.
        """
        return personal_avatar_app.chat_callback_function(message, history, top_p, temperature)

    def start_application(self):
        """
        Initializes and launches the Gradio web app for the avatar.
        """

        # Contact info shown on the page
        CONTACTS = """
        <h3>Contact Juraj Kubica</h3>
        <ul style="font-size:16px;">
          <li>📧 <b>Email:</b> <a href="mailto:kubica.juro@gmail.com">kubica.juro@gmail.com</a></li>
          <li>🌐 <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/juraj-kubica-897a3590" target="_blank">https://www.linkedin.com/in/juraj-kubica-897a3590</a></li>
          <li>📱 <b>Phone:</b> +420 601 121 964</li>
        </ul>
        """

        # Instructions for users
        INSTRUCTIONS = """
        ## ℹ️ How to use this Avatar App

        - 💬 Ask me anything about **Juraj Kubica’s experience, skills, or background**.
        - 📄 You can **download Juraj’s CV** using the button on the right.
        - ✉️ Want to contact Juraj? Just ask: _"Can you send an email to Juraj saying..."_
        - 🧠 I’m powered by AI and trained on Juraj’s career and personality—talk to me as if you’re talking to him.
        """

        with gr.Blocks(theme=gr.themes.Ocean()) as cv_app:

            interview_application = gr.State(None)

            def set_new_llm_app():
                return PersonalAvatarLLM()

            cv_app.load(fn=set_new_llm_app, inputs=[], outputs=[interview_application])

            # Header and guidance
            gr.Markdown(
                "# 👨‍💻 Welcome! I'm Juraj Kubica's Avatar\n\nAsk me anything about my professional journey below."
            )
            gr.Markdown(INSTRUCTIONS)

            with gr.Row():
                gr.HTML(CONTACTS)
                gr.File(value="resources/CV_Juraj_Kubica.pdf", label="Download CV 📄", interactive=True)

            gr.Markdown("---")

            # Main chat interface
            gr.ChatInterface(
                fn=self.chat,
                type="messages",
                additional_inputs=[
                    gr.Slider(0.0, 1.0, label="top_p", value=0.3, render=False),
                    gr.Slider(0.0, 2.0, label="temperature", value=0.5, render=False),
                    interview_application
                ],
                title=None,
                submit_btn="⬅ Send"
            )

        cv_app.launch()


if __name__ == '__main__':
    MyPersonalAvatarApp().start_application()
