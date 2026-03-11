import sys
from collections import defaultdict

def try_match(word: str, d: dict[str, list[str]]):
    n = len(word)
    for i in range(n-1):
        # It should always hold that word[i] in d and word[i+1] in d[word[i]]
        if not (word[i] in d and word[i+1] in d[word[i]]): return False
    return True

if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    with open(infile, "r") as f:
        content = f.read()
        words, markings = content.split("\n\n")
        words = words.strip().split(",")

        d = defaultdict(list)


        for marking in markings.strip().splitlines():
            fro, to = marking.strip().split(" > ")
            to = to.split(",")
            assert fro not in d
            d[fro] = to

        for i, word in enumerate(words):
            print(f"{word=}, {try_match(word, d)=}")
    
