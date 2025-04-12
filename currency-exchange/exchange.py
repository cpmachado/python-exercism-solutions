"""
Group of functions to power Chandler's currency calculator.
"""

from numbers import Number


def exchange_money(budget: Number, exchange_rate: Number) -> Number:
    """

    :param budget: Number - amount of money you are planning to exchange.
    :param exchange_rate: Number - unit value of the foreign currency.
    :return: Number - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget: Number, exchanging_value: Number) -> Number:
    """

    :param budget: Number - amount of money you own.
    :param exchanging_value: Number - amount of your money you want to exchange now.
    :return: Number - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget: Number, denomination: int) -> Number:
    """

    :param budget: Number - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def get_leftover_of_bills(budget: Number, denomination: int) -> Number:
    """

    :param budget: Number - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: Number - the leftover amount that cannot be exchanged given the current denomination.
    """

    return budget % denomination


def exchangeable_value(
    budget: Number, exchange_rate: Number, spread: int, denomination: int
) -> int:
    """

    :param budget: Number - the amount of your money you are planning to exchange.
    :param exchange_rate: Number - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    exchange_fee = (exchange_rate / 100) * spread
    exchanged_money = exchange_money(budget, exchange_fee + exchange_rate)
    bills = get_number_of_bills(exchanged_money, denomination)
    return get_value_of_bills(bills, denomination)
