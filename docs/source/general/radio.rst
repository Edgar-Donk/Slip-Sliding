.. _radio-but:


============
Radio Button
============

Radio buttons operate slightly differently from the other types of form
input. A group of radio buttons are used together, they are linked so that
only one button can be checked at a time, which means that **name** defines
the group.

.. _radio-thumb:

Styling Radio Buttons
=====================

The method for styling is simply to cover the buttons with a thumbnail of the
image we wish to display. Starting with the HTML each radio button and its image
are made as a unit by enclosing by the input's label::

   ...
   <form id="thumbform" autocomplete="off">

   <label>
      <input type="radio" name="thumb" value="../../images/waves.webp" class="custom-radio">
      <img id="firstThumb" class="thumbs" src="../../images/waves.webp" alt="waves">
   </label>
   ...

|

The style can now be added, first for the thumbs of the images, then the radio
buttons::

   .thumbs {
      position: relative;
      width: var(--thumbs-width);
      aspect-ratio: 16 / 9;
   }

   /* styling for radio thumbnails */

   [type=radio] {
     position: absolute;
     opacity: 0;
     width: 0;
     height: 0;
   }

   [type=radio] + img {
     cursor: pointer;
     border: 2px solid transparent;
     transition: border-color 0.3s ease;
   }

   [type=radio]:checked + img {
     border-color: #007bff;
     box-shadow: 0 0 8px rgba(0, 123, 255, 0.5);
   }

   [type=radio]:hover + img {
     opacity:0.7;
     cursor: pointer;
   }

   input[type="radio"]:checked:focus-visible + img {
      outline: solid 1px #007bff;   /* Outline when both checked and focused */
      box-shadow: 0 0 8px rgba(0, 123, 255, 0.5);
   }

|

.. _radio-dom:

On Startup
==========

One of the group can be defined as **default**, this has **checked** written
in its **input**. On startup or after the page is refreshed the default
will show as checked, however unless an additional method is made the result
of checking the button will **not** be made. To activate the change either
use **DOMContentLoaded** or **window.onload**, the first is current when the browser
sets up the DOM before the components are fully loaded, the second is current
after everything is completely loaded. Since all the images are
local we can use the DOM method.

This method has its own listener::

    document.addEventListener('DOMContentLoaded', function() { // => not allowed
        const defaultRadio = document.querySelector('input[name="thumb"]:checked');
        theImage.style.backgroundImage = `url(${defaultRadio.value})`;
      });

..note::

    A normal function must be used with this listener, arrow functions throw an error.

We find the default radio button by searching for those elements with the
name **thumb** (in our case) also look for **checked**. The radio buttons
have had their **value** loaded with the address of one of the four images, so
when the browser is refreshed the default image is shown.

No Default
----------

If there is no default then the browser makes no selection and normally no
change is made to the output. In our
example the main image does change
from the last selection to the **wave**. The method above should only work if one of the buttons
has **checked** written in the **input** since the outcome for
**defaultRadio** is null without a known value. As it happens Firefox, Chrome,
Edge and Opera change the main image to the **wave** when refreshed.

.. _radio-select:

Selecting and Changing
======================

Change the image by normally selecting a radio button::

   const thumbNail = document.getElementById('thumbform');
   thumbNail.addEventListener('change', (e) => {
      // Ensure the change came from one of our thumb radio buttons - optional
   if (e.target.name === 'thumb') {
      theImage.style.backgroundImage = `url(${e.target.value})`;
      }
   });

|

The HTML had **form** enclosing the group of radio buttons, which can be given
an id to give a better way to select the group when used with a listener. As
form only encloses the one group of radio buttons there should be no reason
not to accept the output and change the main image.

Make sure the listener is using **change** - not click - otherwise clicking
on the selected option might cause a shudder.

This method is robust, there is no reason to enclose the listener and its arrow
function in another function as seen on several web sites.
