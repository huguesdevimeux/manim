import code
import random

from manim import Container

from ...scene.scene import Scene
from ...scene.three_d_scene import ThreeDScene
from ... import camera_config, file_writer_config, logger
from ...animation.animation import Animation
from ...animation.transform import MoveToTarget, ApplyMethod
from ...camera.camera import Camera
from ...constants import *
from ...container import Container
from ...mobject.mobject import Mobject
from ...scene.scene_file_writer import SceneFileWriter
from ...utils.iterables import list_update
from ...utils.hashing import get_hash_from_play_call, get_hash_from_wait_call


class LiveStreamingScene(ThreeDScene):
    """Class used in livestreaming mode. This is a subclass of Scene, used to fit specical needs of livestreaming.

    Id est :
    - LiveStreamingScene must be able to render an animation without construct() method implemented by the user
    - LiveStreamingScene must not generate any final movie file, nor combining partial one. (Although it uses partial movie files for caching purpose)
    - This class also contains streamings commands.
    """

    # TODO : Stop __injt__ adter? or before cosntruct(

    def __init__(self, *args, **kwargs):
        Scene.__init__(self, *args, **kwargs)
        pass
        # digest config ?
        # Container.__init__(self, **kwargs)
        # self.camera = self.camera_class(**camera_config)
        # self.file_writer = SceneFileWriter(
        #     self,
        #     **file_writer_config,
        # )
        # self.play_hashes_list = []
        # self.mobjects = []
        # self.original_skipping_status = file_writer_config["skip_animations"]
        # # TODO, remove need for foreground mobjects
        # self.foreground_mobjects = []
        # self.num_plays = 0
        # self.time = 0
        # self.original_skipping_status = file_writer_config["skip_animations"]
        # if self.random_seed is not None:
        #     random.seed(self.random_seed)
        #     np.random.seed(self.random_seed)
        # self.setup()

    def __repr__(self):
        return "LiveStreaming tools for manim.\n To read the full documentation of this tool, do manim.help()"

    def go_back(self):
        print("TU VEUX RETOURNER EN ARRIERE FPD")

    # What to do : nothing will really change concering the partial movie file generation. It will still be generated, and then pass in the stream. the main
    # advantage to do that is to be able to use scene caching (and tex(t) ? ) functionnalities of Manim.
    # I think there should be a flag to determine wether to used caching. If no, I think we should use pass a stream direcrlt to the partial movie file generation.
    # So, there will basically be two implementations. Is it good ? no fucking idea
    # Add a __dell__ method to close the stream (/!\)


def start_streaming():
    # NOTE : this import is used to enable keyboard shortcuts in the interactive shell,
    # Such as up arrow, ctrl+c, etc..
    # Only importing it is enough.
    import readline

    print("LIVESTREAMING TIME")
    manim = LiveStreamingScene()
    shell = code.InteractiveConsole(locals={"manim": manim})
    shell.push("from manim import *")
    shell.interact(banner="Manim is now running in live streaming mode.")
