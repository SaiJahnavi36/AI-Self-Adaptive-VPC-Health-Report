import boto3
from datetime import datetime, timedelta
from config import REGION, INSTANCE_ID

cloudwatch = boto3.client("cloudwatch", region_name=REGION)

def get_metric(metric_name, stat="Average"):
    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName=metric_name,
        Dimensions=[
            {
                "Name": "InstanceId",
                "Value": INSTANCE_ID
            }
        ],
        StartTime=datetime.utcnow() - timedelta(minutes=10),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=[stat]
    )

    datapoints = response.get("Datapoints", [])

    if not datapoints:
        return 0

    return sorted(datapoints, key=lambda p: p["Timestamp"])[-1][stat]


def get_all_metrics():
    cpu = get_metric("CPUUtilization")
    net_in = get_metric("NetworkIn") / (1024 * 1024)   # MB
    net_out = get_metric("NetworkOut") / (1024 * 1024) # MB

    return {
        "cpu": round(cpu, 2),
        "memory": 70,          # Simulated
        "disk": 55,            # Simulated
        "network_in": round(net_in, 2),
        "network_out": round(net_out, 2)
    }