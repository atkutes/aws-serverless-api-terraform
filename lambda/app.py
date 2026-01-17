def handler(event, context):
    # Saves if there is no  None
    if not event:
        return {
            "statusCode": 200,
            "body": "Hello from Lambda (no event received)"
        }

    # Save if queryStringParameters is None
    params = event.get("queryStringParameters") or {}
    name = params.get("name", "World")

    return {
        "statusCode": 200,
        "body": f"Hello, {name}! Your serverless API is running."
    }
