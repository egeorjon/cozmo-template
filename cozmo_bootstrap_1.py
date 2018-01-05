#!/usr/bin/env python3

# Copyright (c) 2017 Emmanuel Georjon.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Template Python code for programming Cozmo through the SDK.


'''


import asyncio
import cozmo

try:
    from PIL import Image
except ImportError:
    sys.exit('Cannot import from PIL.')

async def cozmo_program(robot: cozmo.robot.Robot):
    color_finder = ColorFinder(robot)
    await color_finder.run()

# Constant declaration
CONSTANT_WITH_CAPS = "values"
	

Class MyClass():
    '''Class template.

    Description of the class template

    Args:
        robot (cozmo.robot.Robot): instance of the robot connected from run_program.
    '''
	
	
	def __init__(self, robot: cozmo.robot.Robot):
        self.robot = robot
        self.robot.camera.image_stream_enabled = True
        self.robot.camera.color_image_enabled = True

		# End of __init__

    async def run(self):
        '''Program runs until typing CRTL+C into Terminal/Command Prompt, 
        or by closing the viewer window.
        '''    
        print("code")

	#End of class MyClass
	
	
async def cozmo_program(robot: cozmo.robot.Robot):
    my_class = MyClass(robot)
    await my_class.run()


if __name__ == '__main__':

	# RC can drive off charger if required
	cozmo.robot.Robot.drive_off_charger_on_connect = True

	# Start
	cozmo.run_program(cozmo_program)