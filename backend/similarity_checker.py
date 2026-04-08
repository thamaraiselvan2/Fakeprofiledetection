from difflib import SequenceMatcher


def similarity_score(a, b):

    return SequenceMatcher(None, a.lower(), b.lower()).ratio()