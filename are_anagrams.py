def are_anagrams(a: str, b: str) -> bool:
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Should be strings")
    
    a_clean = a.replace(" ", "").lower()
    b_clean = b.replace(" ", "").lower()
    return sorted(a_clean) == sorted(b_clean)
