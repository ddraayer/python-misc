"""Construct ruler-like strings."""

__author__ = 'Dean Draayer'

def ruler(length, base=10, tick_major='|', tick_minor='.'):
    """
    Return a ruler-like string.

    Arguments:
        length     -- the overall number of tick marks on the ruler
        base       -- number of minor ticks per major tick
        tick_major -- character to use for major tick marks
        tick_minor -- character to use for minor tick marks

    Numeric labels are printed directly to the left of the major tick marks.
    Leftmost digits are truncated to fit the available space if necessary.

    Example: ruler(50, 8) returns
        '......8|.....16|.....24|.....32|.....40|.....48|..'
    """
    # NB: Number of digits available for label is (base - 1)
    label_modulus = 10 ** (base - 1)
    (num_major_ticks, num_leftover_ticks) = divmod(length, base)
    section = '{lbl:{tm}>{fw}d}{tM}'
    pieces = [section.format(
                    lbl=(base * i) % label_modulus,
                    fw=(base - 1),
                    tm=tick_minor,
                    tM=tick_major)
                for i in range(1, num_major_ticks + 1) ]
    pieces.extend(tick_minor * num_leftover_ticks)
    return ''.join(pieces)
