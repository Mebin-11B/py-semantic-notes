---
title: "YOLO26: YOLO Model for Real-Time Vision AI"
url: https://blog.roboflow.com/yolo26/
clipped: 2026-08-31 12:26:32
source: "Web Clipper"
tags:
  - web-clipper
  - clipping
---

# [YOLO26: YOLO Model for Real-Time Vision AI](https://blog.roboflow.com/yolo26/)

## Full Article

[Sign in](https://app.roboflow.com)
        [Book a demo](https://roboflow.com/sales)
        [Get Started](https://app.roboflow.com/login)
      
      
        
        
          
            
          
          
            
          
        
      
    
  

        
            
  
    
      
        [Blog](https://blog.roboflow.com)
        

# What Is YOLO26? An Introduction

      
    
  

  
    
       
          
          
    
    
    
    
    
    

          
            

              
                    
                      
                      
                    
              

              
                [Erik Kokalj](https://blog.roboflow.com/author/erik/)
                Published
                  Jan 14, 2026
                  •
                  6 min read
                
              
            
          

          
            
            
                
                    
                        SUMMARY
                    
                
            
            
                
                
                    
                    
                        
                            YOLO26 is the January 2026 generation of the YOLO family: an edge-optimized, NMS-free multi-task model covering detection, segmentation, classification, pose, and oriented bounding boxes, with up to 43% faster CPU inference than YOLO11 across five sizes from Nano to Extra Large. It ships under AGPL-3.0 and trains and deploys in Roboflow alongside RF-DETR, which outperforms it on accuracy and domain transfer under a commercially permissive Apache 2.0 license.
                        
                    
                    
                    
                
            
        

[YOLO models](https://blog.roboflow.com/guide-to-yolo-models/) are a family of real-time [computer vision models](https://playground.roboflow.com/models?ref=blog.roboflow.com) covering object detection, segmentation, pose estimation, classification, and oriented object detection. Their combination of speed and accuracy has made them a fixture on edge devices and in cloud APIs alike.

In this post, we examine YOLO26, released [January 2026](https://github.com/ultralytics/ultralytics?ref=blog.roboflow.com): its key improvements, its benchmarks, how it compares to other leading computer vision models, and how to train and deploy it.💡Roboflow supports YOLO26 end to end: label data, [train YOLO26 in your browser](https://blog.roboflow.com/yolo26-in-roboflow/) on hosted GPUs, and deploy to an API or edge device. [Start free](https://app.roboflow.com/login?ref=blog.roboflow.com).

## What Is YOLO26?

YOLO26 is a multi-task model family designed to handle a broad range of computer vision tasks, including object detection, instance segmentation, image classification, pose estimation, and oriented object detection. The lineup features multiple size variants Nano (N), Small (S), Medium (M), Large (L), and Extra Large (X) to cater to different performance and deployment needs.

Compared to previous YOLO generations, YOLO26 is optimized for edge deployment, featuring faster CPU inference, a more compact model design, and a simplified architecture for improved compatibility across diverse hardware environments. Notable improvements include decreased latency by removing NMS and results staying consistent in fp16 and fp32, making it possible to run the model in an optimized, low-latency way and get the same high accuracy you saw during training.

## Try YOLO26 on Images

See how YOLO26 performs on images for common objects included in the [COCO dataset](https://universe.roboflow.com/microsoft/coco?ref=blog.roboflow.com). Test out how the model handles your data below.

To compare YOLO26 against RF-DETR, SAM 3, and other models side by side on your own images, use [Roboflow Model Playground](https://playground.roboflow.com/?ref=blog.roboflow.com).

## Download YOLO26

The table below links the object detection checkpoints and shows reported benchmarks across sizes:

Modelsize(pixels)mAPval50-95SpeedCPU ONNX(ms)SpeedT4 TensorRT10(ms)params(M)FLOPs(B)[YOLO26n](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt?ref=blog.roboflow.com)64040.938.9 ± 0.71.7 ± 0.02.45.4[YOLO26s](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26s.pt?ref=blog.roboflow.com)64048.687.2 ± 0.92.5 ± 0.09.520.7[YOLO26m](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26m.pt?ref=blog.roboflow.com)64053.1220.0 ± 1.44.7 ± 0.120.468.2[YOLO26l](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26l.pt?ref=blog.roboflow.com)64055.0286.2 ± 2.06.2 ± 0.224.886.4[YOLO26x](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26x.pt?ref=blog.roboflow.com)64057.5525.8 ± 4.011.8 ± 0.255.7193.9

The tradeoff runs from Nano's 1.7 ms T4 latency to Extra Large's 57.5 mAP. For other task types, see the [YOLO26 GitHub](https://github.com/ultralytics/ultralytics?tab=readme-ov-file&ref=blog.roboflow.com#-models).💡You do not need to download weights to use YOLO26 on your own data: create a free [Roboflow](https://app.roboflow.com/login?ref=blog.roboflow.com) project, label your images with Auto Label, and train YOLO26 with Custom Training, no GPU or local environment required.

## YOLO26 Architecture

YOLO26 introduces several major improvements including:
- Broader Device Support: It removes the Distribution Focal Loss (DFL) module, simplifying inference, enabling multiple export formats ([TFLite](https://blog.roboflow.com/how-to-train-a-tensorflow-lite-object-detection-model/), [CoreML](https://blog.roboflow.com/what-is-coreml/), [OpenVINO](https://blog.roboflow.com/what-is-openvino/), [TensorRT](https://blog.roboflow.com/what-is-tensorrt/), and [ONNX](https://blog.roboflow.com/what-is-onnx/)), and broadening support for edge and low-power devices.
- Enhanced Small-Object Recognition: It utilizes the ProgLoss and STAL loss functions, improving detection accuracy, particularly for small objects, and providing significant advantages for IoT, robotics, and aerial imagery applications.
- End-to-End Predictions: It eliminates [Non-Maximum Suppression (NMS)](https://blog.roboflow.com/how-to-code-non-maximum-suppression-nms-in-plain-numpy/) as a post-processing step, producing predictions directly to reduce latency and make deployment in real-world systems faster, lighter, and more reliable.
- Faster CPU Inference: Optimizations in model design and training make YOLO26 faster on CPUs compared to YOLO11. For instance, the YOLO26-N variant delivers up to 43% faster CPU inference than the YOLO11-N, making YOLO26 ideal for real-time performance on devices without a GPU.
- Improved Training: It introduces the MuSGD optimizer, a hybrid of [SGD](https://docs.pytorch.org/docs/stable/generated/torch.optim.SGD.html?ref=blog.roboflow.com) and [Muon](https://arxiv.org/abs/2502.16982?ref=blog.roboflow.com) inspired by [Kimi K2](https://moonshotai.github.io/Kimi-K2/?ref=blog.roboflow.com) LLM breakthroughs, ensuring stable training and faster convergence by transferring optimization advances from large language models to computer vision.⚡RF-DETR Neural Architecture Search (NAS) is faster and more accurate than YOLO26: it trains multiple configurations on your dataset and recommends the best accuracy-latency fit. Read the [blog post](https://blog.roboflow.com/train-with-neural-architecture-search/) or [try it on your data](https://app.roboflow.com/login?ref=blog.roboflow.com).

## Can I Use YOLO26 Commercially?

YOLO26 ships under the [AGPL-3.0 license](https://blog.roboflow.com/why-agpl-3-0-is-a-risk-for-computer-vision-teams/), which requires open-sourcing derivative works unless you hold a commercial license. A Roboflow Enterprise license includes a pass-through license for commercial YOLO use with [Roboflow Inference](https://github.com/roboflow/inference?ref=blog.roboflow.com) ([talk to sales](https://roboflow.com/sales?ref=blog.roboflow.com)), or train [RF-DETR](https://playground.roboflow.com/models/roboflow/rf-detr?ref=blog.roboflow.com), whose core models and code are Apache 2.0, with no copyleft obligations and nothing to purchase.

## Use YOLO26 in Roboflow

YOLO26 is a [fully supported model in Roboflow](https://docs.roboflow.com/models/supported-models?ref=blog.roboflow.com) for object detection, instance segmentation, and keypoint detection: train it with Custom Training on hosted GPUs, upload externally trained weights, export weights, and deploy through the Serverless Hosted API, [Roboflow Workflows](https://roboflow.com/workflows/build?ref=blog.roboflow.com), or on-device with Roboflow Inference. The full loop, labeling with Auto Label through deployment, runs in one platform; see [YOLO26 in Roboflow](https://blog.roboflow.com/yolo26-in-roboflow/) for the walkthrough.

### YOLO26 Monocular Depth Estimation (YOLO-Depth)

Beyond detection, segmentation, classification, pose, and OBB, YOLO26 supports a sixth task: [monocular depth estimation](https://blog.roboflow.com/what-is-yolo-depth/). Given a single RGB image, the YOLO26-depth models predict a dense depth map, a float tensor aligned to the input resolution where every pixel holds an estimated distance in meters from the camera.

Modeldelta1abs_relRMSEParamsFLOPsYOLO26n-depth0.8820.1090.414m6.4M46.9BYOLO26s-depth0.8960.1040.399m13.2M67.9BYOLO26m-depth0.9210.0890.364m23.3M130.7BYOLO26l-depth0.9300.0830.351m27.7M157.2BYOLO26x-depth0.9330.0800.344m57.0M302.0B

Benchmarks are reported at 768px on the NYU Depth V2 Eigen test split with test-time augmentation, so expect somewhat lower accuracy in single-pass production inference, and note that NYU is an indoor benchmark. The output is metric depth, not relative depth.

For per-object distance in production today, you can pair RF-DETR detections with the [Depth Estimation block](https://docs.roboflow.com/workflows/blocks/blocks/run-a-model/depth-estimation?ref=blog.roboflow.com) in Roboflow Workflows.

## YOLO26 Alternatives

Several multi-task models compete with YOLO26 and are benchmarked with open code on the [object detection leaderboard](https://leaderboard.roboflow.com/?ref=blog.roboflow.com).

### RF-DETR

[RF-DETR](https://playground.roboflow.com/models/roboflow/rf-detr?ref=blog.roboflow.com), developed by [Roboflow](https://roboflow.com/?ref=blog.roboflow.com), is a family of real-time detection transformers supporting object detection, segmentation, and keypoint tasks. RF-DETR outperforms YOLO26 across benchmarks, generalizes better across domains (it leads [RF100-VL](https://rf100-vl.org/?ref=blog.roboflow.com), the real-world transfer benchmark), runs on the edge with [Inference](https://inference.roboflow.com/?ref=blog.roboflow.com), and ships under Apache 2.0.

For new detection projects, it is the model we recommend, and it trains in the same Roboflow flow as YOLO26, so comparing the two on your dataset is an architecture dropdown, not a platform change.

### LW-DETR

Light-Weight Detection Transformer (LW-DETR), released June 2024, combines a [Vision Transformer](https://roboflow.com/model/vision-transformer?ref=blog.roboflow.com) with the [DETR decoder](https://roboflow.com/model/detr?ref=blog.roboflow.com), integrating multi-level feature representations for accurate, robust predictions that outperform [YOLO11](https://playground.roboflow.com/models/ultralytics/yolo11?ref=blog.roboflow.com) on both accuracy and speed.

### D-FINE

[D-FINE](https://roboflow.com/model/d-fine?ref=blog.roboflow.com), released October 2024, introduces Fine-grained Distribution Refinement (FDR), iteratively refining bounding box distributions for greater localization precision, particularly on small or overlapping objects, while preserving real-time performance.

### YOLO26 Paper

As of June 2026, there is a [YOLO26 paper](https://arxiv.org/abs/2606.03748?ref=blog.roboflow.com) "Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models". YOLO26 ditches two long-standing bottlenecks: non-maximum suppression and Distribution Focal Loss.

New training tricks (the MuSGD optimizer, Progressive Loss, and STAL label assignment) improve accuracy, including on small objects. One pipeline handles detection, segmentation, pose, classification, and oriented detection across five scales, plus an open-vocabulary YOLOE-26 extension.

It reports 40.9–57.5 mAP on COCO at 1.7–11.8 ms T4 latency, pushing the accuracy-latency Pareto front past prior real-time YOLO detectors.

## Get Started with YOLO26

Try YOLO26 in the embed above, then put a model to work on your own data: [create a free Roboflow account](https://app.roboflow.com/login?ref=blog.roboflow.com), label a dataset, and train YOLO26 and RF-DETR back to back to see which wins on your images.

Read more:
- [YOLO27](https://blog.roboflow.com/what-is-yolo27/): expected at YOLO Vision 2026 in Shenzhen, expands the YOLO family into 3D perception with two models
- [YOLO-Depth](https://yolodepth.com/?ref=blog.roboflow.com): monocular depth estimation from a single camera
- [YOLO-StereoDepth](https://yolostereodepth.com/?ref=blog.roboflow.com): binocular disparity depth for robotics, positioned as a camera-native alternative to lidar
- [Training a YOLO model](https://blog.roboflow.com/yolo-training/): a walk through of how to train YOLO models in Roboflow

            
              
            

            
  

### Cite this Post

  

Use the following entry to cite this post in your research:
  

[Erik Kokalj](https://blog.roboflow.com/author/erik/). (Jan 14, 2026).
      What Is YOLO26? An Introduction. Roboflow Blog: https://blog.roboflow.com/yolo26/

            
  

### Written by

    
      
          
          
      
      
        Erik Kokalj
        Developer Experience @ Roboflow
      
      
        [View more posts](https://blog.roboflow.com/author/erik/)
      
    

              
    
      

### Topics

        
            
- 
              [Computer Vision](https://blog.roboflow.com/tag/computer-vision/)
            
        
    
  
          
        

        

      
    
  

  
  
    
      

## More About
        Computer Vision

      [View All Computer Vision Posts](https://blog.roboflow.com/tag/computer-vision/)
    
    
            
                

### 

[How to Build an Autonomous Defect Detector with Physical AI
                    Aug 28, 2026
                      •
                      7 min read](https://blog.roboflow.com/how-to-build-an-autonomous-defect-detector-with-physical-ai/)
                

### 

[Roboflow Playground: Try and Compare 130+ Computer Vision Models
                    Aug 27, 2026
                      •
                      7 min read](https://blog.roboflow.com/roboflow-playground/)
                

### 

[Robotics Perception Stacks: How Robots Understand Their Environment
                    Aug 26, 2026
                      •
                      7 min read](https://blog.roboflow.com/robotics-perception-stacks/)
                

### 

[How to Measure Volume with Computer Vision
                    Aug 24, 2026
                      •
                      12 min read](https://blog.roboflow.com/how-to-measure-volume-with-computer-vision/)
                

### 

[Building a Physical AI that Plays Connect 4
                    Aug 21, 2026
                      •
                      5 min read](https://blog.roboflow.com/building-a-physical-ai-that-plays-connect-4/)
                

### 

[Announcing the Visual Intelligence Summit
                    Aug 19, 2026
                      •
                      1 min read](https://blog.roboflow.com/visual-intelligence-summit-2026/)
