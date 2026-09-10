def health_score(metrics):
    score = 0

    # CPU Health
    if metrics["cpu"] > 80:
        score += 40

    # Memory Health (Simulated)
    if metrics["memory"] > 80:
        score += 20

    # Disk Health (Simulated)
    if metrics["disk"] > 90:
        score += 20

    # Network Health
    if (metrics["network_in"] + metrics["network_out"]) > 500:
        score += 20

    # Determine overall system status
    if score <= 30:
        status = "Healthy"
    elif score <= 60:
        status = "Monitor"
    else:
        status = "Adaptation Required"

    return score, status