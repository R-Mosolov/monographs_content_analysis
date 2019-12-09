from private_apps.AI_fiction_or_scientific.modules.main_indicators import text__dialog
from private_apps.AI_fiction_or_scientific.modules.preparation.indicators_constants import fiction_indicators
from private_apps.AI_fiction_or_scientific.modules.preparation.indicators_constants import scientific_indicators
from private_apps.AI_fiction_or_scientific.modules.preparation.indicators_constants import mean_calculator


def run():
    analyzed_text = text__dialog.calc()
    fiction_mean = fiction_indicators.TEXT__DIALOG
    scientific_mean = scientific_indicators.TEXT__DIALOG
    fiction_and_scientific_mean = mean_calculator.run()[4]

    if fiction_mean > scientific_mean:
        if analyzed_text > (fiction_mean - fiction_and_scientific_mean):
            is_fiction_text = True
        else:
            is_fiction_text = False
    else:
        if analyzed_text > (scientific_mean - fiction_and_scientific_mean):
            is_fiction_text = False
        else:
            is_fiction_text = True

    if is_fiction_text:
        return 1
    else:
        return 0
