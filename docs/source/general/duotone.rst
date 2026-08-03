==============
mix-blend-mode
==============

For each pixel among the layers to which it is applied, a blend mode takes
the colors of the foreground and the background, performs a calculation on them,
and returns a new color value.

Changes between blend modes are not interpolated. Any change occurs immediately.

Progressively going from black to white can change the behaviour of each mode.

If you have different background images or different gradients or a
background image and a gradient to blend in the same container use
background-blend-mode.


Applying mix-blend-mode
=======================

If you want to blend text, image or div to blend with the background then use
mix-blend-mode.

Most mix-blend-mode applications use only two layers.
mix-blend-mode controls how an element’s pixels blend with the pixels behind
it (its “backdrop”). That means it’s not just coloring the element. It is
literally mixing two pixel layers.

Blended text is one of the classic uses - text should be bold in either black
or white over a photo or gradient. Try **difference** for an auto-invert look or
**overlay** for punchy contrast.

**Multiply** darkens by multiplying colors together. Bright areas become more visible
and dark areas "sink". Color overlays "feel" printed onto the background. Adds
texture without destroying original image. Makes overlapping shapes look richer.

**Screen** is the opposite of multiply - it brightens by screening colors together.
Dark becomes more transparent and lighter parts glow.

Used for light leaks, glows and neon overlays.
Soft highlights on top of photos.
Make shapes look lit rather than painted.

**Overlay** is a contrast booster. It combines effects from multiply and screen,
dependant on the background.

Used for poster-style effects. Brings out texture. Makes overlays more integrated
than a simple opacity layer can.

**Difference** compares element and backdrop colors and shows their difference.
Often looks inverted to the backdrop.

Used on text remaining readable over changing backgrounds. Cursor-like UI accents
that stand out. Interactive effect using hover.

Creating Duotone Images
=======================

Duotone images are just one of the outcomes of using the css mix-blend-mode.
CSS has 15 different active modes (plus normal), most can be paired with
a mode that has an opposite effect.

Duotone images are one of the more complicated applications.
There are three layers the first has an image whose colors can be changed by
filter to be grayer or brighter. The next two layers are colored by oklch and
have blend-mode-mix applied. The resulting image is due to the intermixing
of each layer.

How was this Done
=================

The principle is shown and explained in `Brad Woods Digital Garden <https://garden.bradwoods.io/notes/css/blend-modes#duotone>`_ .
If you want to see what each of the blend modes does `look at Web.Dev <https://web.dev/learn/css/blend-modes/>`_.
For a closer look at what each `blend mode does by Dan Hollick <https://typefully.com/DanHollick/blending-modes-KrBa0JP>`_.
What can be done with background-blend-mode, mix-blend-mode or filter `on one image by Bennett Feely <https://bennettfeely.com/image-effects/>`_.
A background on duotones `photoshop or gimp based by Johnny Levanier <https://99designs.com/blog/trends/duotone-design/>`_.
Power technique with `five layers by Scott Vandehey <https://cloudfour.com/thinks/the-power-of-css-blend-modes/>`_.
