# internship
Code and documents for the internship

## Day 32 7/13/24
10:51 am - 



## Day 31 7/12/24
12:26 pm - 1:23 pm

1:56 pm - 2:50 pm

4:00 pm - 5:00 pm

Plan: work on single frame loader, if possible also develop the square drawer for labelling.

refactored my approach to opening images. The new one ought to be much better. Now working on finishing it out.

Still working on last few steps

added an abstract view. trying to make it easier for the app to update widgets (particularly when a new image is opened) Hopefully this will mean the whole app could update easily. Not working yet, but working on it.

## Day 30 7/6/24
3:26 pm - 4:21pm
4:55 pm - 5:56 pm

working on loading one frame to start.

## Day 29 7/2/24
11:40 am - 12:06 pm

4:20 pm - 6:15 pm 

7:00 pm - 8:07

8:50 - 9:57

Going back to reading the image as a dask xarray if I can. xarray is having problems unfortunately. Checking to make sure my environement has xarray set up right.

this might not work. xarray still does not work. It looks like it might be an issue with the nd2 package using an old version of xarray. If so numpy arrays might be required... this would slow it down though.

Got xarray working, at least temporarily. It still crashes, but it tries to open the file.

stuck trying to get the image data to render. searching for a solution on stack overflow.

Ok changing the plan... Going to load the nd2 file reference into main memory for now and grab individual frames, actually I'm less sure now that would mean a lot of disc calls.

## Day 28 6/28/24
9:25 am - 11:00 am

11:44 am - 1:12 pm

1:46 pm - 4:00 pm

Finished some minor refactoring. Beginnning work on opening the first nd2 file.

opening it is harder than expected. Because the files are so large I am worried about memory concenrs. Trying to solve that by using a dask xarray but this is proving difficult to understand.

First nd2 image loaded successfully, but it crashes when I try to pull out one frame, looking into it. Also I beleive this first image at least is not in rgb format, but in rgba.

Continued reading up on nd2 and I learned how to extract a single frame correctly. Working on displaying one frame. Note this part may need to get overhauled since we will be processing such large files.

unable to get the first image rendering. Encountering an error converting a frame to a readable format for the canvas.

## Day 27 6/27/24
11:33 am - 12:25 pm

1:30 pm - 3:39 pm

4:15 pm - 5:16 pm

6:15 pm - 6:41 pm

7:37 pm - 8:15 pm

Trying to implement that main memory pipeline. 

imported nd2 package, learning how to use it to display an image with pyqt. Learned several things about the format, it will most likely need to be converted to some kind of array which should be able to be done quickly if some tricks are used. Its also possible to extract the files dimensions including the depth of layers which ought to be useful.

Working on rendering the first nd2 image. Requires a little refactoring. Having some difficulties still but going to have to call it for the day. Need to get it working soon. At least printing the name of the open file or something.


## Day 26 6/26/24
10:08 am - 2:15
2:50 pm - 3:18 (meeting)
4:18 - 4:26

Created a new class to hold all active scenes. The scenes container is class wide which should solve the previous issues related to crashing. Initial tests work.

Run into another problem like before where I need the menu to communicate with another widget. I think I found the solution, I'll use a publish subscribe model. I'm going to create a master memory where each model can be found via a simple address.

## Day 22 6/25/24
9:50 am - 2:50 pm

performed what will hopefully be the last refactor of the base code. Working on rendering those images now on the canvas.

Base canvas now renders again, hooking up the menubar to load one image.

I ran tests on the first attempt to load an image for labelling, it causes an immediate crash. Print off the filepath first to see if your giving it garbage.

Nope it looks like an issue in the central widget. I'm thinking my canvas import might be messed up. Found the issue, it was the class wide variable in the canvas, which was imported via the central widget. Read back into how thats handled, I asked chatGPT earlier for a tip on it and I think it was wrong.

All tries to fix the issue and still have a class wide canvas have failed. Any other class wide variable seems ok and even removing all references to a classwide canvas except its instantiation still causes a crash. I'm just going to have to move forward under the assumption that a class wide canvas (to be more specific QGraphicsScene) is not an option right now.

