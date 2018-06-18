class Kline:
    def __init__(self, open, high, low, close, volume, date) -> None:
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.date = date

    def __str__(self) -> str:
        return "Date:" + self.date + "Open:" + self.open + "," + "Close:" + self.close + "," + "High:" + self.high + "," + "Low:" + self.low + "," + "Volume:" + self.volume
