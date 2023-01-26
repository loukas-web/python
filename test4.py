import string
import random

str_list: str = string.ascii_letters + string.digits + string.punctuation
count: int = 0


def random_string(letters: str) -> str:
    return "".join(random.choices(letters, k=random.randint(7, 100)))


while True:
    count += 1
    if "pokemon" in random_string(str_list) or count >= 10_000_000:
        print(count)
        break
