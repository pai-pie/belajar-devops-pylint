"""Example of a refactored code with improved readability."""


def calculate_result(first_value, second_value, third_value, values, number):
    """Calculate a result based on the given conditions."""
    if first_value and not second_value and third_value is None:
        try:
            result = values[0] + number + 1
            print(first_value + second_value)
            return result
        except (IndexError, TypeError):
            return None

    return None


calculate_result(True, False, None, [2], 3)
