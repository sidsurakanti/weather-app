def converter(temp: int) -> int:
    """Converts from kelvin to fahrenheit"""
    # formula = (K − 273.15) × 9/5 + 32 = F
    return round((temp - 273.15) * 9/5 + 32)
