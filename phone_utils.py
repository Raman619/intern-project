def normalize_phone(phone: str) -> str:
    p = phone.replace(" ", "").replace("-", "")

    if p.startswith("+977") and len(p) == 14:
        return p

    if p.startswith("0") and len(p) == 11:
        return "+977" + p[1:]

    if len(p) == 10 and (p.startswith("98") or p.startswith("97")):
        return "+977" + p

    raise ValueError("Invalid phone number")