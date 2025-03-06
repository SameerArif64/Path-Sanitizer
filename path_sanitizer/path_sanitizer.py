replacements = {
    '<': '_lt_',
    '>': '_gt_',
    ':': '_col_',
    '"': '_qt_',
    '/': '_sl_',
    '\\': '_bsl_',
    '|': '_pip_',
    '?': '_qst_',
    '*': '_str_'
}

def sanitize(text: str) -> str:
    """
    Replaces restricted characters in a folder name with short identifiable tokens.

    Args:
        text (str): The original folder name.

    Returns:
        str: A sanitized folder name with short tokens.
    """
    for char, token in replacements.items():
        text = text.replace(char, token)
    return text

def reverse_sanitize(text: str) -> str:
    """
    Reverses the sanitized string by replacing tokens back with restricted characters.

    Args:
        text (str): The sanitized string.

    Returns:
        str: The original string with restricted characters restored.
    """
    for token, char in replacements.items():
        text = text.replace(token, char)
    return text