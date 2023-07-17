from Config.Singleton import Singleton
from Config.Configs import VConfigs


class Helper(Singleton):
    def __init__(self) -> None:
        if not super().created:
            config = VConfigs()
            self.HELP_SKIP = '跳過目前的歌曲.'
            self.HELP_SKIP_LONG = '跳過目前的歌曲, 請在關閉單曲循環的狀態下使用. \n\n參數: 無.'
            self.HELP_RESUME = '繼續播放歌曲.'
            self.HELP_RESUME_LONG = '當播放器處於暫停狀態, 將繼續播放歌曲. \n\n參數: 無.'
            self.HELP_CLEAR = '清除目前的歌曲列表及歷史紀錄.'
            self.HELP_CLEAR_LONG = '清除目前的歌曲列表及歷史紀錄. \n\n參數: 無.'
            self.HELP_STOP = '將播放器停止.'
            self.HELP_STOP_LONG = '將播放器停止, 清除目前的歌曲列表及歷史紀錄並退出語音頻道.\n\n參數: 無.'
            self.HELP_LOOP = '控制目前的循環狀態.'
            self.HELP_LOOP_LONG = """控制目前的循環狀態.\n\n 執行需求: 正在播放歌曲.\n參數:
                One - 單曲循環.
                All - 列表循環.
                Off - 停止循環."""
            self.HELP_NP = '查看目前播放歌曲的資訊.'
            self.HELP_NP_LONG = '查看目前播放歌曲的資訊.\n\n執行需求: 正在播放歌曲.\n參數: 無.'
            self.HELP_QUEUE = f'查看列表中 前{config.MAX_SONGS_IN_PAGE}首 歌曲.'
            self.HELP_QUEUE_LONG = f'查看列表中 前{config.MAX_SONGS_IN_PAGE}首 歌曲.\n\n參數: 無.'
            self.HELP_PAUSE = '暫停播放器.'
            self.HELP_PAUSE_LONG = '如果正在播放, 將暫停正在播放的歌曲.\n\n參數: 無.'
            self.HELP_PREV = '播放上一首歌曲.'
            self.HELP_PREV_LONG = '播放上一首歌曲. 如果正在播放, 當前的曲目會返回列表中.\n\n執行需求: 循環停用.\n參數: 無.'
            self.HELP_SHUFFLE = '列表隨機排列.'
            self.HELP_SHUFFLE_LONG = '將歌曲列表重新且隨機排列.\n\n參數: 無.'
            self.HELP_PLAY = '播放歌曲.'
            self.CHANGE_VOLUME = '設置音量大小.'
            self.CHANGE_VOLUME_LONG = '設置音量大小, 為 0 到 100 的數字.'
            self.HELP_PLAY_LONG = '在 Discord 中播放音樂. \n\n執行需求: 你正在一個可被機器人加入的語音頻道中.\n參數: Youtube, Spotify 或 Deezer 的歌曲連結 或是 歌曲在 Youtube 中的標題或是關鍵字.'
            self.HELP_HISTORY = f'查看歷史紀錄.'
            self.HELP_HISTORY_LONG = f'查看 {config.MAX_SONGS_HISTORY}首 在歷史紀錄中最近播放的歌曲'
            self.HELP_MOVE = '在歌曲列表中 將 位置A 的歌曲 移動至 位置B.'
            self.HELP_MOVE_LONG = '在歌曲列表中 將 位置A 的歌曲 移動至 位置B.\n\n執行需求: 位置A 與 位置B 必須為有效的數字.\n參數: 1º Number => 初始位置, 2º Number => 目標位置. 兩者都可使用 -1 代表歌曲列表中最後一首歌曲.\n預設選項: 如果指令只有填入一個參數, 將會選擇 第1首 歌曲, 移動至參數位置.'
            self.HELP_REMOVE = '刪除位於 位置A 的歌曲.'
            self.HELP_REMOVE_LONG = '刪除位於 位置A 的歌曲.\n\n執行需求: 位置A 必須為有效的數字.\n參數: 位置A          Number => 介於 1~列表長度 的數字.'
            self.HELP_RESET = '重置播放器.'
            self.HELP_RESET_LONG = '重置此伺服器的播放器. 推薦在發生未知的錯誤時使用此指令.\n\n參數: 無.'
            self.HELP_HELP = f'使用 {config.BOT_PREFIX}help "command" 獲取更多指令資訊.'
            self.HELP_HELP_LONG = f'使用 {config.BOT_PREFIX}help "command" 獲取更多指令資訊.'
            self.HELP_INVITE = '傳給機器人邀請連結, 將機器人加入至伺服器.'
            self.HELP_INVITE_LONG = '在文字頻道中傳送你的伺服器的邀請連結, 機器人將會加入你的伺服器.\n\n參數: 無.'
            self.HELP_RANDOM = '回傳一個介於 1 至 x 的數字.'
            self.HELP_RANDOM_LONG = '回傳一個介於 1 至 x 的數字.\n\n執行需求: 傳送的數字為一個有效的數字.\n參數: 1º 任何可當作範圍的數字.'
            self.HELP_CHOOSE = '回傳選擇的隨機字串.'
            self.HELP_CHOOSE_LONG = '隨機回傳一個您輸入的字串.\n\n執行需求: 字串之間請使用半形逗號分隔.\n參數: 任何你想要的字串.'
            self.HELP_CARA = '回傳 正面 或 反面.'
            self.HELP_CARA_LONG = '回傳 正面 或 反面 .'

            self.SLASH_QUEUE_DESCRIPTION = f'歌曲列表的頁面數字, 一頁有 {config.MAX_SONGS_IN_PAGE} 首歌曲'
            self.SLASH_MOVE_HELP = '在歌曲列表中 將 位置A 的歌曲 移動至 位置B'
