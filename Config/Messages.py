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
            self.RETURNING_SONG = f'{self.__emojis.BACK} 正在播放上一首歌曲'
            self.STOPPING = f'{self.__emojis.STOP} 已停止'
            self.EMPTY_QUEUE = f'{self.__emojis.QUEUE} 歌曲列表是空的, 使用 {configs.BOT_PREFIX}play 來添加更多歌曲'
            self.SONG_DOWNLOADING = f'{self.__emojis.DOWNLOADING} 正在下載...'
            self.PLAYLIST_CLEAR = f'{self.__emojis.MUSIC} 已清空播放列表'

            self.HISTORY_TITLE = f'{self.__emojis.MUSIC} 歷史紀錄'
            self.HISTORY_EMPTY = f'{self.__emojis.QUEUE} 目前尚無歌曲在歷史紀錄中'

            self.SONG_MOVED_SUCCESSFULLY = '`{}` 成功從 `第{}首` 移動至了 `第{}首`'
            self.SONG_REMOVED_SUCCESSFULLY = '`{}` 已被從列表中移除'

            self.LOOP_ALL_ON = f'{self.__emojis.ERROR} Vulkan 正在循環列表歌曲, 請使用 {configs.BOT_PREFIX}loop off 來停止循環'
            self.LOOP_ONE_ON = f'{self.__emojis.ERROR} Vulkan 正在循環目前歌曲, 請使用 {configs.BOT_PREFIX}loop off 來停止循環'
            self.LOOP_ALL_ALREADY_ON = f'{self.__emojis.LOOP_ALL} Vulkan 已經正在循環列表歌曲了'
            self.LOOP_ONE_ALREADY_ON = f'{self.__emojis.LOOP_ONE} Vulkan 已經正在循環當前歌曲了'
            self.LOOP_ALL_ACTIVATE = f'{self.__emojis.LOOP_ALL} 正在循環列表歌曲'
            self.LOOP_ONE_ACTIVATE = f'{self.__emojis.LOOP_ONE} 正在循環當前歌曲'
            self.LOOP_DISABLE = f'{self.__emojis.LOOP_OFF} 已停止循環'
            self.LOOP_ALREADY_DISABLE = f'{self.__emojis.ERROR} 循環已經停止了'
            self.LOOP_ON = f'{self.__emojis.ERROR} 這個指令在循環啟用時無法使用. 請使用 {configs.BOT_PREFIX}loop off 來停止循環'
            self.BAD_USE_OF_LOOP = f"""{self.__emojis.ERROR} 無效的循環模式參數. 使用 {configs.BOT_PREFIX}help loop 來取得更多資訊.
                                -> 可選用的參數有: ["all", "off", "one", ""]"""

            self.SONGS_SHUFFLED = f'{self.__emojis.SHUFFLE} 成功隨機排列歌曲列表'
            self.ERROR_SHUFFLING = f'{self.__emojis.ERROR} 隨機排列歌曲列表時發生錯誤'
            self.ERROR_MOVING = f'{self.__emojis.ERROR} 移動歌曲位置時發生錯誤'
            self.LENGTH_ERROR = f'{self.__emojis.ERROR} 位置參數必須介於 1 與 列表長度 之間, 使用 -1 代表最後一首歌曲'
            self.ERROR_NUMBER = f'{self.__emojis.ERROR} 此指令參數必須為一個數字'
            self.ERROR_VOLUME_NUMBER = f'{self.__emojis.ERROR} 此指令參數必須為一個1~100的數字'
            self.ERROR_PLAYING = f'{self.__emojis.ERROR} 在播放歌曲時發生錯誤'
            self.COMMAND_NOT_FOUND = f'{self.__emojis.ERROR} 未找到此指令, 輸入 {configs.BOT_PREFIX}help 查看指令列表'
            self.UNKNOWN_ERROR = f'{self.__emojis.ERROR} 未知的錯誤, 如果需要, 請使用 {configs.BOT_PREFIX}reset 來重置播放器'
            self.ERROR_MISSING_ARGUMENTS = f'{self.__emojis.ERROR} 在此指令未找到任何參數. 輸入 {configs.BOT_PREFIX}help "command" 查看此指令的資訊'
            self.NOT_PREVIOUS = f'{self.__emojis.ERROR} 沒有上一首歌曲了'
            self.PLAYER_NOT_PLAYING = f'{self.__emojis.ERROR} 目前沒有歌曲正在播放. 使用 {configs.BOT_PREFIX}play 來播放一個歌曲'
            self.IMPOSSIBLE_MOVE = '執行無效 :('
            self.ERROR_TITLE = '錯誤 :-('
            self.COMMAND_NOT_FOUND_TITLE = '無效的指令 :-('
            self.NO_CHANNEL = '播放音樂前請先進入一個語音頻道當中.'
            self.NO_GUILD = f'此伺服器並無播放器正在播放, 請使用 {configs.BOT_PREFIX}reset'
            self.INVALID_INPUT = f'無效的連結, 尋求協助請輸入 {configs.BOT_PREFIX}help play'
            self.INVALID_INDEX = f'索引的參數無效.'
            self.INVALID_ARGUMENTS = f'參數無效.'
            self.DOWNLOADING_ERROR = f"{self.__emojis.ERROR} 無法下載和播放此影片"
            self.EXTRACTING_ERROR = f'{self.__emojis.ERROR} 搜尋歌曲時發生錯誤'

            self.ERROR_IN_PROCESS = f"{self.__emojis.ERROR} 由於內部發生錯誤, 播放器已被重啟, 並跳過此首歌曲."
            self.MY_ERROR_BAD_COMMAND = '該字串用於驗證是否是為我自己故意引發的錯誤'
            self.BAD_COMMAND_TITLE = '錯誤使用指令'
            self.BAD_COMMAND = f'{self.__emojis.ERROR} 使用此指令的方式錯誤, 輸入 {configs.BOT_PREFIX}help "command" 查看此指令的資訊'
            self.VIDEO_UNAVAILABLE = f'{self.__emojis.ERROR} 抱歉. 無法下載此影片.'
            self.ERROR_DUE_LOOP_ONE_ON = f'{self.__emojis.ERROR} 這個指令無法在循環啟用時執行. 請使用 {configs.BOT_PREFIX}loop off 停止循環.'


class SearchMessages(Singleton):
    def __init__(self) -> None:
        if not super().created:
            config = VConfigs()
            self.UNKNOWN_INPUT = f'請更換關鍵字, 或輸入 {config.BOT_PREFIX}help play'
            self.UNKNOWN_INPUT_TITLE = '無搜尋結果'
            self.GENERIC_TITLE = '連結無效'
            self.SPOTIFY_NOT_FOUND = 'Spotify 無法使用此關鍵字來搜尋, 請檢查你的連結 或是稍等再試一次.'
            self.YOUTUBE_NOT_FOUND = 'Youtube 無法使用此關鍵字來搜尋, 請檢查你的連結 或是稍等再試一次.'
            self.DEEZER_NOT_FOUND = 'Deezer 無法使用此關鍵字來搜尋, 請檢查你的連結 或是稍等再試一次.'


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