## Day 21 6/24/24
9:39 am - 1:31 pm

3:02 pm - 3:41 pm

Fixed the github repo so it no longer will keep outdated versions of this app. It will now also be easier for me to update the repo assuming no github syncing issues. Also fixed 3 out of 7 classes. 

Fixed most if not all the classes. Now to test and then implement segmentation if possible. Testing complete, window renders now. Now to hook up image rendering.

## Day 20 6/22/24
01:36pm - 3:10 pm

3:27pm - 3:34 pm

Going to try and fix the code today, if I can just get an image to load properly it will be good progress.

So far I havent made it to images loading but I did clarify the mvp issue fully. If I work quick I may be done refactoring in an hour.

Well I'm trying to do it right this time so its taking a bit longer than I'd like. Maybe 1/4th of the way done?  Fixed the main window and menubar now, both should work... though the menubar is now inheriting directly from the menubar widget which might be a mistake...

## Day 19 6/21/24
1:15 pm - 3:15 pm

4:15 pm - 5:15 pm

Working on the canvas classes. Working on letting the user 1) load any image, 2) add graphics items (this will be used for the labeling and segmentation), 3) resize the view (this will allow them to zoom in if something they want to label is small) 4) switch between several images keeping labels constant.

Started a sinlge image loader to test on a small scale my code. Need to refactor some code to allow cross view communication. Having difficulty with the cross class communication. I need a menubar view to somehow send a signal to the image area canvas model to change its details and then make sure the view is updated... I'm having difficulty without breaking the mvp...

Found the issue, I made an error with the mvp that is causing the issue... the views are handling too much. The Presenter should handle more and thus hopefully be able to provide better updates.

## Day 18 6/19/24
11:45 am - 12:15 pm

Started working to finish hours I missed yesterday, didnt realize I wasnt allowed to work on the holiday. Cutting shift short. Worked on the canvas, trying to get one layer working where I can draw rectangles.

## Day 17 6/18/24
10:30 am - 1:30 pm

3:45 pm - 4:00 pm (had family emergency had to cut this shift short)

Remving the abstract class didnt fix the problem. Its an issue with how paths are handled in python I beleive. I'm going to need to use absolute paths using sys to get updated paths. Its going to take some time to refactor all the files.

Figured out the issue and resolved it. The window now open as it should and renders the controls and canvas. The file explorer is broken and I still need to make the canvas do things but its a start.

Fixed file explorer

## Day 16 6/17/24
10:08 am - 2:00 pm

3:35 pm - 4:35

Spent the day so far fixing issues with the restructuring. Now I think I'm mostly done but even when I am this wont have any more functionality than before, but still the pattern is supposed to help redability and help people who may have to maintain this code in the future. A bit more boring refactoring and then I ought to be able to run the next test. If it renders correctly then its time to try an implement the labelling functionality which is going to be fun to figure out.

Could not for the life of me get it to run. Everything should be in the proper directories but Python is having trouble handling imports. I need to figure out a way to fix it or else use absolute paths or something... Havent been able to test the newly refactored code due to this module importing issue.

## Day 15 6/15/24
11:45 am - 2:00 pm

Cleaned up menubar behind the scenes a bit. Still not functional but the view now tries to talk exclusivley with the presenter. Cleaning up that presenter now and the model.

Menubar should now all conform to the mvp pattern. Still need to make the filtered file list get stored appropriately and make closing the application work too.

## Day 14 6/14/24
10:00 am - 12:15 pm

5:45 pm - 07:00 pm

Began work from home. Intend to work on completing the restructuring today, and maybe getting the canvas working. 

Restructuring is going slow but ok so far. I still need to finish moving main chunks of code and then I need to finish refactoring portions so it all renders like it should. Continued the restructuring. Almost all of the code is in the correct places, now I'm beggining to repair the broken program (fixing calls to self, connecting classes, adding helper methods etc.)

## Day 13 6/13/24
10:15 am - 3:30 pm 

Working on classes and drawing to the canvas. Its not as straightforward as I'd like but I think I'll be drawing tons of dots wherever the mouse moves to? Its a bit primitive...

