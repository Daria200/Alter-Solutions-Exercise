import sys
import logging


def log_bananas():
    logging.basicConfig(
        filename="banana.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

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
