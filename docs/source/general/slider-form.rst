.. _form:

===========
Slider Form
===========

A typical slider has inbuilt methods and usage derived from **form**, where it
makes sense to copy these rather than reinvent from scratch. In particular
copy the **tags** already used rather than have several **divs**. This should
help in understanding the purpose of the element::


     <fieldset>
       <legend>Fruit juice size</legend>
       <p>
         <input type="radio" name="size" id="size_1" value="small" >
         <label for="size_1">Small</label>
       </p>
       <p>
         <input type="radio" name="size" id="size_2" value="medium" >
         <label for="size_2">Medium</label>
       </p>
       <p>
         <input type="radio" name="size" id="size_3" value="large" >
         <label for="size_3">Large</label>
       </p>
     </fieldset>


|

We may not be creating a form but using these tags helps assistive technology
and shows programmers the element's purpose.

section
   Used for logical blocks of different input that form a unit.
fieldset
   Groups controls and their labels often inside a frame (has to be styled).
legend
   Describes the section and section purpose as a headline. When used with
   fieldset it can produce a label frame construct.
input
   Various methods by which the user interacts with the program.
label
   Describes the input purpose, each label can be associated with the input's
   identity using **for**. Alternatively the label can enclose the input and its
   children. A label gives the input an enlarged activation area.
output
   Shows the outcome when the input is changed.
focus-within
   pseudo-class matches an element if the element or any of its descendants
   are focused.
list
   When using a fieldset/legend combination an extra level of styling may be
   necessary, provided by list.

Check using different browsers, most will change styling compared to using
**div**. Adding ``display: block;`` in the CSS to make the tag behave like
**div**.

When using display methods such as flex or grid the results can be changed by
having **form** or not, also whether the **label** is inline (like span) or
surrounds the input. Label affects the styling by putting the contents in line
with the input. Legend works similarly to a headline in that it creates its own
line. Introducing a line break **<br>** wrecks links between input and output.