I've gone ahead and changed the file structure to a model,view,presenter structure commonly used for gui's. Most of the files are still not functional at all but the structure is almost where it needs to be. I'm working on the canvas class then the pen then the canvas view... and then the presenter...The addition of a presenter complicates things but it will probably help with dev stuff later.

Met with dr zhang and went over what direction the project needs to go. Right now priorities include fixing the null file error, finishing rendering the canvas, implement drawing boundry boxes, and implement saving boundry boxes. The goal is to let someone have an ai approximate labels quickly and then let them quickly touch up the labels and box positions. Segmentation areas will be needed but should be done later.

## Day 12 6/12/24
10:30 am - 3:30 pm

Worked a metric ton on fixing up the image area. I have a little menubar now to hold the images within an open folder. There are issues, such as me becoming more and more convinced I'm goin gto need to tear all of this down and refactor them into objects and classes and such to make it object oriented, but for now I'm leaving it because doing that now will mean I'll never get to anything else before reporting in.

Well I didnt leave it, I started developing the classes needed and began prepping to move everything over to individual classes. I also started reading on how to start drawing onto the canvas. I may go to drag and drop rectangles I just havent figured out all the details yet. The end goal is to have a number of images load in, one loads in as a base layer then you can identify objects in it on a layer above that and save a csv or something indicating the objects.

## Day 11 6/11/24
11:00 am - 3:15 pm

Spent the first hour and a half completing all required employee trainings

Downloaded a pyqt based photoshop style app to see how they implemented image layers and editing. Began studying QGraphics. Its much better than what I was doing before. QgraphicsScene acts as a whiteboard where actual image editing positioning and rendering can be done. QGraphicsItem includes all objects I may want to interact with (in this case I think this would be the layers). And Then QGraphicsView affects the rendering which means this view can be manipulated, shrunk, expanded, etc without changing the origonal image. The tools and abilities QGraphics offers I think aligns perfectly with what we want our app to do (if we dont use napari).

Still learning about QGraphics. Its a feature full set of tools. 

## Day 10 6/10/24
10:00 am - 3:00pm

Spent most of the day so far trying to set things up to test another independent pyqt5 project that is supposed to annotate images. However it seems its not working with my current tests. Its gui is also much more primitive than I expected (functional but primitive). Its making me wonder how interactive our gui will need to be. I'm trying a simpler image to give the program to see if that helps it tag it correctly.

Ah got it working. It only allows some file types. Also it only splits images into different classes. E.g. if I had 10 images, half of clowns and the other of coins this program is just an interface to make a csv classifying each image as a clown or coin. That shouldnt be too hard to replicate.

resolved the formatting issue plauging the early versions of the demo app. Now to fix some functionality issues. 

Menus and sub menus now work, and an exit button has been implemented

Implementing a file dialog that selects a folder and grabs all the files of the desired type. The dialog works, but it wont select directories yet, I need to review how that is handled.

## Day 9 6/7/2024
10:06 am - 3:00 pm

As recommended I turned back to focusing on pyqt and my demo app. It needs some major overhauls since before it was just dabbling with pyqt's base functions. I'll see what I can do.

The old code has needed some work. With a week of napari I'm finding progress on the pyqt has been slow. I fixed the menu situation but thye still dont work. Furthermore I havent even begun to understand how to handle the labelling issue. pyqt's pixmap does not lend itself it any sort of image resizing, or editing. A custom pixmap class will probably be needed, as well as layering functionality so the labels can draw onto the image below it.

I discovered the widget I might be looking for. QSplitter. I beleive this will mimic napari's resizable windows, if so this would be the ideal widget to use. trying to implement it now though it keeps failing to compile so I'm not quite used to the changes it will require.

Image no longer loads, something about qsplitter isnt playing well with it.

## Day 8 6/6/2024
10:10 am - 3:25 pm

