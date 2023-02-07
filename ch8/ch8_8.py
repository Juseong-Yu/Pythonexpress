class printSong:
    def __init__(self,l):
        self.lyrics = l
    
    def sing(self):
        for line in range(len(self.lyrics)):
            print(self.lyrics[line])

aSong = printSong(['Twinkle,twinkle,little star',
'How I wonder what you are!',
'Up above the world so high,',
'Like a diamond in the sky'])
aSong.sing()