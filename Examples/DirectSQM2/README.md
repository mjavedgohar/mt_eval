# Appraise Evaluation System



Generating an example campaign with direct assessment tasks with SQM quality
levels. Note it uses exact same batches as standard direct assessment tasks:

    python manage.py StartNewCampaign Examples/DirectSQM2/manifest.json --batches-json Examples/Direct/batches3.json  --csv-output Examples/DirectSQM2/output.csv

    # See Examples/DirectSQM/outputs.csv for a SSO login for the annotator account
    # Collect some annotations, then export annotation scores...

    python manage.py ExportSystemScoresToCSV example6sqm