Having a tough time making progress today. I found some plugins other people have made and I'm reading thm to see how they do it. It's given me additional insights on package structuring and how multiple classes wirk with that. Layer data tuples also make more sense as passing info between plugins looks to be very important. A lot of other folks's plugins use libraries I am unfamiliar with such as Zarr so depending on what we're doing specifically that may be needed.

I'm not seeing much customization of napari's gui. I do see some impressive gui fields being added as well as pop up windows but if we need to edit the standard existing gui I may need to dig deeper.

Began work on a new plugin where I can experiement with the gui a bit. I used cookiecutter this time instead of making the base plugin manually. It has quirks but it might be good to use in the future due to its speed.

Began experiementing with a basic example gui editor. The gui makes sense enough, there are essentially 4 options when it comes to the gui. 1 Type pure python and let the built in autogenerate function make the gui around that. Its easy but I suspect not very accurate the more complex a function gets. In tandem with this or seperate (not entirely sure) magic factory allows some customization of these values while still keeping it simple. Then theres magic gui container which gives even more control and lastly pure qwidget widgets. The last being the most powerful but also the most finnecky. Unfortunately I still need more practice with these things, the prebuilt example only seems to lay a very small line of pixels down the screen rather than seeming to do anything meaningful. I need to figure out better how its actually interacting.

## Day 7 6/5/2024
9:40 am - 2:40 pm

Resolved the issues with my account and the timesheet.

Ran first successful hello world plugin in napari, it printed to the console after clicking a run button in napari. Now to understand better how to make more complex plugins.

Continued research into inner workings of napari. Learned a bunch about different contributions. One thing of note is napari may have moved gui functionality from pyqt to qt for python since the latter is open source. Theyre pretty similar but not the same. Its possible we wont be able to use pyqt but I'm still confirming that.

Nevermind they use qtpy which just has compatability for pyqt and pyside. Pyqt5 stuff should still work.

Began reading up on testing napari plugins. The recommended way is to use pytest in tandem with it. I need to review pytest as I only have a basic understanding of how to use it. Napari recommends testing most functions and methods directly rather than trying to actually test many gui elements since those are hard to test. I have a basic understanding of how plugins are made and how tests work, but I'm going to need some more practical experience to get the full hang of it.

## Day 6 6/4/2024
9:40 am - 3:01 pm

The start of my shift was occupied with some account issues I had to talk with arleen about.

I've spent most of the time since though trying to go over everything about napari I can. I have a bit on an idea how to make a new plugin now, but not deep understanding yet of how to expand beyond simpler plugins. So I decided to try to learn more about napari's built in classes and methods and such, which has been a bit confusing since I've only had the raw documentation to work on but otherwise its been ok. I think I may try to find a plugin so I can open it up and look at how their code is set up, it might help me wrap my head a little around how to use napari.utils and components and such.

I spent time reading up on everything to do with a simple hello world napari module. I started creating it, but I still need to run a few commands to test if its going to render the button correctly. Its tough not quite knowing what I'll need to know but I'm trying to keep a broad base and I'm writing down what a lot of things do on a high level so I can find them and dig deeper as needed.

Attempted to run my napari hello world plugin but it failed. Not sure what I could have done wrong given I followed the tutorial and most of it was simple or copy paste but I'll check each file again and see if I missed something. There may be a manual way to load it bit I want to check the tutorial steps first in case I missed something important.

## Day 5 6/3/2024

10:15 am - 3:17 pm

I have learned a great deal about napari's label class and how its used, as well as some more general info about napari and how it operates. The labels class is a subclass of the image class so learning more about the image class will be beneficial. It seems though these layers support numpy style image arrays which should make live image editing and analysis easy. The labels class will be really useful in any instance or semantic segmentation.

Learned how the layer class works. Its a base class that custom layer classes have to extend, this way its easier to make custom classes.

Learned a bunch about the Image Layer. Again it accepts most any numpy style data array. It also has some advanced functions to help with very large and complex images inclusing multiscale image support, some lazy loading support, and auto computing multiscale images as needed. 

