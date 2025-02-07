# The Project
cell annotation projects are stored in a folder which bear the projects name. Inside the project folder there will be a json file named annotations and another folder named source. 

The annotations file contains a projects metadata as well as all the details regarding the boxes and contours generated in this application (or generated with other programs and imported into this project format). 

The source folder contains the reference image, images, or video that the annotations apply to. 

## Source
The Source folder contains the reference image, images, or video that relate to the project. At this time accepted formats are gif, png, jpeg, and jpg. Furthermore multi frame annotations are at this time non functional (2/7/25)

## Annotations
The Annotations file is a json file that stores all the important project data primarily including the annotations (bounding boxes or cell contours) made by users or automated tools.

The files format echoes the structure of the LabelData class this application uses. The strucure generally follows the pattern shown below.

### Metadata
Primarily contains important information about the project such as the fields below.
            "sourceName": sourceName, //the name or path to the source file, note this may be changed in future versions to be a list
            "projectName" : projectName, //the name of the project, which is set by the app user
            "projectID" : projectID, //the project ID, a number used to help identify the project even if the name changes
            "frameTotal": frameTotal, //the number of frames in the projects image or video
            "maxWidth" : maxWidth, //the width of a frame
            "maxHeight" : maxHeight, //the height of a frame
            "largestID" : -1, //the largest frame or cell ID. used internally to help prevent duplicate ID's.
            "other": other, //A temporary field likely to be removed soon

### Cells

### CellTypes

### Events

### EventTypes

### Frames