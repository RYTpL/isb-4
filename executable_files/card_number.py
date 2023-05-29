import hashlib
import multiprocessing as mp
import typing
import logging

from tqdm import tqdm

logging.getLogger().setLevel(logging.INFO)

def compare_hash_with_number(number:str, hash:str, bin:str, last_numbers:str)->typing.Optional[str]:
    """
    Func that converts a number to a hash and compares it with a given hash 
    """
    curNumber = "".join([bin,number,last_numbers])
    if hashlib.blake2s(curNumber.encode()).hexdigest() == hash:
        return curNumber
    return None

def create_card_number(hash:str, last_numbers:str, bins:tuple, cores:int)->typing.Optional[str]:
    """
    Func that generate uniq numbers for card number
    """
    values = []
    n = 1
    for bin in bins:
        for i in range(1000000):
            values.append((str(i).zfill(6), hash, str(bin), last_numbers))
        with mp.Pool(processes=cores) as p:
            for i in p.starmap(compare_hash_with_number, tqdm(values, desc="processing ...", ncols=100)):
                if i is not None:
                    p.terminate()
                    logging.info("Card number is founded")
                    return i
    return None