Finished going over each of the layer types. It seems to me for this project we are probably using labels, and layer most, as well as image, points, and shapes. Surface renders 3-d objects which is nice, but given we're probably using one 2-d image or several layers of a 2-d images I dont know if we'll need any 3-d rendering. Tracks could get used maybe, but its focus is on projecting the paths of moving objects and applying trails if I understand correctly, which probably wont be of much use here. Vectors could get used, but shapes will probably be more versatile for the job at hand given vectors limitations and lack of interactivity with the gui. 

Next topic will probably be types, as well as looking at the source code of the layers since so far I only have a high level understanding of how theyre used. Edit: Scratch that next part I think will probably be code of layers and how to make plugins. The built in types seem pretty bare bones.


## Day 4 5/31/2024

10:40 am - 3:40pm (5 hours)

I've continued work on the demo application which has caused me to realize I needed more understanding with some widgets as well as slots and signals. With some of my new knowledge The sliders now have defined ranges and output numbers to connected functions. So far the functions dont do anything to the image but thats ok for now. I plan to change the image anyway since the current one is static, next is the file explorer to choose an image, then I need to change my image format so it can be edited.

I'm learning about toolbars and menus. So far Its not implemented but I'm working on it.

Learning about Dialogs now. Once I've learned Dialogs toolsbars, and menues I ought to be able to make a convincing toolbar for the demo app, though its more complicated than I thought it'd be.

Learned mostly how to handle custom dialogs (I'll need to review it), but I also learned about the prebuilt in dialogs which seem very easy and versatile at least for simple popups. More complex ones would be an issue till I've practiced.

## Day 3 
10:28 am - 2:37 pm (4hrs 9 mins)

began work on the demo app for the day. So far I have the controls rendering in, now I'm adding an image field and then adding some formatting.

Added an image and began learning how to alter and resize the image.

Learning about image processing with pyqt, its not as straightforward as I'd hoped.

## Day 2

9:50 am - 3:04pm (5 hrs 14 mins)

Learned how to use grid layouts.

Began first look at Napari to see how they use pyqt. Didnt learn too much however, will need to do some more research. EDIT: Did a bit more research. Modding Napari directly as I first thought probably wont work well, however there are some guides on making Napari plugins which might be better than a direct mod anyway. 

Made first hello world pyqt5 program, practicing now making a UI and having it interact with code.

Ok learned some more about pyqt5. Python projects need to be frozen to enable cross computer support. the pyqt creators recommend fbs for this task and the process is fairly simple. There will/may be issues between different OS's though so mac vs linux vs windows may have issues. Probably linux and mac will be the most compatable but windows devices are more common I reckon. Not sure how this would work with android.

Learned about slots and signals, aka how the pyqt buttons and other widgets actually run code in the background. Its fairly simple, very similar to web dev tech.

Learned about Styling. There are premade styles that can have their color pallets modified easily enough with built in tools. However for finer control there are also style sheets that act much like CSS style sheets. They give finer control but are less flexible so if the modified program we make is needed to look good on many different screen sizes then there may need to be lots of style sheet code.

Began coding a dummy napari UI. The plan is to have a look alike program by tomorrow that performs a similar function, if I can do that I reckon I'll have mastered enough of pyqt.

## Day 1
12:00pm-4:00pm (4 hours)


Set up pyQT5 on my computer and began learning pyQT5. Its a tool that lets you use QT5 with python (since QT5 is C++ based). QT5 is used to make GUI's. pyqt5 may be phased out soon in favor of a n official qt5 for python tool but they are very similar and pyqt5 is commonly used now. pyqt5 is used in napari so it still needs to be learned either way. 

qt designer may be useful in editing pyqt applications

to set up python and pyqt 5:
install python
make sure pip works
run: pip install PyQt5 (you may need python -m or py -m before the pip)

pyqt programs are built on 2 objects Q application and main window. The first handles events and initalization of modules aand is largely automatic. The main window does graphics and logic and is where most work is done.

the main window has graphical elements called widgets and has a bunch of built in widgets that are very similar to how html, css, and js widgets sort of work. Qwidget is an empty container used for formatting (like a flexbox I think) and other Qwidgetname widgets do toher things liek render buttons or text fields.

Learned how to make simple program with basic widgets, though non-functional

