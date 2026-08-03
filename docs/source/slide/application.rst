===================
Sliders for Duotone
===================

.. image:: ../images/fires-bears.avif
   :width: 450
   :height: 450
   :alt: fires and bears
   :align: center

|

`Thanks to the Publishing Project <https://publishing-project.rivendellweb.net/what-are-duotones-and-how-they-work/>`_
on which my effort was based.

We have a standalone application which has eight sliders, two dropdown selections
and one set of four radio buttons. The original script was simplified by
using the some of the methods used to date. Our Javascript has one listener
and a few css
variables to control the sliders and dropdown selections. The radio buttons
require their own prefixed :ref:`listener <radio-select>`.

The idea of the generated settings being made in one place was copied. Each
of the layer groups were shown as containers together with their output shown
in individual windows.

Different images can be used in the main image, these are shown as thumbnails
used as the button input for :ref:`radio buttons <radio-thumb>`. There is a listener triggered when the
:ref:`DOM <radio-dom>` content is loaded, so that the default image is loaded when the page is refreshed -
otherwise the default thumb is highlighted but the main image remains at the last loaded.

The containers were made to have larger sliders, helping with the slider movement,
also the height was reduced. The system was kept static
as far as possible, so if the page was loaded and a slider changed or the drop
down selection changed no unexpected movement would result.

.. image:: ../images/Duotone.avif
   :align: center
   :alt: sliders used to create duotone images

We can use any pixel based image, apply a filter
to apply monochrome and brightness, then using two additional coloured
layers each of which has its own mix-blend-mode, create a duotone image. The pixels
of the different layers are blended together to create the final image.


.. |urarr|   unicode:: U+2197 .. UPRight ARROW

.. _duo-tone: ../_static/scripts/54duotone-application.html

.. |boat| image:: ../images/pbar-boat-a.avif
   :width: 36
   :height: 36
   :target: duo-tone_

|urarr| Click on the boat |boat| to see the duotone application.
Change the main image by clicking on one of the thumbnails.

Read the next section
to help when starting to use the application.

Getting Started
===============

The number of combinations is vast, but a good starting point is to gray the
image out and increase its brightness, so that the image shines through the
other layers. Leave the color sliders at their default middle settings, choose
the same blend modes for layers 2 and 3. You should be able to get different
colors starting from a gray image.

Select different images when it looks interesting - see whether they interact
differently. When you have a bit of confidence try experimenting with opposites.

Select different layer colours that are complementary (hues which are
180 apart). Choose opposite blend modes - they are listed so that opposites are adjacent
in the drop down lists. Where the blend mode darkens use on the darker tone,
conversely where the blend mode lightens use with the lighter tone or you
can switch it round.

Use the following opposite blend mode combinations as an idea::

   Lightness
   Darken / Lighten
   Multiply / Screen
   Color Burn / Color Dodge

   Contrast
   Hard Light / Soft Light

   Color Inversion
   Difference / Exclusion

|

The other modes can be used to preserve the named HSL attribute of the top
element and take the remaining HSL attributes from the background::

   HSL Color Space
   Hue
   Saturation
   Color
   Luminosity

|

If the original image is not grayed out then its colors affect
the final coloring. **Color Inversion** changes colors but using Difference
and Exclusion together shifts the output. Normal blocks the output to a single colour, but
experimentation is the name of the game.

The **Wave** has few colors but the results
are pleasing. Change the image, probably a striking image will work better -
also try one with strong highlights and deep shadows. If it works as a black and
white image it should look good as duotone. The two young ladies have been used
to show off duotone - if you can see the brickwork in the background you probably
are not far off a respectable duotone - the offices and red grouse have been introduced for
variety.

All the colors are based on the OKLCH system (lightness, chroma, hue), lightness
is perceptual lightness, so is closer to how we see color.

Older methods used values of 0-100% for lightness, chroma and grayness.
More modern usage have values 0.0-1.0 as the range, brightness has a larger maximum,
formerly used 0-150%, now uses 0.0-1.5.

Overwhelmed ?
-------------

There are just too many variables each with loads of terms and modes
that is just too much.
Think what the alternative would be - Photoshop or Gimp with all their terms
and different modes. To apply one change takes time - quite a bit. Now look
at the application in one minute probably 10 or more changes can be made easily - try
that in Photoshop or Gimp.

Explanation
===========

There are three layers the first has an image whose colors can be changed by
filter to be grayer or brighter. The next two layers are colored by oklch and
have blend-mode-mix applied.

The filter
shows a base color (orange) and as it becomes grayer changes to black or gray
depending on the brightness. The other two layers show what color we have selected.
Each slider shows its output. Lastly there is a summary of the
settings used under "Generated Settings:" and these change synchronously with
the adjustments.

All the changes were made through CSS variables, which resulted in a reduced
Javascript, as all the variables could be called from one source. Once again
we used a single addEventListener for all the input - sliders and dropdown
selectors. Since we have mixed input we have to add a conditional clause to
only apply output to the sliders - dropdown selectors, in common with all other
input methods, already has its output showing. Using the **name** attribute
with its CSS variable we know where the change should be applied.

The rest of the Javascript was used to update our setting summary. The HTML
was written using a Javascript template literal, the output follows the
typing requiring no concatenation or new line commands.

Try Making Something Similar
----------------------------

See whether you can make something similar for the two young ladies:-

.. image:: ../images/face-to-face-r.avif
   :width: 498
   :height: 386
   :align: center

The grouse image produced interesting patterns:-

.. image:: ../images/grouse-duo.avif
   :width: 341
   :height: 224
   :align: center

