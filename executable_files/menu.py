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
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument(
        "path", type=str, help="The path to the json file with the settings")
    group.add_argument("-cn", "--cardnumber",
                       help="Runs the script for finding the card number")
    group.add_argument("-ct", "--corestime",
                       help="Runs a script to measure the time")
    group.add_argument("-la", "--luhnalg",
                       help="Зruns the Luhn algorithm")
    args = parser.parse_args()
    if args.cardnumber:
        card_info = CardInfo(args.path)
        number = create_card_number(
            card_info.hash_card, card_info.last_num, card_info.bins_card, 8)
        print(f"card number is {number}")
        card_info.card_number_serealization(number, args.path)
    elif args.corestime:
        card_info = CardInfo(args.path)
        stat = Stat(args.path)
        for i in range(1, 9):
            start = time.perf_counter()
            create_card_number(card_info.hash_card,
                               card_info.last_num, card_info.bins_card, i)
            end = time.perf_counter()
            stat.time_serialization(i, end-start)
        stat.save_fig()
    elif args.luhnalg:
        card_info = CardInfo(args.path)
        number = card_info.card_number_deserealization(args.path)
        print(luhn_algorithm(number))