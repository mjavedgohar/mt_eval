from json import loads
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from Campaign.models import Campaign, CampaignData, CampaignTeam

class Command(BaseCommand):
    help = 'Validates campaign data batches'

    def add_arguments(self, parser):
        parser.add_argument(
          'campaign_name', type=str,
          help='Name of the campaign you want to process data for'
        )
        parser.add_argument(
          '--activate', type=bool, default=False,
          help='Activate tasks after creation'
        )

    def handle(self, *args, **options):
        campaign_name = options['campaign_name']
        activate = options['activate']

        campaign = Campaign.objects.filter(campaignName=campaign_name)

        if not campaign.exists():
            _msg = 'Failure to identify campaign {0}'.format(campaign_name)
            self.stdout.write(_msg)
            return

        else:
            campaign = campaign[0]

        # Find super user
        superusers = User.objects.filter(is_superuser=True)
        if not superusers.exists():
            _msg = 'Failure to identify superuser'
            self.stdout.write(_msg)
            return

        validated_batches = 0
        activated_batches = 0
        for batch in campaign.batches.filter(dataValid=False, dataReady=False):
            batch_name = batch.dataFile.name
            batch_file = batch.dataFile

            try:
                batch_json = loads(str(batch_file.read(), encoding="utf-8"))
                batch.dataValid = True
                batch.dataReady = True
                validated_batches += 1

                if activate:
                    batch.activate()
                    activated_batches += 1

                batch.save()

            except:
                continue

        _msg = 'Validated {0} batches'.format(validated_batches)
        self.stdout.write(_msg)

        _msg = 'Activated {0} batches'.format(activated_batches)
        self.stdout.write(_msg)
