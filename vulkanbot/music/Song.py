from vulkanbot.music.Interfaces import ISong, IPlaylist


class Song(ISong):
    """Store the usefull information about a Song"""

    def __init__(self, identifier: str, playlist: IPlaylist) -> None:
        """Create a song with only the URL to the youtube song"""
        self.__identifier = identifier
        self.__info = {}
        self.__problematic = False
        self.__playlist: IPlaylist = playlist

    def finish_down(self, info: dict) -> None:
        """Get and store the full information of the song"""
        self.__usefull_keys = ['url', 'duration',
                               'title', 'webpage_url',
                               'channel', 'id', 'uploader',
                               'thumbnail', 'original_url']

        for key in self.__usefull_keys:
            try:
                self.__info[key] = info[key]
            except Exception as e:
                print(e)
                raise e

    @property
    def source(self) -> str:
        """Return the Song Source URL to play"""
        if 'url' in self.__info.keys():
            return self.__info['url']
        else:
            return None

    @property
    def title(self) -> str:
        """Return the Song Title"""
        if 'title' in self.__info.keys():
            return self.__info['title']
        else:
            return None

    @property
    def duration(self) -> str:
        """Return the Song Title"""
        if 'duration' in self.__info.keys():
            return self.__info['duration']
        else:
            return 0.0

    @property
    def identifier(self) -> str:
        return self.__identifier

    @property
    def problematic(self) -> bool:
        return self.__problematic

    def destroy(self) -> None:
        """Mark this song with problems and removed from the playlist due to any type of error"""
        self.__problematic = True
        self.__playlist.destroy_song(self)

    @property
    def info(self):
        return self.__info
