

1.Dataset

In this project, I used a dataset called “android-ui-dataset”, which I downloaded from the Roboflow platform. The dataset includes screenshots from Android applications, and each image is labeled with bounding boxes showing different UI components like buttons, text fields, switches, and checkboxes. The labels follow the YOLO format, which means each text file includes the class number and the position of each element in the image.

The dataset was automatically organized into three parts: training, validation, and test sets. All the images were resized to 640×640 pixels so they could work properly with the YOLO model. Since the screenshots were taken from real Android apps, the dataset had lots of variation in layout and component styles.

2.The class list includes common Android components such as:

Button
TextView
ImageView
Switch
EditText
Checkbox

Thanks to this variety, the model was able to learn how to detect different types of UI elements from different layouts and screen designs.


3.Model Selection
For this task, I decided to use YOLOv11 because it is a fast and reliable object detection model. YOLO stands for "You Only Look Once", and version 11 is one of the newest and most improved versions. It was a good choice because it can detect multiple objects in real time, which is useful for this kind of interface analysis.

I started with a pretrained model (yolo11m.pt) and then fine-tuned it using my own dataset. This helped the model learn faster and perform better since it already had some knowledge from previous training on general data.

4.During training, I used the following settings:

200 training epochs
Batch size of 16
Image size: 640 × 640
Training on GPU (CUDA)
Early stopping after 10 epochs with no improvement

The model stopped early at epoch 85, because there was no improvement for 10 consecutive epochs. The best performance was reached at epoch 75 and saved accordingly.
