from similarity_checker import similarity_score


def calculate_risk(new_username, existing_users):

    risk_score = 0
    matches = []

    for user in existing_users:

        existing_username = user["username"]

        score = similarity_score(new_username, existing_username)

        similarity_percent = round(score * 100, 2)

        if similarity_percent >= 70:

            matches.append({
                "username": existing_username,
                "email": user["email"],
                "similarity": similarity_percent
            })

            if similarity_percent >= 90:

                risk_score += 70

            else:

                risk_score += 30

    # profile image empty detection (basic version)
    risk_score += 25

    return risk_score, matches


def get_status(risk_score):

    if risk_score >= 90:

        return "Fake"

    elif risk_score >= 50:

        return "Suspicious"

    else:

        return "Real"