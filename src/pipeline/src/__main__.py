import logging
from .modules.pipeline_builder import PipelineEngine
from .pipes.entry_stage import EntryPipe


logging.basicConfig(
    level=logging.INFO,
    filename="./logs.txt",
)

def main():
    # Start the game loop
    #must define output video_name and video location

    engine = PipelineEngine()

    #TODO change the payload to match

    #TODO remove redunant pipes that we dont need in this program. dl, upload,

    #TODO add file drop into tui app

    #TODO design new tui app and figure the changes we need in a document

    """
        given a video file -> trigger pipeline  to find the best spots
            changes we need to mak

    """

    payload5 = {
        "stream_id" : 2209761727,
        "is_community" : False,
        "video_name" : "dyrus",
    }

    logging.info("Starting Program")
    engine.q.put(payload5)
    engine.run(EntryPipe(engine=engine))


if __name__ == "__main__":
    main() #./TwitchDownloaderCLI videodownload --id 612942303 -b 0:01:40 -e 0:03:20 -o video.mp4
