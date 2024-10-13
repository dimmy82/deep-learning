from google.cloud import aiplatform

aiplatform.init(
    project=PROJECT_ID,
    location=LOCATION,
    experiment=EXPERIMENT_NAME,
    staging_bucket=BUCKET_URI,
)

job = aiplatform.CustomContainerTrainingJob(
    display_name=JOB,
    project=PROJECT_ID,
    location=LOCATION,
    container_uri=TRAIN_IMAGE,
    staging_bucket=BUCKET_URI,
)

job.run(
    args=[],
    replica_count=1,
    machine_type=TRAIN_COMPUTE,
    service_account=SERVICE_ACCOUNT,
    accelerator_type=accelerator_type,
    accelerator_count=accelerator_count,
    sync=True,
    environment_variables={
        "EXPERIMENT_NAME": EXPERIMENT_NAME,
        "BUCKET_DIR": f"/gcs{BUCKET_DIR}",
        "TENSORBOARD_URI": TENSORBOARD_URI,
    },
)
