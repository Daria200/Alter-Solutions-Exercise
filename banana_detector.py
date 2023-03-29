import sys
import logging


def log_bananas():
    """
    Reads an input stream. Logs a minion to the banana.log file
    when word banana is contained in the stream.
    """

    # Configure the file where the minion will be logged
    logging.basicConfig(
        filename="banana.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Log the minion
    for line in sys.stdin:
        if "banana" in line.lower():
            logging.info(
                """
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
            )


if __name__ == "__main__":
    log_bananas()
