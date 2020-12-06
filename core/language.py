import json
from typing import Tuple, Any
from hanspell import spell_checker


def correct_text(text: str) -> Tuple[str, Any]:
    """
    Returns (corrected_text, correction_info)
    """
    result = spell_checker.check(text).as_dict()
    return result["checked"], json.dumps(result)

