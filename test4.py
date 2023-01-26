import string
import random

str_list: str = "" + string.ascii_letters + string.digits + string.punctuation
count: int = 0


def random_string() -> str:
    return "".join(random.choices(str_list, k=random.randint(7, 100)))


while True:
    count += 1
    if "pokemon" in random_string() or count >= 10_000_000:
        print(count)
        break
