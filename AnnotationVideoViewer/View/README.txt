Handles actually rendering the application. Should receive info about the model from the presenters and notify the presenters when the user inputs
information.

note: "label" gets used in two different contexts in the views files. Informally I use "label" to refer to bounding boxes with the 
assotiated cell and event data, this is a leftover from an early design phase though I am intending to rename all informal label
uses. "label" in a more programatic sense is used by pyqt's widget package to refer to text labels placed in a widget.