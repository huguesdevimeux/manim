import numpy as np
import subprocess
from pathlib import Path
import os


from ... import file_writer_config, logger, console
from ...constants import FFMPEG_BIN


class LiveStreamer(object):
    def __init__(self, scene, *args, **kwargs):
        self.scene = scene
        self.partial_movie_directory = Path(
            r"/home/hugues/Desktop/Programmation/PYTHON/MANIM-DEV/test_stream/"
        )
        self.use_cached = False
        pass
        # Init config from config file

    # NOTE : this should live in an abstract class for filewriter ?
    def is_already_cached(self, hash_animation):
        path = os.path.join(
            self.partial_movie_directory,
            "{}{}".format(hash_animation, ".mp4"),  # TODO change this to the extension
        )
        return os.path.exists(path)

    def _send_video_to_stream(self, path_to_video):
        command = [
            FFMPEG_BIN,
            "-stream_loop",  # NOTE : this is done to stop at the last frame.
            "0",
            "-i",
            str(path_to_video),
            "-loglevel",
            file_writer_config["ffmpeg_loglevel"],
            "-f",  # output to stream
            "mpegts",
            "udp://224.2.2.2:8888",
        ]
        self.streaming_process = subprocess.Popen(command, stdin=subprocess.PIPE)

    def begin_animation(self, allow_write=True, *args):
        """Used internally by manim to stream the animation to FFMPEG, which will output in the stream."""
        output_video_path = (
            self.partial_movie_directory
            / f"{self.scene.play_hashes_list[-1]}.mp4"  # TODO : replace with the config value for partial movie file dir, for stream.
        )  # TODO change this to the extension specified in config
        if (
            not allow_write
        ):  # NOTE there might be conflict, when one wants to skip an animation but then self interprets it as a willing to use cached data. TODO
            self.use_cached = True
            self._send_video_to_stream(output_video_path)
            return
        width = 1920
        height = 1080
        fps = 60
        command = [
            FFMPEG_BIN,
            "-stream_loop",  # NOTE : this is done to stop at the last frame.
            "0",
            "-y",  # overwrite output file if it exists
            "-f",
            "rawvideo",
            "-s",
            "%dx%d" % (width, height),  # size of one frame
            "-pix_fmt",
            "rgba",
            "-r",
            str(fps),  # frames per second
            "-i",
            "-",  # The imput comes from a pipe
            "-an",  # Tells FFMPEG not to expect any audio
            "-loglevel",
            file_writer_config["ffmpeg_loglevel"],
            "-f",  # output to stream
            "mpegts",
            "udp://224.2.2.2:8888",
        ]
        print(allow_write)
        if allow_write:
            command.append(str(output_video_path))
        print(self.scene.play_hashes_list)
        self.streaming_process = subprocess.Popen(command, stdin=subprocess.PIPE)
        pass

    def end_animation(self, *args):
        """Internally used by Manim to stop streaming to
        FFMPEG gracefully.
        """
        # Wreidly, this has to be commented out, otherwise it does not fo to live
        # TODO : investigate on this, more particularly in the PR intender to fix livesyteamingj

        self.streaming_process.stdin.close()
        self.streaming_process.wait()
        print("STREAMED")

    def write_frame(self, frame):
        """Used internally by Manim to write a frame to
        the FFMPEG input buffer.

        Parameters
        ----------
        frame : np.array
            Pixel array of the frame.
        """
        self.streaming_process.stdin.write(frame.tostring())

    def finish(self):
        pass

    # Stream commands :
    def go_back(self, n_animations=1):
        video_to_play = (
            self.partial_movie_directory / self.scene.play_hashes_list[-n_animations]
            + ".mp4"  # TODO change this to the extension
        )
        self._send_video_to_stream(video_to_play)
        print("WENT BACK FROM ")

    def go_further(self, n_animations):
        pass
