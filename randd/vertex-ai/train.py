from google.cloud import aiplatform

aiplatform.init(experiment=EXPERIMENT_NAME,
                experiment_tensorboard=TENSORBOARD_URI)
aiplatform.start_run(RUN_NAME)  # 「run-xxxxxx」という実行名を渡す

aiplatform.start_upload_tb_log(
    tensorboard_experiment_name=EXPERIMENT_NAME,
    experiment_display_name=EXPERIMENT_NAME,
    description="gcs tensorboard log",
    run_name_prefix=RUN_NAME,
    logdir=LOGGING_DIR,
)

# paramsは訓練用パラメーター
aiplatform.log_params(params)

# 訓練のコード〜〜〜

# eval_metricsは評価結果
aiplatform.log_metrics(eval_metrics)

aiplatform.end_upload_tb_log()
aiplatform.end_run()
