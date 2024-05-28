# Appraise Evaluation System

    python manage.py init_campaign Examples/Data3/manifest.json

    # From the admin panel, create a campaign with the name 'examplespandata'
    # From the admin panel, add batches.json and add the batch to the campaign 'examplespandata'

    python manage.py validatecampaigndata examplespandata
    python manage.py ProcessCampaignData examplespandata Data
    python manage.py UpdateEvalDataModels
    python manage.py init_campaign Examples/Data3/manifest.json    --csv-output Examples/Data3/output4.csv

    # See Examples/Data/outputs.csv for a SSO login for the annotator account
    # Collect some annotations, then export annotation scores...

    python manage.py ExportSystemScoresToCSV examplespandata
