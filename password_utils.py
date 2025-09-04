import re

def match_pass_criteria(s: str, criteria: list = [r"[!@#\$%\^&\*\(\)_\+-=\{\}\;:,\.\?]", r"[a-z]", r"[A-Z]", r".{8,}"]) -> bool:
    failed = []
    for c in criteria:
        if not re.search(c, s):
            failed.append(f"Password must meet criteria: {str(c).replace("\\", "")}")
    
    if not failed:
        return True
    
    #for f in failed:
    #    print(f)
    
    return False