"""You can use it to play simple tunes, provided that you connect a speaker to your board.
By default the music module expects the speaker to be connected via pin 0
"""

import microbit


# static variables
DADADADUM = tuple()
ENTERTAINER = tuple()
PRELUDE = tuple()
ODE = tuple()
NYAN = tuple()
RINGTONE = tuple()
FUNK = tuple()
BLUES = tuple()
BIRTHDAY = tuple()
WEDDING = tuple()
FUNERAL = tuple()
PUNCHLINE = tuple()
PYTHON = tuple()
BADDY = tuple()
CHASE = tuple()
BA_DING = tuple()
WAWAWAWAA = tuple()
JUMP_UP = tuple()
JUMP_DOWN = tuple()
POWER_UP = tuple()
POWER_DOWN = tuple()

def set_tempo(ticks: int = 4, bpm: int = 120) -> None:
    """Sets the approximate tempo for playback. A number of ticks (expressed as an integer)
    constitute a beat. Each beat is to be played at a certain frequency per minute (expressed as the
    more familiar BPM - beats per minute - also as an integer).

    Suggested default values allow the following useful behaviour:

    music.set_tempo() - reset the tempo to default of ticks = 4, bpm = 120
    music.set_tempo(ticks=8) - change the “definition” of a beat
    music.set_tempo(bpm=180) - just change the tempo

    To work out the length of a tick in milliseconds is very simple arithmetic:
    60000/bpm/ticks_per_beat . For the default values that's 60000/120/4 = 125 milliseconds or 1
    beat = 500 milliseconds
    """
    _t = ticks
    _b = bpm

def get_tempo() -> tuple:
    """Gets the current tempo as a tuple of integers: (ticks, bpm)"""
    return (1, 1)

def pitch(
    frequency: int,
    duration: int = -1,
    pin: microbit._MicroBitTouchPin = microbit.pin0,
    wait: bool = True
    ) -> None:
    """Plays a pitch at the integer frequency given for the specified number of milliseconds. For
    example, if the frequency is set to 440 and the length to 1000 then we hear a standard concert A
    for one second.

    Note that you can only play one pitch on one pin at any one time.

    If wait is set to True, this function is blocking. If duration is negative the pitch is played
    continuously until either the blocking call is interrupted or, in the case of a background call,
    a new frequency is set or stop is called (see below)
    """
    _f = frequency
    _d = duration
    _p = pin
    _w = wait

def stop(pin: microbit._MicroBitTouchPin = microbit.pin0) -> None:
    """Stops all music playback on a given pin, eg. music.stop(pin1). If no pin is given, eg.
    music.stop() pin0 is assumed
    """
    _ = pin

def reset() -> None:
    """Resets the state of the following attributes in the following way:
        ticks = 4
        bpm = 120
        duration = 4
        octave = 4
    """
