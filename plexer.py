import os
import re

startDir = "S:\\MyMedia2\\mkv2\\"

# myre = re.compile(".*\([1,2][9,0]..\)\.(mkv|mp4|MKV|MP4)$")
myre = re.compile(".*\([1,2][9,0]..\).*(mkv|mp4|MKV|MP4)$")
i = 0
if __name__ == "__main__":
    for (root,dirs,allFiles) in os.walk(startDir, topdown=True):
        # print(root)
        # print(dirs)
        movies = [m.group(0) for l in allFiles for m in [myre.search(l)] if m]
        for movie in movies:
            i += 1
            if (len(movies) > 1):
                print(str(i) + 'Movie: ' + movie)

        # print('--------------------------------')