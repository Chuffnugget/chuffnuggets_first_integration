"""Config flow for Chuffnuggets First Integration."""
from homeassistant import config_entries
import voluptuous as vol

from .const import DOMAIN

class NuggetCounterConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Chuffnuggets First Integration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Nugget Counter", data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({})
        )
