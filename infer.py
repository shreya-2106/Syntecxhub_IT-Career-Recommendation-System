from rep import rep

def forward_chaining(facts):

    inferred = set(facts)
    explanation = []
    fired_rules = set()

    while True:
        rule_triggered = False
        for rule in sorted(rep, key=lambda x: x["priority"], reverse=True):

            if rule["id"] not in fired_rules:
                
                if all(condition in inferred for condition in rule["if"]):

                    for conclusion in rule["then"]:
                        if conclusion not in inferred:
                            inferred.add(conclusion)
                            explanation.append(
                                f"{rule['id']} fired → added {conclusion}"
                            )
                            rule_triggered = True

                    fired_rules.add(rule["id"])

        if not rule_triggered:
            break

    return inferred, explanation