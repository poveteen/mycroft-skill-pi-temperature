# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import time
import os

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
import mycroft.audio


class PiCpuTemperatureSkill(MycroftSkill):

    def __init__(self):
        super(PiCpuTemperatureSkill, self).__init__(name="PiCpuTemperatureSkill")

    def initialize(self):
        pass

    @intent_handler(IntentBuilder("PiCpuTemperatureIntent").require("query").require("cpu").require("temperature"))
    def handle_query(self, message):
        try:
            with open("/sys/class/thermal/thermal_zone0/temp") as sys_file:
                temp_millis = sys_file.readline()
                temp = int(int(temp_millis) / 1000)
                self.speak_dialog("cpu temperature", {'temp': temp})
        except Exception:
            self.speak_dialog("cannot read temperature")


def create_skill():
    return PiCpuTemperatureSkill()
