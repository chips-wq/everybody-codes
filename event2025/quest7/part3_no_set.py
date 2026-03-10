import sys
from collections import defaultdict, deque

def try_match(word: str, d: dict[str, list[str]]):
    n = len(word)
    for i in range(n-1):
        # It should always hold that word[i] in d and word[i+1] in d[word[i]]
        if not (word[i] in d and word[i+1] in d[word[i]]): return False
    return True

def bfs(start: str, min_len: int, max_len: int, d: dict[str, list[str]]):
    assert min_len + 4 == max_len

    if max_len < 0:
        return
    
    if min_len <= 0:
        yield ""

    q = deque(start)
    
    while q:
        c_w = q.popleft()
        
        if len(c_w) > max_len:
            continue

        if len(c_w) >= min_len:
            yield c_w

        if c_w[-1] in d:
            for n_letter in d[c_w[-1]]:
                q.append(c_w + n_letter)
    

MIN_LEN = 7
MAX_LEN = 11

"""
Given a list of words, make sure that for any w1, w2
w1 is not a prefix of w2

"""

def restrict_prefix(words: list[str]):
    s = set()
    # O(n^2)
    for word in words:
        c_words = list(s)
        # Otherwise, is a word in s a prefix of this word
            # Then don't do anything
        go_on = False
        for ww in c_words:
            if word.startswith(ww):
                go_on = True
                break
        if go_on: continue
        # First, is this word a prefix of another word in s
            # Then update set with this word
        for ww in c_words:
            if ww.startswith(word):
                s.remove(ww)
                s.add(word)
                go_on = True
                break
        if go_on: continue
        # Otherwise, s.add(word)
        s.add(word)

    return list(s)

if __name__ == '__main__':
    assert len(sys.argv) > 1
    infile = sys.argv[1]
    with open(infile, "r") as f:
        content = f.read()
        words, markings = content.split("\n\n")
        words = words.strip().split(",")

        words = restrict_prefix(words)

        d = defaultdict(list)


        for marking in markings.strip().splitlines():
            fro, to = marking.strip().split(" > ")
            to = to.split(",")
            assert fro not in d
            d[fro] = to

        ans = 0
        for i, word in enumerate(words):
            if not try_match(word, d): continue
            c_len = len(word)

            assert word[-1] in d
            ans += sum(1 for _ in bfs(d[word[-1]], MIN_LEN-c_len, MAX_LEN-c_len, d))

            # print(len(ll))
            # print(ll)
        print(f"{ans=}")
    
