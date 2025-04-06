**INBRE-retina Design Document**

# Intent

The intent of this application is to make it possible for people (and potential future algorithm based extensions) to identify and label cells found within multidimensional videos of fish retinas. The exact details of the video formats and exact preferences/needs are still unknown but for now video viewing, basic labeling functions, and import and export capabilities are needed.

# Class descriptions

Main:  
Initializes the master memory and begins generating the views which will govern the UI.

## Views:

MainWindowView: A class for rendering the main window and its contents. Extends qtw.QMainWindow. Contains the MainWindowMenuBar view and the CenterBox view.

WindowMenuBarView: A class for rendering the menubar for the main window. Currently most buttons are placeholders. Should provide UI options to the user such as “Open file”, “Export Labels”, “Import Labels”, “Settings” etc.

CenterBox: A container for other views to be rendered within the greater main window. Sets some basic layout settings and contains ControlAreaView and MediaAreaView.

ControlsAreaView: A container for the different controls the user may need to view and manipulate the labels on the canvas. Contains MainControlView, and LabelDataView.

MainControlsView: Contains most controls the user will need to interact with the loaded project data or the canvas. Contains video playback controls, as well as a field to view the loaded in label data.

LabelDataView: A textbox to show the currently loaded project data for review before saving or exporting

MediaAreaView: Likely unnecessary code. Serves as a container for CanvasView and nothing else at this time, though it does set some layout rules. May also contain video controls in the future.

CanvasView: extends QGraphicsView and serves to both render the current image but also receives user input when selecting a bounding box or drawing a new one. Data for drawing new bounding boxes originates from here. Also instantiates LabelPopup though that may change.

LabelPopup: possibly unnecessary code and currently in need of refactoring. The intended purpose was to make it so when a user drew a new bounding box for a label a popup would appear with fields the user could fill in with all needed data for the label. (i.e. what cell(s) are included in the bounding box, what event(s) are included, wether these are the first instances of a cell or event, etc.)

## Presenters:

AbstractPresenter: Defines some minimum requirements for other presenters such as requiring a view class gets defined. Also provides a getView method.

CanvasPresenter: Facilitates communication between the canvas view the user interacts with and the canvas model which actually holds the image data and accesses the label data.

LabelDataPresenter: Facilitates communication between the possibly unneeded label data view fields and the LabelData object which holds all relevant Label data for the file.

MainControlsPresenter: Facilitates communication between the main controls and master memory. At this time only sets the users interaction mode. This code may need refactoring.

WindowMenuBarPresenter:Facilitates communication between the MenuBars view and its model. 

## Models:

MasterMemory: A class that holds essential application data as class wide variables to ensure all other classes can access up to data data. Holds such data as the labels that apply to the given file, the current canvas, and the current user interaction mode.

LabelData: A class which defines how frame data, bounding box data, cell data, event data, type data, and file metadata are stored. Everything at the moment is stored as dictionaries or lists in the hope of making exporting the data easier.  
LabelExporter: Does nothing yet. Intended to be a class which takes Label Data from master memory and encodes it in JSON (or whatever other format the project desires). The exporter then saves the data on the computer so it can be used later.

ProjectOpener: Opens a given project if the given project meets the specs.

WindowMenuBarModel: The model for the main views menubar. Receives user inputs to interact with the label data, changes settings, etc. 

Displayable: A parent class, all compatable formats with the canvas and app logic will be children of this class.

SimpleMovie: Extends displayable. Accepts GIF, MNG, and APNG formats and allows for extracting individual frames as pixmaps.

StandardImage: Opens single images of accepted formats

SimpleVideo: extends displayable. Accepts mp4's. Handles stepping frames, jumping to frames, playing and pausing.

Frame: extends dictionary. Contains data for all annotationIDs and eventIDs associated with the frame.

Annotation: contains individual annotation details. Such as what cell is being annotated, what event(s) are assotiated, and the annotation mask details (a list of points)

Cell: extends dictionary. Contains all data for a cell including the cellId and cellType.

Event:extends dictionary. Contains all data for an event including eventID, eventType, and associated boxIDs.

MetaData: Contains metadata for the project, mostly details about the image/video source.