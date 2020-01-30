from datetime import date, datetime

class Helpers(object) :
    """
    Helper functions and utilities to be used throughout SDK framework.
    """

    @staticmethod
    def json_serial(obj):
        """
        JSON serializer for objects not serializable by default json code
        """

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError ("Type %s not serializable" % type(obj))

    def update_avg(self, field, count, new_value, round_to) :
        """
        Update the an average value when knowing the value, the count, and the new value to be included.
        Round to a decimal placement.
        """

        return round(((field * (count - 1)) + new_value) / count, round_to)

    def calc_percentage(self, value_a, value_b, round) :
        """
        Calculate the percentage difference between two numbers.
        """

        return round((float(value_a - value_b) / value_a) * 100.0, round)
