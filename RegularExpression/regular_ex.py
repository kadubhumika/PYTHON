import re
text = "The quick brown fox jumps over the lazy dog"
matches = re.search("jumps", text)
if matches:
    print("Yeah ! Found")
    print(matches.group())
    print("Start index: ", matches.start())
    print("End index: ", matches.end())

    matches = re.findall("the", text, re.IGNORECASE)
    print(matches)

    new_text = re.sub("dog", "cat", text)
    print(new_text)