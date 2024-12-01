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
  The evaluation criteria utilized to evaluate the proposed method include accuracy (AC), false negative rate (FN Rate), false positive rate (FP Rate), precision, recall, and F-measure.
![image](https://github.com/user-attachments/assets/5d0fb1db-d74d-4bab-a519-93689dded560)
![image](https://github.com/user-attachments/assets/bcf1f076-b197-4447-b671-dd5bcbb13ab3)


