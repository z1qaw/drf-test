import xml.etree.ElementTree as ET

import requests
from django.core.management.base import BaseCommand

from ...models import Currency


class Command(BaseCommand):
    def handle(self, *args, **options):
        currs_info = get_updates()
        for curr in currs_info:
            Currency.objects.update_or_create(
                name=curr['Name'], defaults={'rate': curr['Value'] / 10}
            )
        self.stdout.write(self.style.SUCCESS(
            'Currency instances has been successfully updated.'
            )
        )


def get_updates() -> list:
    updates = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currs_list = ET.fromstring(updates).findall('Valute')
    
    updates = []
    for c_el in currs_list:
        result = {}
        for item in list(c_el.iter())[1:]:
            result[item.tag] = item.text
        result['Value'] = float(result['Value'].replace(',', '.'))
        updates.append(result)
    
    return updates
