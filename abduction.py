# código baseado no material do professor

def abduction(kb, observations, explanation=set()):

    if observations:
        consequence = botton_up(kb)
        explanation = []
        observation_rules = []
        for ob in observation:
            observation_rules += kb["rules"][ob]

        for rule in observation_rules:
            is_explanation = True
            atoms = []

        for atom in rule:
            atoms.append(atom)

            if not (atom in consequence or atom in kb["assumables"]):
                is_explanation = False
                atoms = []
                break

        if is_explanation and not (rule in explanation):
            explanation += [rule]

    return [explanation]


def botton_up(kb):
    C = []

    if 'askables' in kb:
        for a in kb['askables']:
            if ask(a):
                C.append(a)

    new_consequence = True

    while new_consequence:
        new_consequence = False

        for head in kb['rules']:
            if head not in C:  # Very inneficent
                for body in kb['rules'][head]:
                    if not set(body).difference(set(C)):  # Very innefient
                        C.append(head)
                        new_consequence = True

    return C


def ask(askable):
    ans = input(f'Is {askable} true?')
    return True if ans.lower() in ['sim', 's', 'yes', 'y'] else False


if __name__ == "__main__":
    kb = {
        'rules':
         {
             'bronchitis': [['influenza'], ['smokes']],
             'coughing': [['bronchitis']],
             'wheezing': [['bronchitis']],
             'fever': [['influenza', 'infection']],
             'sore_throat': [['influenza']],
             'false': [['smokes', 'nonsmokers']]
         },
        'assumables': ['smokes', 'nonsmokers', 'influenza', 'infection']
    }
    observation = ['wheezing', 'fever', 'sore_throat']
    print(f"Explanation to {observation}: {abduction(kb, observation)}")
