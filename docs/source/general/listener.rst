.. _add-listener:

===============================
addEventListener Arrow Function
===============================

The arrow function is a shorthand for an ordinary function. When used in
conjunction with the `addEventListener <https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener>`_
it has a narrow range of attributes. For us the important one is **input**.
It allows one to handle events such as **click** or **key press** on any of the
form elements and obtain the
new target **value** to be used according to the script.

As we are dealing with simple variables containing numbers or text simple replacement
will usually work.

A typical example is as follows, where the slider **value** is picked up and
used for the **output**::

   <label style="width: 55%;">
      <input type="range" min="-20" max="20" value="0">
      <output>0</output>
   </label>

   <script>

   addEventListener("input", e => {
      e.target.nextElementSibling.value = e.target.value  ;
   });

   </script>

|

addEventListener
   is using the **=>** shorthand function method.
"input"
   refers to a change in any form element
event (e may be used instead)
   is the handle for the Listener
event.target/e.target
   is the slider, when multiple sliders are used some means to differentiate
   may be necessary depending on the HTML structure.
nextElementSibling
   this is the slider's sibling - the output
value
   the target's value on one side of the replacement and in this case output's
   value

When starting the script the slider automatically takes the mean of min and max
if no **value** is given, but there is no output value yet. Either put in the
mean of min and max, or else write a short instruction to the user.

Make sure that the input and output are tied together structurally or as a last
resort using identities.
