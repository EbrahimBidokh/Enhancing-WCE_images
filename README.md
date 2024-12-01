# Enhancing Wireless Capsule Endoscopy Images

## Description 
This repository contains the code and supplementary files, as well as a brief explanation for my research article titled "Enhancing Wireless Capsule Endoscopy images from intense illumination specular reflections using the homomorphic filter".

The full version is available online on (https://www.sciencedirect.com/science/article/abs/pii/S1746809423001568). 

## Abstract 

Wireless Capsule Endoscopy (WCE) is a non-invasive medical imaging device that gastroenterologists use to investigate gastrointestinal tract disorders. WCE images often suffer from specular reflections (SRs). SR is an outcome of the rigorous light and luminous regions emerging in WCE images, impacting the performance of abnormality detection approaches and physician analysis. The current study aims to invent a method that can automatically segment and eliminate SRs in WCE images to increase the accuracy of abnormality detection approaches and help physicians to make a potent diagnosis. In this study, we introduce a novel method for SR elimination with a negligible damage to the image texture using a homomorphic filter. The proposed method encompasses three steps. Initially, we utilize a robust segmentation technique using the U-Net model to segment SRs based on semantic segmentation. Then, we use the homomorphic filter to separate the illumination and reflection components. Damage caused by SR has different effects on these two components. Our proposed method enhances each of these components separately instead of enhancing the whole image uniformly. Eventually, we reconstruct SR regions using the Navier Stokes inpainting technique based on fluid dynamics. Our experiments were conducted on three different types of WCE datasets. The evaluations were performed with the following criteria accuracy, false negative rate, false positive rate, precision, recall, and F-Measure. The results show that our proposed method eliminates SRs admirably and quantitatively increases the accuracy of the stateof-the-art abnormality detection methods in WCE and improves their performance.

## Contributions and novelties 
• Proposing an approach for the elimination of SR from WCE images with minimal damage to the inherent information of the image using homomorphic filter.<br />
• A U-Net model based on binary semantic segmentation is proposed to segment SR in WCE images. This model only focuses on the SR pixels, not the other pixels in the image.<br />
• A Navier-Stokes inpainting technique is used to reconstruct the SR regions. The proposed technique reconstructs the SR region by selecting the most well-suited value from adjacent pixels.<br />

## Material and method
This part consists of three parts:
### Proposed U-Net structure for SR segmentation:
We utilize RGB images with 256 × 256 pixels for the proposed model input. Since the proposed model provides a binary mask, the input and output sizes of the model must be the same. Accordingly, the model’s output produces a single-channel image with 256 × 256 pixels. The network architecture is demonstrated at the end of this paragraph. We established four convolution blocks (CONV) in each encoder and decoder path for our UNet model. The encoder blocks involve two 3 × 3 CONV layers, and each CONV layer is followed by batch normalization and rectified linear unit (ReLU) activation layer. There is a 2 × 2 max-pooling layer with stride 2 for down-sampling after each CONV block. The number of feature maps is doubled at each down-sampling stage. The bottleneck layer uses two 3 × 3 CONV layers followed by a 2 × 2 up-convolution layer. Each block includes two 3 × 3 CONV layers in the decoder path that receives input. There is a concatenation with corresponding block feature maps in the encoder path, which is appended as input to each decoder block. After each block, a 2 × 2 up-convolution layer is used for up-sampling and halving the feature map. At the last layer, a 1 × 1 convolution layer with a sigmoid activation is utilized for mapping every 64-component feature vector to the intended number of classes. Eventually, a threshold will be applied to convert the image to a binary mask.<br /> The U-Net implemented code is available in this repository "model.py"

The proposed U-Net architecture for SR segmentation.
![image](https://github.com/user-attachments/assets/01f22b3e-dfab-49d3-b086-cc74d0810040)

### Homomorphic filtering:
When an image is captured, pixels of the image are often affected by two prevalent cases called ambient light and light reflected by the object. The ambient light constitutes the illumination component, and the light reflected by objects constitutes the reflection component of an image. Therefore, each image is constituted of two illumination and reflection components. Image damages stemming from the SR can possess different effects on these two components. For this reason, we separate these two components by applying the homomorphic filter and then enhance them separately by using the inpainting technique.<be /> You can find the code for the homomorphic filter in this repository "homo.py".

### Homomorphic filtering:
In this section, we use the inpainting technique based on NavierStokes to reconstruct the SR areas. This algorithm is based on fluid dy­namics and utilizes Partial Differential Equations (PDEs). This algorithm causes the image Laplacian in the isophotes (stage lines) orientation to spread and resolves the image intensity’s smoothing gradient in the stage-lines direction. For example, the algorithm first moves along the edges from known to unknown areas (since edges are continuous). It also continues isophotes while adapting gradient vectors at the boundary of the inpainting area. Hence, the resulting design is a discontinuous esti­mation of the PDE (for more information read the full version).

Block diagram of the proposed method.
![image](https://github.com/user-attachments/assets/b704c579-1b1c-4d81-ac45-125e575fdc7c)

#### Evaluation criteria 
  The evaluation criteria utilized to evaluate the proposed method include accuracy (AC), false negative rate (FN Rate), false positive rate (FP Rate), precision, recall, and F-measure.<br />
![image](https://github.com/user-attachments/assets/5d0fb1db-d74d-4bab-a519-93689dded560)
![image](https://github.com/user-attachments/assets/bcf1f076-b197-4447-b671-dd5bcbb13ab3)

#### Qualitative results
In this section, the experimental results of the proposed method will be visually explored on a couple of WCE images. Apart from SR, there are other challenges in WCE images, including bubbles, shadows, and floating substances in the gastrointestinal tract. We revealed the quali­tative results of applying our proposed method on a number of WCE images in the figure below. In the figure below (a) refers to the input images that contain SR, and (b) shows the enhanced images using our proposed method. It can be clearly seen that our proposed method specifically focuses on SRs and is able to eliminate them satisfactorily even in the presence of bubbles and white textures, and it can preserve the image’s texture, structure, and information.

![image](https://github.com/user-attachments/assets/d49d002a-c8a1-42f0-acbb-ae77fb1bb15c)


#### Quantitative results
To further evaluate the performance of our proposed method, we employ it as a pre-processor for Amiri_1 and Amiri_2’s approaches. Amiri_1 has introduced an approach to detect abnormalities such as angiodysplasia, ulcer, bleeding, lymphoid hyperplasia, and polyp in WCE images. This approach uses a joint-normal distribution to highlight distinct areas and disregard non-distinct areas for abnormality detec­ tion. This approach extracts appropriate features associated with the color, texture, and shape of the region of interest. Eventually, the feature set will be used to classify the region as abnormal or normal using the support vector machine. Amiri_2 was introduced to detect abnormal­ ities, including bleeding and angiodysplasia, in WCE images. This method specifies potential regions of interest by utilizing an image segmentation algorithm based on expectation–maximization, then uses a composition of color histogram analysis and statistical features to classify images into normal and abnormal using a multi-layer perception.<br />

We first evaluate Amiri_1’s method on the Kvasir-Capsule dataset before and after applying our pre-processing method. The re­sults are shown in the table below. It is obvious that our pre-processing improves the method in all measures, especially the accuracy, which has increased from 97.6% to 98.8%. The FN Rate and the Recall are two important measures for abnormality detection approaches because improving these measures enhances their performance. Our proposed method has significantly improved these two measures as in others.<br />

![image](https://github.com/user-attachments/assets/57657569-af66-42ba-8b03-89e62a278477)

Similarly, we next evaluate the performance of Amiri_2’s method before and after employing our pre-processing method. The dataset used in Amiri_2’s method is shown in Table (a) is shown below. The results of this experiment are demonstrated in Table (b). It is evident that our proposed method enhanced Amiri_2’s method per measure, particularly the accuracy which has been raised from 96.7% to 97.2%.<br />

Table a<br />
![image](https://github.com/user-attachments/assets/6938d066-b941-4c01-b790-9dbe3edc056a)

Table b
![image](https://github.com/user-attachments/assets/7a8dd266-7b53-47cb-988d-2a74fd44bde5)


In this paper, a novel method using HF for SR elimination from WCE images was proposed. In the proposed method, at first, a powerful se­ mantic segmentation method utilizing the U-Net model is used for automatic SR segmentation. Then, the illumination and reflection components of the images were separated using the HF. We observed that the destruction of SR may not be the same in the illumination and reflection components. For this reason, the damaged areas in each component were separately reconstructed by using the Navier-Stokes inpainting technique. This approach minimizes the destruction effect on the image texture. Although the inpainting technique has recon­ structed the areas damaged by SR satisfactorily, but this technique ig­nores the intrinsic information of the image. That is why, in cases where the SR area in the image is extensive, it may not have acceptable per­formance in the reconstruction of that area. We evaluated the perfor­mance of the proposed method with the criteria of accuracy, FNR, FPR, precision, recall, and F-Measure and conducted it on two datasets. The results indicated that our proposed method has a satisfactory result in terms of quality and has eliminated SR well. In addition, our proposed method improved the performance of abnormality detection methods and increased their accuracy from 97.6% to 98.8% and 96.7% to 97.2%, respectively.

Note: The code for this research has been implemented and placed in this repository. To run the code, open the main.py file and run it.<br />
Note: The weights obtained from training the U-Net model for specular reflection segmentation are not in this repository. If you need them, email ebrahim.bidokh1@gmail.com.<br />
Note: Several types of datasets were used in this research. Read the full version of this research and if you need the datasets, email ebrahim.bidokh1@gmail.com.
