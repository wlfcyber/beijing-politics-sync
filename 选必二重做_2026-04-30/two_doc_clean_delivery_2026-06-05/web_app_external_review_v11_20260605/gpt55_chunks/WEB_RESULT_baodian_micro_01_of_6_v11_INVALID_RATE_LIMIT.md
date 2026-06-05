# Invalid GPT-5.5 Pro Web Attempt - baodian-micro-01

- reviewed_via: Chrome visible ChatGPT web session through CDP browser automation
- status: invalid
- reason: The prompt insertion check passed, but the ChatGPT web page showed `请求过于频繁` and did not return the required `chunk_id` plus `verdict`.
- action: This result is not counted. Retry after the web rate limit cools down, or use the user's logged-in app/browser surface.
