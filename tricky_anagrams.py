from collections import defaultdict

paragraph = """The rat sat in a tar pit today. I gave him a tip then. I wished on a star for no rats tonight."""

pretty_words = [single_word.lower() for single_word in set(paragraph.split())]

testdir = defaultdict(list)
word_comparison = defaultdict(list)

for word in pretty_words:
    testdir[word].append("".join(sorted(word)))

for word in pretty_words:
    word_comparison["".join(sorted(word))]

for key, value in testdir.items():
    if (len(key)) > 1:
        for other_key in word_comparison.keys():
            if (len(other_key)) > 1:
                if value[0] == other_key:
#                 if value[0] in other_key:
                    word_comparison[other_key].append(key)

for key, value in word_comparison.items():
    if len(value) > 1:
        print(value)



