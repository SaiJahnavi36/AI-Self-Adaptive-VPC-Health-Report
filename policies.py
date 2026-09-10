def evaluate(metrics):
    cpu = metrics["cpu"]
    disk = metrics["disk"]
    net = metrics["network_in"] + metrics["network_out"]

    # CPU-based scaling
    if cpu > 80:
        return (
            "Scale Out",
            f"CPU utilization is {cpu:.2f}% (above 80%).",
            "Increase the Auto Scaling Group capacity."
        )

    elif cpu < 20:
        return (
            "Scale In",
            f"CPU utilization is {cpu:.2f}% (below 20%).",
            "Decrease the Auto Scaling Group capacity."
        )

    # Storage recommendation
    elif disk > 90:
        return (
            "Increase Storage",
            f"Disk utilization is {disk}% (above 90%).",
            "Expand the attached EBS volume."
        )

    # Network recommendation
    elif net > 500:
        return (
            "Investigate High Traffic",
            f"Network traffic is {net:.2f} MB (above 500 MB).",
            "Inspect VPC Flow Logs and Security Groups."
        )

    # Normal state
    else:
        return (
            "No Action",
            "All monitored metrics are within normal operating thresholds.",
            "No action required."
        )