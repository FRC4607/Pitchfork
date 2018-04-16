from wpilib.command import Command
from ctre.wpi_talonsrx import WPI_TalonSRX
from constants import BOOM_STATE, LOGGER_LEVEL
import logging
logger = logging.getLogger(__name__)
logger.setLevel(LOGGER_LEVEL)


class BoomJoystick(Command):
    """
    This command will use the driver inputs to drive the robot.
    """
    def __init__(self, robot):
        super().__init__()
        self.requires(robot.boom)
        self.robot = robot

    def execute(self):
        # Get the joystick inputs.  -'ve is up and +'ve is down, joytick up returns -'ve
        boomThrottle = -self.robot.oi.operatorJoystick.getY()

        # Only apply joystick when reading a 5% throttle
        if boomThrottle < 0.05 and boomThrottle > -0.05:
            boomThrottle = 0.0
        else:
            self.robot.boomState = BOOM_STATE.Unknown
            
        self.robot.boom.talon.set(WPI_TalonSRX.ControlMode.PercentOutput, boomThrottle)