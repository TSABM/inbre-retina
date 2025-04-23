# The Project
cell annotation projects are stored in a folder which bear the projects name. Inside the project folder there will be a json file named annotations and another folder named source. 

The annotations file contains a projects metadata as well as all the details regarding the boxes and contours generated in this application (or generated with other programs and imported into this project format). 

The source folder contains the reference image, video that the annotations apply to. 

## Source
The Source folder contains the reference image, or video to be viewed. Accepted formats are PNG, JPEG, JPG, and MP4.

## Annotations
The Annotations file is a json file that stores all the important project data primarily including the annotations (bounding boxes or cell contours) made by users or automated tools.

The files format echoes the structure of the LabelData class this application uses. The strucure generally follows the pattern: Metadata, Cells, CellTypes, Events, EventTypes, Frames. 

### Metadata
Primarily contains important information about the project. The fields it contains are shown below in the same order they appear in in the json annotations file. The format of each line is '"fieldName" : data type'. 
            "sourceName": string, //the name or path to the source file, note this may be changed in future versions to be a list
            "projectName" : string, //the name of the project, which is set by the app user
            "projectID" : integer, //the project ID, a number used to help identify the project even if the name changes
            "frameTotal": integer, //the number of frames in the projects image or video
            "maxWidth" : integer, //the width of a frame
            "maxHeight" : integer, //the height of a frame
            "largestID" : integer, //the largest frame or cell ID. used internally to help prevent duplicate ID's. -1 by default
            "other": list[string], //A temporary field likely to be removed soon added for testing and development purposes

### Cells
A dicitonary contianing each individual cell found in the entire project. Each item in "Cells" has two fields as defined below.
            "cellID" : integer, //cellID is a unique integer used to help differentiate different cells
            "cellType" : string //cellType is a non-unique string used to define a cells type or category

### CellTypes
A dicitonary containing each cell type found within the project.
Each cell type is just a string.

### Events
A dictionary containing each event found in the entire project. Each event contained within has the following fields.
            "eventID": integer, // a unique integer used to help differentiate different events from each other
            "eventType": string, // a non-unique string 
            "annotationIDs" : list[integer] // a list of the annotationIDs associated with an event
### EventTypes
A dicitonary containing each event type contained in the project.
Each event type is just a string.

### Frames
A dicitonary contianing each frame contained in the project. Each frame has the following fields:
            "projectID" : integer, // a unique integer used to identify what project the frame is a part of
            "frameID" : integer, //  a unique integer used to identify the frame provided by our annotation drawer. defaults to the same as frameNumber if not provided.
            "frameNumber" : integer, // an integer representing which frame in a video this object referrs to. It begins counting from 0
            "annotations": Annotation, //a dicitonary containing items of the custom type "annotation" which have all the details associated with bounding boxes and cell contours

#### Annotation
A type that defines the boxes, or cell contours and their associated details.
            "projectID" : integer, // the projects unique integer id
            "frameID" : integer, // the id of the frame the annotation is placed on
            "imageSource" : string, // the path to the image
            "annotationID" : integer, // a unique integer differentiating this annotation from any others.
            "frameNumber" : integer, // the number of the frame the annotation is placed on
            "annotationType" : string, // A string defining the type of annotation this is, particularly helpful to tell the program how to handle the points contained in the mask list. For now it will either be "Box" or "Contour"
            "mask": mask, // A list of points that define a box or cell contour. Boxes are defined by two corner points, contours are defined by an arbitrary number of points that closely follow the shape of a given cell.
            "cellId" : integer, // the integer that defines what cell in a frame the annotation applies to
            "cellType" : string, // a string that indicates what type of cell is being annotated
            "eventID" : integer, // an integer that indicates what event the annotation being associated with. It is -1 by default if the annotation does not define an event.
            "created_by": string | None, // the user name of the person who created the annotation. Usually None at this time because the current applciation does not have a logging in function but some external tools used in conjunction do
            "creationTimestamp": string, // a date in string form defining when the annotation was created
            "approved": boolean, // a boolean defining if the annotation has been verified. This field is mainly a leftover from an external tool we are using that needs this field.