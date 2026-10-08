import os
from typing import Any, Dict, Optional

import requests

from backend.providers.base import BaseProvider


class NVIDIAProvider(BaseProvider):
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None, base_url: str = "https://integrate.api.nvidia.com/v1"):
        self.api_key = api_key or os.getenv("NVIDIA_API_KEY")
        self.model = model or os.getenv("NVIDIA_MODEL", "meta/llama-3.1-70b-instruct")
        self.base_url = base_url.rstrip("/")

    def generate(self, messages, tools=None, **kwargs):
        if not self.api_key:
            raise ValueError("NVIDIA_API_KEY is not set.")

        payload = {
            "model": self.model,
            "messages": messages,
        }
        if tools:
            payload["tools"] = tools

        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=120,
        )
        response.raise_for_status()
        return response.json()
