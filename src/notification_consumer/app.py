def lambda_handler(event, context):
    records = event.get("Records", [])

    print(
        f"PHASE 22: received "
        f"{len(records)} SQS record(s)"
    )

    return {
        "processed_records": len(records)
    }
