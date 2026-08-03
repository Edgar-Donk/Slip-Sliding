.. _slider-attr:

==========
Attributes
==========

Attributes are found within the **inp** tag.

Standard Attributes
===================

value
-----

This must be equivalent to a valid floating point number, between the minimum
(**min**) and maximum (**max**) values and a multiple of **step**, default 1.
When the **value** is set the thumb positions itself to the value when the
slider is initialised, otherwise the default value at mid range is used.

max
---

The maximum value of the range, has to be greater than
the minimum value. This must be a valid number, or else it is not set.

min
---

The minimum value of the range, has to be less than the
maximum value. This must be a valid number, or else it is not set.

step
----

The step specifies the granulity of the value. The default is 1 which means
integers may be entered. However a string value of **any** means no stepping
is used and the difference between values has no limit.
Decimal values may also be entered.

list
----

The list attribute is the id of a <datalist> that holds the predefined values used
for the tick positions. Ticks are small marks made perpendicular to the trackway length.
Ticks often divide the range into smaller chunks and
represent a multiple of the steps. The datalist can be used to label the ticks.

name
----

The name of the input, used to reference the value in forms. Often the name and
id have the same value. Radio buttons have a common name but different ids.
Used to dynamically allocate a CSS Variable when dealing with a general Javascript
Listener.

oninput
-------

oninput provides immediate feedback from html to javascript.


Non-Standard Attributes
=======================

orient
------

Orientation of the slider, horizontal or vertical where horizontal is the default.
Vertical sliders easily show equally spaced
tick labels.

progress
--------

As the thumb moves in the trackway the colour of the left hand track changes
on most of the sliders apart from Opera.

Special Attributes
==================

The slider can gain many different extra additions, which for want of a better
expression we call special attributes. The range input seems to be flexible,
and we can add quite a few additions.

id
--

Standard method to add a unique identity for the element.

class
-----

A way to assign one or more class names to an element. This may be superfluous
when styling the slider as we can use **input[type=range]**.

style
-----

Adding inline styling to the element. CSS Variables can be used within
range styling.

data-suffix
-----------

Used to dynamically allocate a unit for the CSS Variable when dealing with a general Javascript
Listener.
