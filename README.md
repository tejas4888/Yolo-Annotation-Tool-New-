# Yolo-Annotation-Tool-New

Put all images in the "images" folder under respective categorical folders.

Add all classes to "classes.txt" file.

Do steps:
```
run main.py
run check.py (this will remove redundant label files)
run process.py (note that images are written on valid.txt for validation set)
```

NOTE: If you use new annotation tool, please create classes.txt file and write all classes what you train the objects. Because I read the all classes from classes.txt.

The dataset is ready for yolo training.
