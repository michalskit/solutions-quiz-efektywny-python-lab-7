import unittest
from lab7_quiz import SmartLight, AudioSystem, SmartSpeaker, CleaningRobot

class TestSmartLight(unittest.TestCase):
    def test_brightness_setter(self):
        light = SmartLight()
        light.brightness = 50
        self.assertEqual(light.brightness, 50)

    def test_brightness_setter_invalid(self):
        light = SmartLight()
        with self.assertRaises(ValueError):
            light.brightness = 150

class TestAudioSystem(unittest.TestCase):
    def test_audio_system(self):
        audio = AudioSystem("Sony", 100)
        self.assertEqual(audio.get_details(), {"brand": "Sony", "max_volume": 100})

class TestSmartSpeaker(unittest.TestCase):
    def test_smart_speaker(self):
        speaker = SmartSpeaker("Sony", 100, True)
        self.assertEqual(speaker.get_details(), {"brand": "Sony", "max_volume": 100, "voice_command_enabled": True})

class TestCleaningRobot(unittest.TestCase):
    def test_cleaning_robot_attributes(self):
        robot = CleaningRobot("ModelX", 10)
        self.assertEqual(robot.battery_life, 10)

    def test_cleaning_robot_battery_life_validation(self):
        with self.assertRaises(ValueError):
            CleaningRobot("ModelX", "NotAnInteger")

    def test_cleaning_robot_str(self):
        robot = CleaningRobot("ModelX", 10)
        self.assertEqual(str(robot), "CleaningRobot(model=ModelX, battery_life=10)")

if __name__ == '__main__':
    unittest.main()
