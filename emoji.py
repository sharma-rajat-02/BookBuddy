#Change emoticons to emoji
def main():
     emoji=input("")
     emoji=convert(emoji)
     print(emoji)
def convert(emoji):
    emoji=emoji.replace(":)","🙂")
    emoji=emoji.replace(":(","🙁")
    return emoji
main()