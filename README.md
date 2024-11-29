# Enhancing Wireless Capsule Endoscopy Images

## Description 
This repository contains the code and supplementary files for my research article titled "[Enhancing Wireless Capsule Endoscopy images from intense illumination specular reflections using the homomorphic filter]".

Online version (https://www.sciencedirect.com/science/article/abs/pii/S1746809423001568). 

## Introduction 

Wireless Capsule Endoscopy (WCE) is a non-invasive medical imaging device that gastroenterologists use to investigate gastrointestinal tract disorders. WCE images often suffer from specular reflections (SRs). SR is an outcome of the rigorous light and luminous regions emerging in WCE images, impacting the performance of abnormality detection approaches and physician analysis. The current study aims to invent a method that can automatically segment and eliminate SRs in WCE images to increase the accuracy of abnormality detection approaches and help physicians to make a potent diagnosis. In this study, we introduce a novel method for SR elimination with a negligible damage to the image texture using a homomorphic filter. The proposed method encompasses three steps. Initially, we utilize a robust segmentation technique using the U-Net model to segment SRs based on semantic segmentation. Then, we use the homomorphic filter to separate the illumination and reflection components. Damage caused by SR has different effects on these two components. Our proposed method enhances each of these components separately instead of enhancing the whole image uniformly. Eventually, we reconstruct SR regions using the Navier Stokes inpainting technique based on fluid dynamics. Our experiments were conducted on three different types of WCE datasets. The evaluations were performed with the following criteria accuracy, false negative rate, false positive rate, precision, recall, and F-Measure. The results show that our proposed method eliminates SRs admirably and quantitatively increases the accuracy of the stateof-the-art abnormality detection methods in WCE and improves their performance.

