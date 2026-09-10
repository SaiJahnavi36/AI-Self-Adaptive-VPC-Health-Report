import time
from datetime import datetime

from cloudwatch_reader import get_all_metrics
from policies import evaluate
from report_generator import generate_report
from config import CHECK_INTERVAL_SECONDS


def run():
    print("=" * 60)
    print("AI-Based Self-Adaptive Secure VPC Engine Started")
    print("=" * 60)

    while True:
        try:
            print(f"\n[{datetime.utcnow().strftime('%d-%b-%Y %H:%M:%S UTC')}] Checking CloudWatch metrics...")

            # Read metrics from CloudWatch
            metrics = get_all_metrics()

            # AI Decision Engine
            decision, reason, service = evaluate(metrics)

            # Generate report and upload to S3
            report_file = generate_report(
                metrics,
                decision,
                reason,
                service
            )

            print(f"Report generated successfully: {report_file}")
            print(f"Next analysis in {CHECK_INTERVAL_SECONDS} seconds...")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    run()