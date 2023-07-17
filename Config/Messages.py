from Config.Singleton import Singleton
from Config.Configs import VConfigs
from Config.Emojis import VEmojis


class Messages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.__emojis = VEmojis()
            configs = VConfigs()
            self.STARTUP_MESSAGE = '正在開啟 Vulkan...'
            self.STARTUP_COMPLETE_MESSAGE = 'Vulkan 已經上線!'

            self.SONGINFO_UPLOADER = "上傳者: "
            self.SONGINFO_DURATION = "歌曲時長: "
            self.SONGINFO_REQUESTER = '指令使用者: '
            self.SONGINFO_POSITION = '在列表位置: '

            self.VOLUME_CHANGED = '聲音大小已切換至 `{}`%'
            self.SONGS_ADDED = '正在下載 `{}` 個歌至列表中'
            self.SONG_ADDED = '正在下載 `{}` 至列表中'
            self.SONG_ADDED_TWO = f'{self.__emojis.MUSIC} 歌曲已添加至列表!'
            self.SONG_PLAYING = f'{self.__emojis.MUSIC} 歌曲正在播放'
            self.SONG_PLAYER = f'{self.__emojis.MUSIC} 播放器狀態:'
            self.QUEUE_TITLE = f'{self.__emojis.MUSIC} 歌曲列表'
            self.ONE_SONG_LOOPING = f'{self.__emojis.MUSIC} 正在單曲循環'
            self.ALL_SONGS_LOOPING = f'{self.__emojis.MUSIC} 正在列表循環'
            self.SONG_PAUSED = f'{self.__emojis.PAUSE} 已暫停'
            self.SONG_RESUMED = f'{self.__emojis.PLAY} 繼續播放'
            self.SONG_SKIPPED = f'{self.__emojis.SKIP} 已跳過'
            self.RETURNING_SONG = f'{self.__emojis.BACK} Playing previous song'
            self.STOPPING = f'{self.__emojis.STOP} 已停止'
            self.EMPTY_QUEUE = f'{self.__emojis.QUEUE} 歌曲列表是空的, 使用 {configs.BOT_PREFIX}play 來添加更多歌曲'
            self.SONG_DOWNLOADING = f'{self.__emojis.DOWNLOADING} 正在下載...'
            self.PLAYLIST_CLEAR = f'{self.__emojis.MUSIC} 已清空播放列表'

            self.HISTORY_TITLE = f'{self.__emojis.MUSIC} 歷史紀錄'
            self.HISTORY_EMPTY = f'{self.__emojis.QUEUE} 目前尚無歌曲在歷史紀錄中'

            self.SONG_MOVED_SUCCESSFULLY = '`{}` 成功從 `第{}首` 移動至了 `第{}首`'
            self.SONG_REMOVED_SUCCESSFULLY = '`{}` 已被從列表中移除'

            self.LOOP_ALL_ON = f'{self.__emojis.ERROR} Vulkan is looping all songs, use {configs.BOT_PREFIX}loop off to disable this loop first'
            self.LOOP_ONE_ON = f'{self.__emojis.ERROR} Vulkan is looping one song, use {configs.BOT_PREFIX}loop off to disable this loop first'
            self.LOOP_ALL_ALREADY_ON = f'{self.__emojis.LOOP_ALL} Vulkan 已經正在循環列表歌曲了'
            self.LOOP_ONE_ALREADY_ON = f'{self.__emojis.LOOP_ONE} Vulkan 已經正在循環當前歌曲了'
            self.LOOP_ALL_ACTIVATE = f'{self.__emojis.LOOP_ALL} 正在循環列表歌曲'
            self.LOOP_ONE_ACTIVATE = f'{self.__emojis.LOOP_ONE} 正在循環當前歌曲'
            self.LOOP_DISABLE = f'{self.__emojis.LOOP_OFF} 已停止循環'
            self.LOOP_ALREADY_DISABLE = f'{self.__emojis.ERROR} 循環已經停止了'
            self.LOOP_ON = f'{self.__emojis.ERROR} This command cannot be invoked with any loop activated. Use {configs.BOT_PREFIX}loop off to disable loop'
            self.BAD_USE_OF_LOOP = f"""{self.__emojis.ERROR} Invalid arguments of Loop command. Use {configs.BOT_PREFIX}help loop to more information.
                                -> Available Arguments: ["all", "off", "one", ""]"""

            self.SONGS_SHUFFLED = f'{self.__emojis.SHUFFLE} Songs shuffled successfully'
            self.ERROR_SHUFFLING = f'{self.__emojis.ERROR} Error while shuffling the songs'
            self.ERROR_MOVING = f'{self.__emojis.ERROR} Error while moving the songs'
            self.LENGTH_ERROR = f'{self.__emojis.ERROR} Numbers must be between 1 and queue length, use -1 for the last song'
            self.ERROR_NUMBER = f'{self.__emojis.ERROR} This command require a number'
            self.ERROR_VOLUME_NUMBER = f'{self.__emojis.ERROR} This command require a number between 0 and 100'
            self.ERROR_PLAYING = f'{self.__emojis.ERROR} Error while playing songs'
            self.COMMAND_NOT_FOUND = f'{self.__emojis.ERROR} Command not found, type {configs.BOT_PREFIX}help to see all commands'
            self.UNKNOWN_ERROR = f'{self.__emojis.ERROR} Unknown Error, if needed, use {configs.BOT_PREFIX}reset to reset the player of your server'
            self.ERROR_MISSING_ARGUMENTS = f'{self.__emojis.ERROR} Missing arguments in this command. Type {configs.BOT_PREFIX}help "command" to see more info about this command'
            self.NOT_PREVIOUS = f'{self.__emojis.ERROR} 沒有上一首歌曲了'
            self.PLAYER_NOT_PLAYING = f'{self.__emojis.ERROR} No song playing. Use {configs.BOT_PREFIX}play to start the player'
            self.IMPOSSIBLE_MOVE = '執行無效 :('
            self.ERROR_TITLE = '錯誤 :-('
            self.COMMAND_NOT_FOUND_TITLE = 'This is strange :-('
            self.NO_CHANNEL = '播放音樂前請先進入一個語音頻道當中.'
            self.NO_GUILD = f'This server does not has a Player, try {configs.BOT_PREFIX}reset'
            self.INVALID_INPUT = f'This URL was too strange, try something better or type {configs.BOT_PREFIX}help play'
            self.INVALID_INDEX = f'Invalid index passed as argument.'
            self.INVALID_ARGUMENTS = f'Invalid arguments passed to command.'
            self.DOWNLOADING_ERROR = f"{self.__emojis.ERROR} It's impossible to download and play this video"
            self.EXTRACTING_ERROR = f'{self.__emojis.ERROR} An error ocurred while searching for the songs'

            self.ERROR_IN_PROCESS = f"{self.__emojis.ERROR} Due to a internal error your player was restarted, skipping the song."
            self.MY_ERROR_BAD_COMMAND = 'This string serves to verify if some error was raised by myself on purpose'
            self.BAD_COMMAND_TITLE = 'Misuse of command'
            self.BAD_COMMAND = f'{self.__emojis.ERROR} Bad usage of this command, type {configs.BOT_PREFIX}help "command" to understand the command better'
            self.VIDEO_UNAVAILABLE = f'{self.__emojis.ERROR} Sorry. This video is unavailable for download.'
            self.ERROR_DUE_LOOP_ONE_ON = f'{self.__emojis.ERROR} This command cannot be executed with loop one activated. Use {configs.BOT_PREFIX}loop off to disable loop.'


class SearchMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            config = VConfigs()
            self.UNKNOWN_INPUT = f'This type of input was too strange, try something else or type {config.BOT_PREFIX}help play'
            self.UNKNOWN_INPUT_TITLE = 'Nothing Found'
            self.GENERIC_TITLE = 'URL could not be processed'
            self.SPOTIFY_NOT_FOUND = 'Spotify could not process any songs with this input, verify your link or try again later.'
            self.YOUTUBE_NOT_FOUND = 'Youtube could not process any songs with this input, verify your link or try again later.'
            self.DEEZER_NOT_FOUND = 'Deezer could not process any songs with this input, verify your link or try again later.'


class SpotifyMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.INVALID_SPOTIFY_URL = '無效的 Spotify 連結, 請檢查.'
            self.GENERIC_TITLE = '連結無法正常使用'


class DeezerMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.INVALID_DEEZER_URL = '無效的 Deezer 連結, 請檢查.'
            self.GENERIC_TITLE = '連結無法正常使用'
