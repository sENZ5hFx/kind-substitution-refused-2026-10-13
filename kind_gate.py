"""Kind-substitution gate. A wrong-kind answer counts only if someone published it."""

def kind_gate(sentence_retrieved, kinds_differ, owned_counterfactual, authors_separate):
    if not sentence_retrieved:
        return "NO_SENTENCE"
    if not kinds_differ:
        return "SAME_KIND"
    if owned_counterfactual:
        return "OWNED_COUNTERFACTUAL"
    if authors_separate:
        return "AUTHORS_ALREADY_SEPARATE"
    return "KIND_SUBSTITUTION"


if __name__ == "__main__":
    synthetic = kind_gate(True, True, False, False)
    same = kind_gate(True, False, False, False)
    assert synthetic == "KIND_SUBSTITUTION"
    assert same == "SAME_KIND"
    print("controls_ok", True)
