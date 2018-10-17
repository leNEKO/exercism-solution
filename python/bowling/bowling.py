class BowlingGame:
    def __init__(self):
        self._rolls = []
        self._frames = []
        self.new_frame()

    @property
    def _frame_cursor(self):
        return len(self._frames) + 1

    def new_frame(self):
        """ record a new frame """

        new_frame = False

        if self._frame_cursor < 10:
            new_frame = Frame(self)
        elif self._frame_cursor == 10:
            new_frame = TenthFrame(self)

        if new_frame != False:
            self._frames.append(new_frame)

    def roll(self, pins):
        """ Record a new roll """

        # validate pins value
        if not (0 <= pins <= 10):
            raise ValueError("0 <= pins <= 10")

        # create a new Roll
        new_roll = Roll(pins)
        # record it in common history
        self._rolls.append(new_roll)
        # and in the current frame
        self._frames[-1].frame_roll(new_roll)

    def score(self):
        """ Total score """
        return sum(frame.frame_score() for frame in self._frames)


class Roll:
    """ A roll """

    def __init__(self, pins):
        self.pins = pins

    def __repr__(self):
        return "{}".format(self.pins)


class CommonFrame:
    """ Common frame mechanics """

    def __init__(self, parent):
        self._pins = 10
        self._roll = 2
        self._score = []
        self._parent = parent

    @property
    def _is_finished(self):
        return self._pins == 0 or self._roll == 0

    @property
    def _type(self):
        empty_roll = self._roll == 0
        empty_pins = self._pins == 0
        return {
            (True, False): "STRIKE",
            (True, True): "SPARE",
            (False, True): "OPEN",
            (False, False): "UNFINISHED",
        }[(empty_pins, empty_roll)]

    def frame_roll(self, roll):
        """ record a new Roll

        Arguments:
            roll {Roll} -- a Roll object

        Raises:
            ValueError -- impossible pins value
        """

        self._pins -= roll.pins
        if self._pins < 0:
            raise ValueError("is someone cheating ?")
        self._roll -= 1
        self._score.append(roll)


class Frame(CommonFrame):
    """ Normal frame """

    def frame_roll(self, roll):
        super().frame_roll(roll)

        if self._is_finished:
            self._parent.new_frame()

    def frame_score(self):
        """ Calculate frame score
        (with look ahead)

        Returns:
            int -- total frame score
        """

        # look ahead
        length = {
            "STRIKE": 3,
            "SPARE": 3,
            "OPEN": 2,
            "UNFINISHED": 0
        }[self._type]

        key = self._parent._rolls.index(self._score[0])
        rolls = self._parent._rolls[key:key+length]
        return sum(roll.pins for roll in rolls)


class TenthFrame(CommonFrame):
    """ Special frame """

    def __init__(self, parent):
        self._bonus = 0
        super().__init__(parent)

    def frame_roll(self, roll):
        super().frame_roll(roll)

        if self._is_finished:
            # bonus roll
            if self._type in ["STRIKE", "SPARE"]:
                self._pins = 10
                self._bonus = 1

        if (self._roll < 0 and not self._bonus) or self._roll < -1:
            raise IndexError("Cannot roll another one")

    def frame_score(self):
        """ Calculate frame score

        Raises:
            IndexError -- If the frame is unfinished

        Returns:
            int -- frame total score
        """

        if self._bonus and self._roll != -1:
            raise IndexError("Unfinished game")

        return sum(roll.pins for roll in self._score)
