from dagster import job, op

@op
def fetch_data(context):
    context.log.info("Fetching data")
    # Your data fetching logic here
    return "Data fetched"

@op
def process_data(context, data):
    context.log.info(f"Processing data: {data}")
    # Your data processing logic here
    return "Data processed"

@job
def data_ingestion_job():
    data = fetch_data()
    process_data(data)
