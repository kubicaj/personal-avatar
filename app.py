import inspect

import gradio as gr

from personal_avatar_llm import PersonalAvatarLLM
from ui.profile_page import PAGE_CSS, build_profile_page


class RecruiterProfileApp:
    """Main recruiter profile page with a CV download and guided AI avatar chat."""

    def chat(self, message, history, avatar: PersonalAvatarLLM) -> str:
        return avatar.chat_callback_function(message, history)

    def start_application(self):
        launch_signature = inspect.signature(gr.Blocks.launch)
        blocks_kwargs = {}
        if "css" not in launch_signature.parameters:
            blocks_kwargs["css"] = PAGE_CSS

        with gr.Blocks(**blocks_kwargs) as app:
            avatar_state = gr.State(None)

            def create_avatar():
                return PersonalAvatarLLM()

            app.load(fn=create_avatar, inputs=[], outputs=[avatar_state])

            build_profile_page(chat_callback=self.chat, avatar_state=avatar_state)
        launch_kwargs = {}
        if "css" in launch_signature.parameters:
            launch_kwargs["css"] = PAGE_CSS
        app.launch(**launch_kwargs)


if __name__ == "__main__":
    RecruiterProfileApp().start_application()
