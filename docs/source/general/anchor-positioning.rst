.. _anchor-pos:

======================
CSS Anchor Positioning
======================

This gives us the ability to tether two elements together. It also enables
us to specify alternative positions if the anchor position causes the tethered
element to overflow or rendered offscreen. We can also declare conditions when
the tethered element is to be hidden.

Older scripts would need to use javascript and the programmer would need to
calculate the positions of the anchor element, its size and the position and
size of the tethered item and what should occur if the anchor moves. Anchor
positioning involves no calculation. Just a few CSS clauses to indicate the
anchor and the tethered element and its position relative to the anchor.

In this basic example most of the script was about styling the **anchor** and
**infobox** the tethered element::

   <style>
   .anchor {
     font-size: 1.8rem;
     color: white;
     text-shadow: 1px 1px 1px black;
     background-color: hsl(240 100% 75%);
     border-radius: 10px;
     border: 1px solid black;
     padding: 3px;
     width: fit-content;
   }

   .infobox {
     color: darkblue;
     background-color: azure;
     border: 1px solid #dddddd;
     padding: 10px;
     border-radius: 10px;
     font-size: 1rem;
   }
    /* the anchor positioning part follows */
   .anchor {
     anchor-name: --my-anchor;

   }

   .infobox {
     position: fixed;
     position-anchor: --my-anchor;
   }

   </style>

   <div class="anchor">⚓︎</div>

   <div class="infobox">
     <p>This is an information box.</p>
   </div>

|

.. image:: ../images/basic-anchor.png
    :width: 421px
    :align: center
    :height: 275px
    :alt: basic-anchor

|

When this script is run we see a mauve anchor in the upper left corner, sitting
underneath is the azure tethered element (infobox). The positioning used the
default setting from the browser.
What happens when the anchor moves - it becomes a bit more complicated.
This next example has an anchor inside a block of text, the tethered element
(infobox) sits on the right side of the anchor, separated by a margin. Hover
over the anchor it grows in size by expanding rightwards, which pushes the
tethered element rightwards as well, at the same time the margin is recalculated
and it enlarges as the anchor grows.

.. raw:: html

   <br>
   <details>
   <summary style="color:#018199;">
   <b> <i> Show/Hide Code </i> anchor-position-margin.html </b> </summary>

   <br>

   <style>
   /* You can use the anchor-size() function within a margin-* property
   value to set element margins based on their anchor element's size
   margin-left: calc(anchor-size(width) / 4);
   margin-block-start: anchor-size(--my-anchor self-block, 20px);

   In the HTML, we specify two <div> elements, one anchor element and one
   infobox element that we'll position relative to the anchor. We give the
   anchor element a tabindex attribute so that it can be focused via the
   keyboard. We also include filler text to make the <body> tall enough to
   require scrolling, but this has been hidden for the sake of brevity.

   hover and tab show the change

   infobox to right anchor */

   legend {
        display: block;
        width: 30em;
        border: 1px solid silver;
        border-radius: 1em;
        background-color: ghostwhite;
        padding: 1em 0 1em 0;
        display: flex;
        text-align: center;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        }

   .anchor {
     font-size: 2rem;
     color: white;
     text-shadow: 1px 1px 1px black;
     background-color: hsl(240 100% 75%);
     text-align: center;
     align-content: center;
     outline: 1px solid black;
   }

   body {
     width: 80%;
     margin: 0 auto;
     position: relative;
   }

   .infobox {
     align-content: center;
     color: darkblue;
     background-color: azure;
     outline: 1px solid #dddddd;
     font-size: 1rem;
     text-align: center;
   }

   /* from here on we are setting anchor positionimg */
   .anchor {
     anchor-name: --my-anchor;
     width: 100px;
     height: 100px;
     transition: 1s all;
   }

   .infobox {
     position-anchor: --my-anchor;
     position: absolute;
     height: 100px;
     width: 100px;
   }
   .anchor:hover,
   .anchor:focus {
     width: 300px;
   }

   .infobox {
     /*top: anchor(top);*/
     position-area: right;
     left: calc(anchor-size(width) / 4);
     margin-right: calc(anchor-size(width) / 4);
   }
   </style>
   <legend>
   <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>

   <p>
     Nisi quis eleifend quam adipiscing vitae proin sagittis nisl rhoncus. In arcu
     cursus euismod quis viverra nibh cras pulvinar.
   </p>
   <div class="anchor" tabindex="0">⚓︎</div>

   <div class="infobox">
     <p>Infobox.</p>
   </div>
   <p>Vulputate ut pharetra sit amet aliquam.</p>

   <p>
     Malesuada nunc vel risus commodo viverra maecenas accumsan lacus. Vel elit
     scelerisque mauris pellentesque pulvinar pellentesque habitant morbi
     tristique. Porta lorem mollis aliquam ut porttitor. Turpis cursus in hac
     habitasse platea dictumst quisque. Dolor sit amet consectetur adipiscing elit.
     Ornare lectus sit amet est placerat. Nulla aliquet porttitor lacus luctus
     accumsan.
   </p>
   </legend>


   </details>

|
