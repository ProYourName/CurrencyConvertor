from currency_converter import CurrencyConverter

def Convert(fromm,to,value):
    try:
        converter = CurrencyConverter(fallback_on_wrong_date=True)
        converter = converter.convert(value,fromm,to)
        return converter

    except Exception as error:
        print(error)