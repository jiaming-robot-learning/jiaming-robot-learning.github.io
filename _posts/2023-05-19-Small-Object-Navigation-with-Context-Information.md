---
title: Small Object Navigation with Context Information
date: 2023-05-19 12:13:36 +0800
categories: [research]
tags: [research]
---



We introduce a novel framework designed to effectively address the object goal navigation task, specifically focusing on smaller daily household objects such as bowls or mugs. These diminutive objects present challenges to existing SLAM-based semantic mapping methods, as the object detection module employed in the mapping pipeline struggles to accurately detect them. To address this limitation, we propose to use a probabilistic semantic map. It is updated by a trained mapping module that incorporates contextual information to estimate the likelihood of object presence within the agent's current field of view. Subsequently, this probabilistic map guides the agent towards more promising areas for object search. Our experimental results demonstrate that the proposed method surpasses the SOTA approach by 26\% in Small Object Navigation tasks.


