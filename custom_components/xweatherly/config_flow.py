from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME, CONF_LATITUDE, CONF_LONGITUDE

from .const import (
    DOMAIN,
    CONF_CLIENT_ID,
    CONF_CLIENT_SECRET,
    CONF_UPDATE_INTERVAL,
    CONF_FORECAST_COUNT_DAILY,
    CONF_FORECAST_COUNT_HOURLY,
    DEFAULT_NAME,
    DEFAULT_UPDATE_INTERVAL,
    DEFAULT_FORECAST_COUNT_DAILY,
    DEFAULT_FORECAST_COUNT_HOURLY,
)


class XweatherlyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Xweatherly."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Create the config entry with provided data
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        schema = vol.Schema(
            {
                vol.Required(CONF_CLIENT_ID): str,
                vol.Required(CONF_CLIENT_SECRET): str,
                vol.Optional(CONF_LATITUDE, default=self.hass.config.latitude): float,
                vol.Optional(CONF_LONGITUDE, default=self.hass.config.longitude): float,
                vol.Optional(CONF_NAME, default=DEFAULT_NAME): str,
                vol.Optional(CONF_UPDATE_INTERVAL, default=DEFAULT_UPDATE_INTERVAL): int,
                vol.Optional(CONF_FORECAST_COUNT_DAILY, default=DEFAULT_FORECAST_COUNT_DAILY): vol.All(
                    vol.Coerce(int), 
                    vol.Range(min=1, max=21)
                ),
                vol.Optional(CONF_FORECAST_COUNT_HOURLY, default=DEFAULT_FORECAST_COUNT_HOURLY): vol.All(
                    vol.Coerce(int), 
                    vol.Range(min=1, max=504)
                ),
            }
        )

        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
