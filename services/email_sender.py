import logging
import os

import resend


class EmailSender:
    """Small Resend-backed email service used by the avatar application."""

    DEFAULT_FROM = "interviewapp@resend.dev"

    def __init__(
        self,
        logger: logging.Logger | None = None,
        api_key: str | None = None,
        session_id: str | None = None,
    ):
        self.logger = logger or logging.getLogger(__name__)
        self.api_key = api_key or os.getenv("RESEND_API_KEY")
        self.session_id = session_id or "email-service"

    def send(
        self,
        *,
        to: str,
        subject: str,
        html: str,
        from_email: str = DEFAULT_FROM,
    ) -> bool:
        """Send an email and return False when delivery is unavailable."""
        if not self.api_key:
            self._log_warning("RESEND_API_KEY is not configured; skipping email")
            return False
        self.logger.info("Sending email via Resend from %s to %s with subject %s", from_email, to, subject)
        resend.api_key = self.api_key
        try:
            resend.Emails.send({
                "from": from_email,
                "to": to,
                "subject": subject,
                "html": html,
            })
            return True
        except Exception as email_error:
            self._log_warning(
                f"Resend email failed; continuing without email: {email_error}"
            )
            return False

    def _log_warning(self, message: str):
        self.logger.warning(f"[{self.session_id}] {message}")
