from ..base import Base
from .account_helper import AccountHelper

from ..const import API_PATH
from ..const import API_ENDPOINT
import os
from ..exceptions import ClientException

class Balance(Base, AccountHelper):
    def __init__(self):
        Base.__init__(self)
        AccountHelper.__init__(self, endpoint=self._endpoint)

        if self._endpoint is not API_ENDPOINT['brokerage']:
            raise ClientException('Bad Endpoint: account paths require the full API (no sandbox!)')

        self._path = API_PATH['account']
        self._path += os.environ['API_ACCOUNT_ID'] + '/balances'

        self._data = self._api_response(endpoint=self._endpoint,
                                        path=self._path,
                                        payload=self._payload)

        self._key = self._data['balances']


    def _parse_response(self, attribute, **config):
        if 'update' in list(config.keys()) and config['update'] is False:
            pass

        else:
            # update the data if the `update` parameter is true
            self.update_data()  # updates by default, user must specify to not update from the API

        if 'inner' in list(config.keys()):

            return self._data['balances'][attribute][config['inner']]

        else:
            return self._data['balances'][attribute]

    def account_number(self, **config):
        """ Return the account number associated with the current account. """
        return self._parse_response(attribute='account_number', **config)

    def account_type(self, **config):
        """ Return the type of trading account. For example, ``'cash'``, ``'margin'``, ``'pdt'``. """
        return self._parse_response(attribute='account_type', **config)

    def cash_available(self, **config):
        """ Return the amount of funds ready for trading. """
        return self._parse_response(attribute='cash', inner='cash_available',**config)

    def close_pl(self, **config):
        """ Return the Profit and Loss of the current trading day's closed positions. """
        return self._parse_response(attribute='close_pl', **config)

    def current_requirement(self, **config):
        """ Return the option requirement of current account positions."""
        return self._parse_response(attribute='current_requirement', **config)

    def day_trade_buying_power(self, **config):
        """ Return the total amount of funds available for the purchase of fully marginable stock during the current 
            trading day. A portion of these funds cannot be held overnight."""
        return self._parse_response(attribute='day_trade_buying_power', **config)

    def dividend_balance(self, **config):
        """ Return the account's dividend balance. """
        return self._parse_response(attribute='dividend_balance', **config)

    def equity(self, **config):
        """ Return the account's equity value. """
        return self._parse_response(attribute='equity', **config)

    def fed_call(self, **config):
        """ Returns the amount that the account is in deficit for trades that have occurred but not been paid for. """
        return self._parse_response(attribute='fed_call', **config)

    def long_liquid_value(self, **config):
        """ Return the account's long liquid value. """
        return self._parse_response(attribute='long_liquid_value', **config)

    def long_market_value(self, **config):
        """ Return the account's long market value. """
        return self._parse_response(attribute='long_market_value', **config)

    def maintenance_call(self, **config):
        """ Return the amount that the account is under the minimum equity required in the account to 
            support the current holdings."""
        return self._parse_response(attribute='maintenance_call', **config)

    def market_value(self, **config):
        """ Return the market value of the account's positions. """
        return self._parse_response(attribute='market_value', **config)

    def net_value(self, **config):
        """ Return the net value of the account's positions. """
        return self._parse_response(attribute='net_value', **config)

    def open_pl(self, **config):
        """ Return the Profit & Loss of the account's current positions."""
        return self._parse_response(attribute='open_pl', **config)

    def option_buying_power(self, **config):
        """ Return the amount of funds available to purchase non-marginable securities. """
        return self._parse_response(attribute='option_buying_power', **config)

    def option_long_value(self, **config):
        """ Return the value of long options held in the account."""
        return self._parse_response(attribute='option_long_value', **config)

    def option_requirement(self, **config):
        """ Return the account's option requirement. """
        return self._parse_response(attribute='option_requirement', **config)

    def option_short_value(self, **config):
        """ Return the value of short options held in the account. """
        return self._parse_response(attribute='option_short_value', **config)

    def pending_cash(self, **config):
        """ Return the amount of cash that is being held for open orders. This is generally from funds that are
        transferred into the account or from selling profitable positions. """
        return self._parse_response(attribute='pending_cash', **config)

    def pending_orders_count(self, **config):
        """ Returns the account's amount of open orders."""
        return self._parse_response(attribute='pending_orders_count', **config)

    def sweep(self, **config):
        """ Sweep. Documentation in progress. """
        return self._parse_response(attribute='cash', inner='sweep', **config)

    def short_liquid_value(self, **config):
        """ Return the short liquid value of the account. """
        return self._parse_response(attribute='short_liquid_value', **config)

    def short_market_value(self, **config):
        """ Return the short market value of the account. """
        return self._parse_response(attribute='short_market_value', **config)

    def stock_buying_power(self, **config):
        """ Return the amount of funds available to purchase fully marginable securities. """
        return self._parse_response(attribute='stock_buying_power', **config)

    def stock_long_value(self, **config):
        """ Return the value of long stocks held in the account."""
        return self._parse_response(attribute='stock_long_value', **config)

    def stock_short_value(self, **config):
        """ Return the value of short stocks held in the account."""
        return self._parse_response(attribute='stock_short_value', **config)

    def uncleared_funds(self, **config):
        """ Return the amount of funds that are not currently available for trading. """
        return self._parse_response(attribute='uncleared_funds', **config)

    def unsettled_funds(self, **config):
        """ Return the amount of cash that is in the account from recent stock or option sales, but has not yet 
            settled. """
        return self._parse_response(attribute='cash', inner='unsettled_funds', **config)

    def total_cash(self, **config):
        """ Return the total amount of cash in the account."""
        return self._parse_response(attribute='total_cash', **config)

    def total_equity(self, **config):
        """ Return the total value of the account."""
        return self._parse_response(attribute='total_equity', **config)




