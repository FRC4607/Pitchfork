import os
import pickle
from wpilib.command import CommandGroup
from utilities.drivetrain_path_follower import DrivetrainPathFollower


class AutonForward(CommandGroup):

    def __init__(self, robot):
        super().__init__()
        self.requires(robot.driveTrain)

        # Read up the pickled path file of trajectories
        with open(os.path.join(os.path.dirname(__file__),
                               'forward.pickle'), "rb") as fp:
            path = pickle.load(fp)

        # Add commands to run
        self.addSequential(DrivetrainPathFollower(robot, path, False))
