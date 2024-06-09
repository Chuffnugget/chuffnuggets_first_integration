"""Sensor platform for Chuffnuggets First Integration."""
import asyncio
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, config_entry, async_add_entities):
    """Set up the nugget_counter sensor."""
    coordinator = NuggetCounterCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()

    async_add_entities([NuggetCounterSensor(coordinator)], True)

class NuggetCounterCoordinator(DataUpdateCoordinator):
    """Manages fetching data from the nugget_counter."""

    def __init__(self, hass: HomeAssistant):
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name="Nugget Counter",
            update_interval=1.0,
        )
        self._count = 0

    async def _async_update_data(self):
        """Update data."""
        self._count = (self._count + 1) % 11
        return self._count

class NuggetCounterSensor(SensorEntity):
    """Representation of a Nugget Counter sensor."""

    def __init__(self, coordinator: NuggetCounterCoordinator):
        """Initialize the sensor."""
        self.coordinator = coordinator
        self._attr_name = "Nugget Counter"
        self._attr_unique_id = "nugget_counter_sensor"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data

    async def async_update(self):
        """Update the sensor."""
        await self.coordinator.async_request_refresh()
