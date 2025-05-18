# Dummy recommendation logic
def get_recommendation(symptoms: list[str]) -> list[str]:
    recommendations = []

    if "blurry vision" in symptoms:
        recommendations.append("Schedule an eye exam")
    if "eye pain" in symptoms:
        recommendations.append("Consult an ophthalmologist")
    if not recommendations:
        recommendations.append("Maintain regular checkups and eye hygiene")

    return recommendations
