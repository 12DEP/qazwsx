#    hass-hikvision-connector
#    Copyright (C) 2020 Dmitry Berezovsky
#    The MIT License (MIT)
#    
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#    
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#    
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import enum

DOMAIN = 'hikvision_isapi'
PLATFORMS = ('binary_sensor',)

DATA_API_CLIENT = 'api_client'
UNDO_UPDATE_CONF_UPDATE_LISTENER = 'undo_config_update_listener'

#####
DATA_EVENT_STREAM = 'event_stream'
DATA_ALERTS_BG_TASKS = 'alerts_bg_tasks'
DATA_ALERTS_QUEUE = 'alerts_queue'
DATA_ENTITIES = 'entities'
#####
DATA_HAS_SUBSCRIBERS = 'has_subscribers'
DATA_ALERT_CONFIGS = 'alert_configs'
DATA_BG_TASKS = 'bg_tasks'

CONF_BASE_URL = 'base_url'
CONF_USER = 'username'
CONF_PASSWORD = 'password'
CONF_IGNORE_SSL_ERRORS = 'ignore_ssl_errors'
CONF_DEVICE_TYPE = 'device_type'

DEVICE_TYPE_NVR = 'NVR'

EDIT_COMMON_SETTINGS = 'common'
EDIT_INPUT_PREFIX = 'input_settings'

OPT_EDIT_KEY = 'edit_key'
OPT_ROOT_COMMON = 'common'
OPT_ROOT_ALERTS = 'alerts'

OPT_COMMON_DEFAULT_RECOVERY_PERIOD = 'default_recovery_period'
OPT_COMMON_ALERT_INPUTS = 'alert_inputs'

OPT_ALERTS_ALERT_TYPES = 'alert_types'
OPT_ALERTS_ENABLE_TRACKING = 'enable_tracking'


DEFAULTS_COMMON_DEFAULT_RECOVERY_PERIOD = '00:01:00'

NON_NVR_CHANNEL_NUMBER = '1'


class AlertType(enum.Enum):
    LineCrossing = 'linedetection'
    Intrusion = 'fielddetection'
    VideoLoss = 'videoloss'


ALERT_STATE_ACTIVE = 'active'
ALERT_STATE_INACTIVE = 'inactive'

ALERT_TYPES_MAP = {
    'videoloss': 'Video Loss',
    'fielddetection': 'Intrusion',
    'linedetection': 'Cross Line',
}

CONTEXT_ALERT_CONFIG_KEY = 'selected_alert_chanel'

SENSOR_ID_PREFIX = 'cam'

SIGNAL_ALERT_NAME = DOMAIN + '_alert'

EVENT_ALERT_NAME = DOMAIN + '_alert'
EVENT_ALERT_DATA_CHANNEL = 'channel'
EVENT_ALERT_DATA_TYPE = 'alert_type'
EVENT_ALERT_DATA_DEVICE = 'device'
EVENT_ALERT_DATA_TIMESTAMP = 'timestamp'

ATTR_LAST_TRIGGERED_TIME = 'last_triggered'
