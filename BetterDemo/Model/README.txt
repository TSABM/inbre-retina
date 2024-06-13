The model handles the actual backend stuff. In this case holding data, dealing with the interactions, holding objects, etc.
These things should communicate with presenters which in turn communicate with the views (where the views render the display 
and send user inputs to the presenters to be sent back here)