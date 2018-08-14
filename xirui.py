from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def setup_platform(hass, config, add_devices, discovery_info=None):
	"""Setup the sensor platform."""
	add_devices([Temperature_Sensor(), Humidity_Sensor(), PM25_Sensor(), hcho_Sensor(), Charging_Sensor(), Bat_Sensor()])

def loaddata():
	headers = {'Content-Type': 'application/json;charset=UTF-8',
			   'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A5345f',
			'accept-language':'zh-cn'
			  }
	data = {
		"serialNo" : "id_here"
	}
	data = json.dumps(data)
	re = requests.post("https://server.developmentservice.cn//device/realTimeData", data = data, headers = headers, verify=False)
	return json.loads(re.text)

def get_temp():
	data = loaddata()
	return int(float('%.f' % float(data['body']['RT']['temp'] / 10)))

def get_humi():
	data = loaddata()
	return int(float('%.f' % float(data['body']['RT']['humi'] / 10)))

def get_PM25():
	data = loaddata()
	return data['body']['cube']['RT']['pm2_5']
	
def get_charging():
	data = loaddata()
	return "已连接电源" if data['body']['cube']['RT']['isCharging'] == 1 else "未充电"
	
def get_bat():
	data = loaddata()
	return int(data['body']['cube']['RT']['Bat'] * 20)
	
def get_hcho():
	data = loaddata()
	return float('%.2f' % float(data['body']['cube']['RT']['hcho'] / 1000))

class Temperature_Sensor(Entity):
	"""Representation of a Sensor."""

	def __init__(self):
		"""Initialize the sensor."""
		self._state = None

	@property
	def name(self):
		"""Return the name of the sensor."""
		return 'Temperature'

	@property
	def state(self):
		"""Return the state of the sensor."""
		return self._state

	@property
	def unit_of_measurement(self):
		"""Return the unit of measurement."""
		return TEMP_CELSIUS

	def update(self):
		"""Fetch new state data for the sensor.

		This is the only method that should fetch new data for Home Assistant.
		"""
		self._state = get_temp()
		
class Humidity_Sensor(Entity):
	"""Representation of a Sensor."""

	def __init__(self):
		"""Initialize the sensor."""
		self._state = None

	@property
	def name(self):
		"""Return the name of the sensor."""
		return 'Humidity'

	@property
	def state(self):
		"""Return the state of the sensor."""
		return self._state

	@property
	def unit_of_measurement(self):
		"""Return the unit of measurement."""
		return "%"

	def update(self):
		"""Fetch new state data for the sensor.

		This is the only method that should fetch new data for Home Assistant.
		"""
		self._state = get_humi()
		
class hcho_Sensor(Entity):
	"""Representation of a Sensor."""

	def __init__(self):
		"""Initialize the sensor."""
		self._state = None

	@property
	def name(self):
		"""Return the name of the sensor."""
		return 'hcho'

	@property
	def state(self):
		"""Return the state of the sensor."""
		return self._state

	@property
	def unit_of_measurement(self):
		"""Return the unit of measurement."""
		return "mg/m³"

	def update(self):
		"""Fetch new state data for the sensor.

		This is the only method that should fetch new data for Home Assistant.
		"""
		self._state = get_hcho()
		
class PM25_Sensor(Entity):
	"""Representation of a Sensor."""

	def __init__(self):
		"""Initialize the sensor."""
		self._state = None

	@property
	def name(self):
		"""Return the name of the sensor."""
		return 'PM2.5'

	@property
	def state(self):
		"""Return the state of the sensor."""
		return self._state

	@property
	def unit_of_measurement(self):
		"""Return the unit of measurement."""
		return "μg/m³"

	def update(self):
		"""Fetch new state data for the sensor.

		This is the only method that should fetch new data for Home Assistant.
		"""
		self._state = get_PM25()

class PM25_Sensor(Entity):
	"""Representation of a Sensor."""

	def __init__(self):
		"""Initialize the sensor."""
		self._state = None

	@property
	def name(self):
		"""Return the name of the sensor."""
		return 'PM2.5'

	@property
	def state(self):
		"""Return the state of the sensor."""
		return self._state

	@property
	def unit_of_measurement(self):
		"""Return the unit of measurement."""
		return "μg/m³"

	def update(self):
		"""Fetch new state data for the sensor.

		This is the only method that should fetch new data for Home Assistant.
		"""
		self._state = get_PM25()
		
class Charging_Sensor(Entity):
	"""Representation of a Sensor."""

	def __init__(self):
		"""Initialize the sensor."""
		self._state = None

	@property
	def name(self):
		"""Return the name of the sensor."""
		return 'Charging'

	@property
	def state(self):
		"""Return the state of the sensor."""
		return self._state

	@property
	def unit_of_measurement(self):
		"""Return the unit of measurement."""
		return ""

	def update(self):
		"""Fetch new state data for the sensor.

		This is the only method that should fetch new data for Home Assistant.
		"""
		self._state = get_charging()
		
class Bat_Sensor(Entity):
	"""Representation of a Sensor."""

	def __init__(self):
		"""Initialize the sensor."""
		self._state = None

	@property
	def name(self):
		"""Return the name of the sensor."""
		return 'Battery'

	@property
	def state(self):
		"""Return the state of the sensor."""
		return self._state

	@property
	def unit_of_measurement(self):
		"""Return the unit of measurement."""
		return "%"

	def update(self):
		"""Fetch new state data for the sensor.

		This is the only method that should fetch new data for Home Assistant.
		"""
		self._state = get_bat()