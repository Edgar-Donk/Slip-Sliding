

==============
Drop Down List
==============

The drop down list can be made using the select element::

   <label>Choose a fruit</label>
   <select name="fruits">
      <option value="apple">Apple</option>
      <option value="banana" selected>Banana</option>
      <option value="cherry">Cherry</option>
   </select>

At startup the drop down list box shows the selected entry or the first entry
if there is no selected entry, when it is clicked
it shows all the options then click on your choice the list closes and now
the box shows the new selection. Each option has their own value and output so
these change in line with the choice.

It has properties in common with other inputs belonging to form. Unlike the
slider its output is already showing when a change is made. A listener can
detect the change so the same listener that is used for multiple sliders is
used for the drop down selector. We can use the selector's name attribute to
pinpoint the change we require, if required we can add a dataset for any units
used in the change::

   // slider and dropdown selector
   addEventListener("input", e => {
       const inp = e.target;
       console.log("inp", inp);
       const effect = inp.value+(inp.dataset.suffix||'');
       const hasRange = e.target.matches('input[type="range"]');
       // check if slider, then use effect to change output, selector shows already
       if (hasRange) {
         inp.nextElementSibling.value = effect;
       };
       // both slider and selector change elements
       document.body.style.setProperty(inp.name, effect);

|
