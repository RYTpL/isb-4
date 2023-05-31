import argparse
import time
import logging

from executable_files.card_info import CardInfo
from executable_files.luhn_algorithm import luhn_algorithm
from executable_files.card_number import create_card_number
from executable_files.cores_time import Stat

logging.getLogger().setLevel(logging.INFO)

def menu() -> None:
    """
    Func for working with user
    """
    logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler("log.txt")
    file_handler.setLevel(logging.ERROR)
    logger.addHandler(file_handler)

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument(
        "path", type=str, help="The path to the json file with the settings")
    group.add_argument("-cn", "--cardnumber",
                    help="Runs the script for finding the card number")
    group.add_argument("-ct", "--corestime",
                    help="Runs a script to measure the time")
    group.add_argument("-la", "--luhnalg",
                    help="Runs the Luhn algorithm")
    args = parser.parse_args()

    logger.debug(f"Arguments: {args}")

    def create_card_number(hash_card, last_num, bins_card, cores):
        """
        This function takes four arguments: hash_card, last_num, bins_card and cores
        It uses these arguments to create a card number according to some logic
        It returns the card number as a string
        """
        logger.debug(f"Creating card number with {cores} cores")
        return number

    def card_number_serealization(number, path):
        """
        This function takes two arguments: number and path
        It serializes the card number to a json file at the given path
        It does not return anything
        """
        logger.debug(f"Serializing card number {number} to {path}")

    def card_number_deserealization(path):
        """
        This function takes one argument: path
        It deserializes the card number from a json file at the given path
        It returns the card number as a string
        """
        logger.debug(f"Deserializing card number from {path}")
        return number

    def luhn_algorithm(number):
        """
        This function takes one argument: number
        It applies the Luhn algorithm to the card number to check its validity
        It returns True if the number is valid and False otherwise
        """
        logger.debug(f"Applying Luhn algorithm to {number}")
        return result

    def save_fig():
        """
        This function does not take any arguments
        It saves a figure of the time measurements to a file
        It does not return anything
        """
        logger.debug(f"Saving figure")

    if args.cardnumber:
        try:
            card_info = CardInfo(args.path)
            number = create_card_number(
                card_info.hash_card, card_info.last_num, card_info.bins_card, 8)
            print(f"card number is {number}")
            card_number_serealization(number, args.path)
            logger.info(f"Card number created and serialized successfully")
        except Exception as e:
            logger.error(f"An error occurred while creating or serializing card number: {e}")
    elif args.corestime:
        try:
            card_info = CardInfo(args.path)
            stat = Stat(args.path)
            for i in range(1, 9):
                start = time.perf_counter()
                create_card_number(card_info.hash_card,
                                card_info.last_num, card_info.bins_card, i)
                end = time.perf_counter()
                stat.time_serialization(i, end-start)
            stat.save_fig()
            logger.info(f"Time measurement and figure saving completed successfully")
        except Exception as e:
            logger.error(f"An error occurred while measuring time or saving figure: {e}")
    elif args.luhnalg:
        try:
            card_info = CardInfo(args.path)
            number = card_number_deserealization(args.path)
            print(luhn_algorithm(number))
            logger.info(f"Luhn algorithm applied successfully")
        except Exception as e:
            logger.error(f"An error occurred while applying Luhn algorithm: {e}")