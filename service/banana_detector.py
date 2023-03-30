import logging
import sys

minion = """
      ________\|/________
     /      ________     \\
    |     |   __   |      |
    |=====|  |__|  |======|
    |     |________|      |
    |       ______        |
    |       \____/        |
    |_____________________|
    |\      _____        /|
    |/      | G |        \|
    |       |___|         |
    |                     |  
    |_____________________|
            |   |           
          __|   |__
    """


def log_bananas():
    """
    Reads an input stream. Logs a minion to the banana.log file
    when word banana is contained in the stream.
    """

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("banana.log", "a")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Log the minion
    for line in sys.stdin:
        if "banana" in line.lower():
            logger.info(minion)


if __name__ == "__main__":
    log_bananas()
