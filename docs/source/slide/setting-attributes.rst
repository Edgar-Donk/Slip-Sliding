

==================
Setting Attributes
==================

.. image:: ../images/min-max-trackway.avif
   :width: 408
   :height: 68

As seen in the figure above the min corresponds to 0 and max is 100.
The step was set to 25 and the ticks and remaining labels correspond.

.. note:: Special Setting

   For this example the min and max value were spelt out, normally the min
   and max values would be shown - in this case 0 and 100.

min & max Attributes
====================

The two most important attributes are **min** and **max**, these set the minimum
and maximum extent of the slider. When the round part (thumb) is hard up against the
leftmost part of the slider it's at its minimum **min** and when it is hard up against
the rightmost part of its slider it's at its maximum **max**. As we have said if
these are not set then the default settings of 0 and 100 apply.

step Attribute
==============

The next attribute
that normally needs setting is **step** which adjusts the change in value when
the thumb moves the smallest amount. Different steps alters the way the thumb moves
along the trackway. Our minimalist slider used the default step size of 1, which on
a slider moving between 0 and 100 gives a 100 steps and moves smoothly. Change the
step to 25 and the movement is jerky in comparison. If there are fewer steps across
the range it becomes difficult to make the thumb move by dragging the mouse, then click
on the trackway adjacent to the thumb in the required direction.

value Attribute
===============

If you require the slider to start from a set value then set **value**, when the
slider is first instantiated it will have its thumb over the set value. The value
must correspond to a setting within the range (max - min) and steps, so if we had a
range of 0 to 100 with a step of 5, a starting value could be anywhere between 0 and
100 inclusive in multiples of 5 - so 4 would not work, but 20 would. The starting
value only works once, you can modify the settings or refresh the browser, it only
works when you start fresh.

Set Attributes
==============

The attributes are set in html so every value is quoted::

    <input type="range" min="0" max="100" step="1">

or::

    <input
    type="range"
    min="0"
    max="100"
    step="1"
    >

.. hint::

    The closing chevron requires no divide sign - so::

        <input type="range"> **correct**
        not <input type="range"/> **wrong**

There are other attributes we can set which will be shown as required. A larger
selection is available with :ref:`standard attributes <slider-attr>` also specials.

It should be apparent that we are missing vital feedback for the user. This can
be resolved either by displaying the changing value or by adding ticks (small vertical
lines) and labels indicating the value when the thumb is over a tick.

Let's start by giving immediate feedback by using fixed output.
