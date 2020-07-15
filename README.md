# Public datasets preprocessing
## Segmentation 
- pascal-context.py: convert the mat format of annations (400 categoires) of PASCAL Context dataset into the png label (59 objects+1backgroubnd)
Note: the code is borrowed from [ZzzjzzZ](https://github.com/ZzzjzzZ/segmentation.data/blob/cf7b3e300621c57af507786062256d40012f2e49/convert_pascal_context.pyZzzjzzZ).
- Camvid.py: extract the 11 subset classes of total 32 classes. In particular， void pixel is represented by 255. 
