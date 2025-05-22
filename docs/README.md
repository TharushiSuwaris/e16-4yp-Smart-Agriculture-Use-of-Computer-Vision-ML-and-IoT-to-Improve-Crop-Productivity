

# Smart Agriculture : Use of Computer Vision, ML and IoT to Improve Crop Productivity

#### Team

- E/16/364, Tharushi Suwaris, [email](e16364@eng.pdn.ac.lk)
- E/16/173, Dumindu Karunarathne, [email](e16173@eng.pdn.ac.lk)
- E/16/127, Yoshith Harshana, [email](e16127@eng.pdn.ac.lk)

#### Supervisors

- Dr. Asitha Bandaranayake, [email](asithab@eng.pdn.ac.lk)
- Prof. Roshan Ragel, [email](roshanr@eng.pdn.ac.lk)
- Prof. Pradeepa Bandaranayake, [email](agbc@pdn.ac.lk)
- Dr. Prabhath Gunathilake, [email](prabhathg@sci.pdn.ac.lk)

#### Table of content

1. [Abstract](#abstract)
2. [Related works](#related-works)
3. [Methodology](#methodology)
4. [Experiment Setup and Implementation](#experiment-setup-and-implementation)
5. [Results and Analysis](#results-and-analysis)
6. [Conclusion](#conclusion)
7. [Publications](#publications)
8. [Links](#links)
9. [Summary](#summary)
---


## Abstract
Agriculture is the main source of the world's food supply. It has been the backbone of civilizations for thousands of years. During recent decades, the focus of agriculture has shifted to producing crops in more controlled and optimal environments in order to increase the quality and quantity of the yield at lower costs to fulfill the massive food requirements of a continuously growing population. Modern smart greenhouses are buildings that are equipped with the latest IoT devices, environment control and monitoring systems and automated irrigation and fertilizer systems to provide optimal growth conditions for crops. The latest trend in smart agriculture is to incorporate computer vision and machine learning (ML) capabilities to predict and optimize existing cropping systems to maximize productivity. The research focus on reduce the harm cased by different diseased by introducing disease/anomaly detection and identification so that the earlies and the necessary actions can be taken.

## Related works
- 0S. Poornima, S. Kavitha, S. Mohanavalli, N. Sripriya (2019) Detection and classification of diseases in plants using image processing and machine learning techniques, AIP Conference Proceedings 2095, 030018 (2019)
- Rahman, Hidayat Ch, Manzoor N.J. , Najeeb S., Siddique F., Khan Y. M., Alam R. A. (2017) comparative analysis of machine learning approaches for plant disease identification, Advancements in Life Sciences, 4-4 120-126
- Sequeira, R., Sebastian, R., Bunde, Y., Suryawanshi, U.,(2014)  International Journal of Science, Environment and Technology, Vol. 3, No 6, 2014, 2258 – 2268
- Singh V. , Misra A.K. (2016) Detection of plant leaf diseases using image segmentation and soft computing techniques, Information Processing In Agriculture 4 (2017) 41–49
- Barbedo J. G. A. , Koenigkana L. V. , Santos T. T. Identifying multiple plant diseases using digital image processing, Biosystems Engineering 147, July 2016, 104-116

## Methodology
By using computer vision techniques, solutions to address the following scenarios are to be done
- Develop a disease detection system by analyzing the aerial data of the plant considering the phentyping characteristics
- Develop a disease identification system by analysing the plant leaves separately by analyzing the features of the disease classes and develop a mobile application to be used the field.

Apart form these main objectives, it is planned to observe some of the exsisting models performance on the system and to develop a local dataset.

## Experiment Setup and Implementation

- Used tools such as Tensorflow 2, Numpy, Keras, CV2, Matplotlib, PIL
- Models - Inception V3, Mask RCNN, CNN, UNET

Data collection
- Cameras : ZED, Smartphone 16MP

The aerial data was collected using both the cameras, and the amount is 500 and 300 each. Plant leaves data were gathered with smartphone which included 400 images and those images were categorized after running sample tests in Horticultural Crop Reseasech and Development institute in Peradeniya. Then in order to develop more accurate solutions in the preprocessing phase, color calibration with backgroud removal was done alog with the annotation and categorisation of the data.

## Results and Analysis
Disease Identification
- CNN model accuracy: 87.5%
- Inception V3 model accuracy : 80%

Disease Detection
- Mask Rcnn Model : 52% (ZED), 58%(Smartphone)

## Conclusion
In conclusion, the custom CNN model which was developed from scratch gave the best results that can be applied to the real world application that is being developed, considering the disease identification phase.  
Considering the disease detection phase, it leave the question of the robustuness due to the only anased feature was color variation and upto the depth the solution is useful in a real wolrd system. As a begining of this kind of an apprach, it was possible to achieve more that 50% of accuracy, and this can be further improved in future research. 

## Publications
Abstract published in Perdeniya University International Research Sessions (iPURSE 2023).

[Conference Proceedings - Volume 24, Page 252](https://site.pdn.ac.lk/ipurse/2023/docs/iPURSE%20Proceedings%202023.pdf) 

<!-- 1. [Semester 7 report](./) -->
<!-- 2. [Semester 7 slides](./) -->
<!-- 3. [Semester 8 report](./) -->
<!-- 4. [Semester 8 slides](./) -->
<!-- 5. Author 1, Author 2 and Author 3 "Research paper title" (2021). [PDF](./). -->


## Links

[//]: # ( NOTE: EDIT THIS LINKS WITH YOUR REPO DETAILS )

- [Project Repository](https://github.com/cepdnaclk/repository-name)
- [Project Page](https://cepdnaclk.github.io/repository-name)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

[//]: # "Please refer this to learn more about Markdown syntax"
[//]: # "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"

## Summary

The research was conducted aiming to introdude computer vision, machine learning techniques to develop a smart agricultural system, and addressing this concept, two approaches were taken to adrress the issue of avoiding/reducing the threat of diseases to improve the quality and the quantity of the yield. the main objective was to develop a disease detection system with the use of aerial images analysing the phenotying characteristics of plants. This was done with a help of a mask RCNN model which we could obtain a result of accuracy 52-28% based on the dataset used. Other approach was to develop a disease identification system which has the ability to identify 3 disease classes in this research. For this apprach the existing inception v3 model was observed with its performance and a custom CNN was developed from scratch which resulted the best performance in comparison which is 87.5% if accuracy. The models gave considerably satisfying results and they are further to be improved ot be used in real world applications.  
