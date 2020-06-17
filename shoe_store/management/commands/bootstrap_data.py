from shoe_store.models import ShoeType, ShoeColor
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populate the ShoeType and ShoeColor tables'

    def handle(self, *args, **options):
        for color in ShoeColor.SHOE_COLORS:
            ShoeColor.objects.create(color_name=color[0])

            self.stdout.write(self.style.SUCCESS(
                'Successfully closed color "%s"' % color[1]))

        for type_ in ShoeType.SHOE_TYPE:
            ShoeType.objects.create(style=type_[0])

            self.stdout.write(self.style.SUCCESS(
                'Successfully closed type "%s"' % type_[1]))
