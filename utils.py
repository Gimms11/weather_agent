from typing import Any
from langchain_core.messages import BaseMessage


def format_content(response_or_content: Any) -> str:
    """Extract and normalize plain text from any LLM response or content format.

    Supports:
        - BaseMessage instances (AIMessage, HumanMessage, etc.)
        - Raw strings
        - Lists of strings, dicts ({'text': ...}), or objects with a 'text' attribute
        - Dict payloads containing 'text' or 'content' keys
    """
    if isinstance(response_or_content, BaseMessage):
        content = response_or_content.content
    else:
        content = response_or_content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                if "text" in item:
                    parts.append(str(item["text"]))
                elif "content" in item:
                    parts.append(str(item["content"]))
            elif hasattr(item, "text"):
                parts.append(str(item.text))
            else:
                parts.append(str(item))
        return "".join(parts)

    if isinstance(content, dict):
        if "text" in content:
            return str(content["text"])
        if "content" in content:
            return str(content["content"])

    return str(content) if content is not None else ""
