import inspect
from pathlib import Path

import gradio as gr


PAGE_CSS = Path(__file__).resolve().with_name("profile.css").read_text(encoding="utf-8")
RESOURCES_PATH = Path(__file__).resolve().parents[1] / "resources"
CV_PATH = RESOURCES_PATH / "CV_Juraj_Kubica.pdf"
PHOTO_URL = "https://huggingface.co/spaces/kubicajuraj/avatar_kubica/resolve/main/resources/photo.png"


def build_profile_page(chat_callback, avatar_state):
    """Build the profile page and its embedded CV chat interface."""
    with gr.Column(elem_id="cv-page"):
        with gr.Row(elem_id="cv-header"):
            gr.HTML("<div class='wordmark'>Juraj Kubica</div>")
            gr.HTML(
                """
                <nav class="header-links" aria-label="Contact links">
                    <a href="mailto:kubica.juro@gmail.com" aria-label="Email Juraj">
                        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/></svg>
                        Email
                    </a>
                    <a href="https://www.linkedin.com/in/juraj-kubica-897a3590" target="_blank" rel="noopener noreferrer">
                        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.58c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.13 1.44-2.13 2.94v5.68H9.35V8.99h3.41v1.57h.05c.47-.9 1.63-1.85 3.36-1.85 3.59 0 4.25 2.36 4.25 5.43v6.31zM5.34 7.42a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM3.56 20.45h3.56V8.99H3.56v11.46zM22.22 0H1.78C.8 0 0 .77 0 1.72v20.56C0 23.23.8 24 1.78 24h20.44C23.2 24 24 23.23 24 22.28V1.72C24 .77 23.2 0 22.22 0z"/></svg>
                        LinkedIn
                    </a>
                </nav>
                """
            )

        with gr.Row(elem_id="profile-hero"):
            with gr.Column(elem_id="profile-copy"):
                gr.HTML(
                    """
                    <div class="eyebrow">Data engineering · Architecture</div>
                    <h1>Senior Data Engineer &amp; Data Architect</h1>
                    <div class="role-line">AI-ready data platforms · Market data · Semantic layers</div>
                    <p class="profile-summary">I design cloud data platforms and integration frameworks. At Barclays, I work on Market Data onboarding, integration, and governance, and help make Market Data usable for AI through semantic layers. My recent work also includes RAG architectures and MCP for connecting LLMs with enterprise data and tools.</p>
                    <div class="current-role">
                        <span class="current-role-label">Current role</span>
                        <span class="current-role-title">VP, Senior Data Engineer at Barclays</span>
                    </div>
                """
                )

                with gr.Row(elem_id="hero-actions"):
                    gr.DownloadButton(
                        label="Download CV",
                        value=CV_PATH,
                        variant="primary",
                        size="md",
                        elem_id="cv-download",
                        scale=0,
                        min_width=0,
                    )
                    gr.HTML(
                        """
                        <a class="action-link chat-cta" href="#conversation-section" aria-label="Scroll to chat with my AI avatar">
                            <svg class="action-link-icon" viewBox="0 0 24 24" aria-hidden="true">
                                <circle cx="12" cy="12" r="9.25" />
                                <circle cx="12" cy="9" r="2.7" />
                                <path d="M6.8 17.7c.8-2.4 2.6-3.7 5.2-3.7s4.4 1.3 5.2 3.7" />
                            </svg>
                            <span>Chat with my AI avatar</span>
                            <svg class="action-link-icon action-link-arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6" /></svg>
                        </a>
                        """
                    )

            with gr.Column(elem_id="profile-image-column"):
                gr.HTML(
                    f'<img src="{PHOTO_URL}" '
                    'alt="Portrait of Juraj Kubica" loading="eager">',
                    elem_id="profile-photo",
                )

        gr.HTML(
            """
            <section id="expertise" aria-label="Professional focus">
                <div class="expertise-item">
                    <strong>Cloud data platforms</strong>
                    <span>Snowflake, AWS, Databricks, and data pipelines</span>
                </div>
                <div class="expertise-item">
                    <strong>AI data enablement</strong>
                    <span>Semantic layers, RAG, and MCP for enterprise data</span>
                </div>
                <div class="expertise-item">
                    <strong>Architecture &amp; integration</strong>
                    <span>System design, reusable pipelines, and technical leadership</span>
                </div>
            </section>
            """
        )

        gr.HTML(
            """
            <section id="experience-section" class="content-section" aria-labelledby="experience-title">
                <div class="content-section-heading">
                    <div class="section-label">Career</div>
                    <h2 id="experience-title">Experience</h2>
                    <p>Recent roles across market data, cloud data platforms, and system integration.</p>
                </div>
                <div class="experience-list">
                    <article class="experience-entry">
                        <div class="experience-company-block">
                            <div class="experience-brand">
                                <span class="company-logo barclays" aria-hidden="true">B</span>
                                <span class="experience-company">Barclays</span>
                            </div>
                            <span class="experience-dates">Nov 2025 - Present</span>
                        </div>
                        <div>
                            <h3>VP, Senior Data Engineer</h3>
                            <p>Responsible for Market Data onboarding, integration, and governance across Snowflake, AWS, and Databricks. Help enable Market Data for AI through semantic layers, and coordinate onboarding with S&amp;P, Bloomberg, and LSEG.</p>
                        </div>
                    </article>
                    <article class="experience-entry">
                        <div class="experience-company-block">
                            <div class="experience-brand">
                                <span class="company-logo profinit" aria-hidden="true">P</span>
                                <span class="experience-company">Profinit</span>
                            </div>
                            <span class="experience-dates">Jan 2018 - Nov 2025</span>
                        </div>
                        <div>
                            <h3>IT Architect / AWS Competency Lead</h3>
                            <p>Consulted across pharma and financial services, focusing on data and software architecture. Project roles included Big Data Developer, Tech Lead, and Architect.</p>
                        </div>
                    </article>
                    <article class="experience-entry">
                        <div class="experience-company-block">
                            <div class="experience-brand">
                                <span class="company-logo cgi" aria-hidden="true">C</span>
                                <span class="experience-company">CGI</span>
                            </div>
                            <span class="experience-dates">Jun 2015 - Dec 2017</span>
                        </div>
                        <div>
                            <h3>Analyst / Programmer</h3>
                            <p>Developed Java and system integration applications, progressing into technical leadership and software architecture work.</p>
                        </div>
                    </article>
                    <article class="experience-entry">
                        <div class="experience-company-block">
                            <div class="experience-brand">
                                <span class="company-logo onesto" aria-hidden="true">O</span>
                                <span class="experience-company">Onesto</span>
                            </div>
                            <span class="experience-dates">May 2014 - May 2015</span>
                        </div>
                        <div>
                            <h3>Java Developer</h3>
                            <p>Developed features and improved components for a web-based business travel management system.</p>
                        </div>
                    </article>
                    <article class="experience-entry">
                        <div class="experience-company-block">
                            <div class="experience-brand">
                                <span class="company-logo scheidt-bachmann" aria-hidden="true">S+B</span>
                                <span class="experience-company">Scheidt &amp; Bachmann</span>
                            </div>
                            <span class="experience-dates">Nov 2012 - Apr 2014</span>
                        </div>
                        <div>
                            <h3>Java Developer</h3>
                            <p>Built an emulator used to test petrol station processes without the expensive hardware devices.</p>
                        </div>
                    </article>
                </div>
            </section>

            <section id="selected-work" class="content-section" aria-labelledby="selected-work-title">
                <div class="content-section-heading">
                    <div class="section-label">Selected work</div>
                    <h2 id="selected-work-title">Data platforms, built for reuse</h2>
                </div>
                <div class="selected-work-grid">
                    <article class="project-card">
                        <h3>Multi-platform data integration framework</h3>
                        <div class="project-role">Architect · Technical team lead</div>
                        <p>Designed a reusable ETL and pipeline framework across AWS Glue, Databricks, and StreamSets, with automated deployment. An AI assistant to help users understand the framework and build pipelines is in progress.</p>
                        <div class="project-metric">
                            <strong>&gt;40%</strong>
                            <span>faster pipeline development and deployment compared with previous solutions</span>
                        </div>
                        <div class="project-tech">AWS Glue · Databricks · StreamSets · Spark · Python · Terraform</div>
                    </article>
                    <article class="project-card">
                        <h3>Data Integration Gateway</h3>
                        <div class="project-role">Solution architect</div>
                        <p>Designed a portal to standardize onboarding and use of data integration tools, including Airflow pipeline orchestration and AI assistance for pipeline creation.</p>
                        <div class="project-tech">AWS · Airflow · FastAPI · Python · CI/CD · Security architecture</div>
                    </article>
                </div>
            </section>

            <section id="certifications" aria-labelledby="certifications-title">
                <h2 id="certifications-title">Certifications</h2>
                <div class="certification-list">
                    <a href="https://www.credly.com/badges/119f348b-e6b8-4e7f-a245-d6e9ef70e252/linked_in_profile" target="_blank" rel="noopener noreferrer">
                        <span class="credential-logo aws" role="img" aria-label="AWS logo">
                            <svg viewBox="0 0 48 34" aria-hidden="true" focusable="false">
                                <text x="3" y="21" fill="#263747" font-family="Arial, sans-serif" font-size="19" font-weight="700" letter-spacing="-1.1">aws</text>
                                <path d="M8 25c8 6 22 6 31-1" fill="none" stroke="#f39a1e" stroke-linecap="round" stroke-width="2.7" />
                                <path d="m34 23 5 1-2 4" fill="none" stroke="#f39a1e" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" />
                            </svg>
                        </span>
                        <span class="credential-name">AWS Certified AI Practitioner</span>
                        <svg class="credential-arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3h8v8M13 3 4 12" /></svg>
                    </a>
                    <a href="https://www.credly.com/badges/4547e28b-0e4d-4811-a78b-80664f3281f6/linked_in_profile" target="_blank" rel="noopener noreferrer">
                        <span class="credential-logo aws" role="img" aria-label="AWS logo">
                            <svg viewBox="0 0 48 34" aria-hidden="true" focusable="false">
                                <text x="3" y="21" fill="#263747" font-family="Arial, sans-serif" font-size="19" font-weight="700" letter-spacing="-1.1">aws</text>
                                <path d="M8 25c8 6 22 6 31-1" fill="none" stroke="#f39a1e" stroke-linecap="round" stroke-width="2.7" />
                                <path d="m34 23 5 1-2 4" fill="none" stroke="#f39a1e" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" />
                            </svg>
                        </span>
                        <span class="credential-name">AWS Certified Solutions Architect - Associate</span>
                        <svg class="credential-arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3h8v8M13 3 4 12" /></svg>
                    </a>
                    <a href="https://credentials.databricks.com/570769bc-33ab-45c6-ae1a-e55d65c80ef6#acc.x7TBcOJH" target="_blank" rel="noopener noreferrer">
                        <span class="credential-logo databricks" role="img" aria-label="Databricks logo">
                            <svg viewBox="0 0 40 40" aria-hidden="true" focusable="false">
                                <path d="m20 4 14 8-14 8-14-8 14-8Z" fill="none" stroke="#e64a35" stroke-linejoin="round" stroke-width="2.8" />
                                <path d="m6 19 14 8 14-8M6 26l14 8 14-8" fill="none" stroke="#e64a35" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.8" />
                            </svg>
                        </span>
                        <span class="credential-name">Databricks Certified Data Engineer Professional</span>
                        <svg class="credential-arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3h8v8M13 3 4 12" /></svg>
                    </a>
                    <a href="https://credentials.databricks.com/4942430e-b1e0-417d-87bd-b0cd702be874#acc.oJ02CVHi" target="_blank" rel="noopener noreferrer">
                        <span class="credential-logo databricks" role="img" aria-label="Databricks logo">
                            <svg viewBox="0 0 40 40" aria-hidden="true" focusable="false">
                                <path d="m20 4 14 8-14 8-14-8 14-8Z" fill="none" stroke="#e64a35" stroke-linejoin="round" stroke-width="2.8" />
                                <path d="m6 19 14 8 14-8M6 26l14 8 14-8" fill="none" stroke="#e64a35" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.8" />
                            </svg>
                        </span>
                        <span class="credential-name">Databricks Certified Data Engineer Associate</span>
                        <svg class="credential-arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3h8v8M13 3 4 12" /></svg>
                    </a>
                </div>
            </section>
            """
        )

        with gr.Row(elem_id="conversation-section"):
            with gr.Column(elem_id="conversation-intro"):
                gr.HTML(
                    """
                    <div class="section-label">AI avatar</div>
                    <h2>Ask about my experience</h2>
                    <p>Chat with my AI avatar about a project, technology, role, or certification listed on this page.</p>
                    <div class="conversation-hint">Replies are based on my CV and professional profile.</div>
                    """
                )

            with gr.Column(elem_id="conversation-card"):
                chatbot_kwargs = {
                    "elem_id": "chatbot",
                    "show_label": False,
                    "height": 300,
                    "min_height": 260,
                    "layout": "panel",
                    "buttons": [],
                    "placeholder": (
                        "<div style='text-align:center; padding: 28px 16px;'>"
                        "<div style='font-size: 15px; font-weight: 600; color: #1e2937;'>Ask a question about my work</div>"
                        "<div style='margin-top: 7px; color: #596678;'>For example: “What data engineering experience do you have?”</div>"
                        "</div>"
                    ),
                }
                chatbot_signature = inspect.signature(gr.Chatbot)
                if "type" in chatbot_signature.parameters:
                    chatbot_kwargs["type"] = "messages"
                chatbot_kwargs = {
                    key: value
                    for key, value in chatbot_kwargs.items()
                    if key in chatbot_signature.parameters
                }

                chat_kwargs = {
                    "fn": chat_callback,
                    "additional_inputs": [avatar_state],
                    "chatbot": gr.Chatbot(**chatbot_kwargs),
                    "textbox": gr.Textbox(
                        placeholder="Ask about my experience…",
                        show_label=False,
                        lines=1,
                    ),
                    "title": None,
                    "submit_btn": "Send",
                    "stop_btn": False,
                }
                chat_signature = inspect.signature(gr.ChatInterface)
                if "type" in chat_signature.parameters:
                    chat_kwargs["type"] = "messages"
                chat_kwargs = {
                    key: value
                    for key, value in chat_kwargs.items()
                    if key in chat_signature.parameters
                }
                gr.ChatInterface(**chat_kwargs)

        gr.HTML(
            """
            <footer id="recruiter-links">
                <div class="contact-heading">Interested in discussing an opportunity?</div>
                <div class="contact-links">
                    <a href="mailto:kubica.juro@gmail.com">
                        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/></svg>
                        kubica.juro@gmail.com
                    </a>
                    <a href="https://www.linkedin.com/in/juraj-kubica-897a3590" target="_blank" rel="noopener noreferrer">
                        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.58c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.13 1.44-2.13 2.94v5.68H9.35V8.99h3.41v1.57h.05c.47-.9 1.63-1.85 3.36-1.85 3.59 0 4.25 2.36 4.25 5.43v6.31zM5.34 7.42a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM3.56 20.45h3.56V8.99H3.56v11.46zM22.22 0H1.78C.8 0 0 .77 0 1.72v20.56C0 23.23.8 24 1.78 24h20.44C23.2 24 24 23.23 24 22.28V1.72C24 .77 23.2 0 22.22 0z"/></svg>
                        LinkedIn
                    </a>
                    <a href="tel:+420601121964">
                        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24c1.12.37 2.33.56 3.57.56.55 0 1 .45 1 1V20c0 .55-.45 1-1 1C10.61 21 3 13.39 3 4c0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.24.19 2.45.56 3.57a1 1 0 0 1-.25 1.02l-2.19 2.2z"/></svg>
                        +420 601 121 964
                    </a>
                </div>
            </footer>
            <div class="footer-note">Juraj Kubica · Data engineering, integration, architecture, and AI</div>
            """
        )
