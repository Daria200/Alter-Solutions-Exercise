import sys
import logging

logging.basicConfig(
    filename="banana.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

for line in sys.stdin:
    if "banana" in line:
        logging.info(
            """
 ________\|/_________\n
/      ________     \\\n
|     |   __   |      |\n
|=====|  |__|  |======|\n
|     |________|      |\n
|       ______        |\n
|       \____/        |\n
|_____________________|\n
|\      _____        /|\n
|/      | G |        \|\n
|       |___|         |\n
|                     |\n  
|_____________________|\n
        |   |           \n
      __|   |__
   """
        )
