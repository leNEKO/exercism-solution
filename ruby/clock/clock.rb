# Clock : a clock that handles times without dates
class Clock
  HOUR = 60
  DAY = HOUR * 24

  attr_reader :minutes

  def initialize(hour: 0, minute: 0)
    # convert to minutes & wrap around day
    @minutes = (hour * HOUR + minute) % DAY
  end

  def to_s
    format('%02d:%02d', *minutes.divmod(HOUR))
  end

  def +(other)
    self.class.new(
      minute: minutes + other.minutes
    )
  end

  def -(other)
    self.class.new(
      minute: minutes - other.minutes
    )
  end

  def ==(other)
    minutes == other.minutes
  end
end
