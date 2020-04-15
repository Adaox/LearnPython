class Song(object):
    def __init__(self, lyrics, artist="Unknown"):
        self.lyrics = lyrics
        self.artist = artist

    def announce(self):
        print(f"Please enjoy the following song by {self.artist}")

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


truth_hurts_lyrics = [
    "Why men great 'til they gotta be great?",
    "Woo",
    "I just took a DNA test, turns out I'm 100% that bitch",
    "Even when I'm crying crazy",
    "Yeah, I got boy problems, that's the human in me",
    "Bling bling, then I solve 'em, that's the goddess in me",
    "You coulda had a bad bitch, non-committal",
    "Help you with your career just a little",
    "You're 'posed to hold me down, but you're holding me back",
    "And that's the sound of me not calling you back",
]

happy_bday = Song(
    ["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"]
)

bulls_on_parade = Song(["They rally around tha family", "With pockets full of shells"])


truth_hurts = Song(truth_hurts_lyrics, "Lizzo")

happy_bday.announce()
happy_bday.sing_me_a_song()

# bulls_on_parade.announce()
# bulls_on_parade.sing_me_a_song()

truth_hurts.announce()
truth_hurts.sing_me_a_song()
