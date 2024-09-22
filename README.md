# Video Enhancement Tool / 视频增强工具

This project provides a Python script for enhancing video quality using super-resolution techniques.

本项目提供了一个使用超分辨率技术来提高视频质量的Python脚本。

## Features / 功能

- Upscales video resolution by 4x using ESPCN model
- Supports various video formats
- Automatic model download

- 使用ESPCN模型将视频分辨率提高4倍
- 支持多种视频格式
- 自动下载模型

## Requirements / 依赖

- Python 3.6+
- OpenCV
- NumPy
- MoviePy

## Installation / 安装

1. Clone this repository / 克隆此仓库
   ```
   git clone https://github.com/yourusername/video-enhancement-tool.git
   cd video-enhancement-tool
   ```

2. Install dependencies / 安装依赖
   ```
   pip install opencv-python numpy moviepy
   ```

## Usage / 使用方法

1. Place your input video in the project directory / 将输入视频放在项目目录中
   Make sure this filename is iput.mp4/ 确保文件名是input.mp4

2. Run the script / 运行脚本
   ```
   python videoenhance.py
   ```

3. The enhanced video will be saved as "enhanced_output.mp4" / 增强后的视频将保存为"enhanced_output.mp4"

## How it works / 工作原理

The script uses the ESPCN (Efficient Sub-Pixel Convolutional Neural Network) model for super-resolution. It processes the video frame by frame, enhancing each frame's resolution before reconstructing the video.

该脚本使用ESPCN（高效亚像素卷积神经网络）模型进行超分辨率处理。它逐帧处理视频，在重建视频之前提高每一帧的分辨率。

## License / 许可证

This project is licensed under the MIT License 

本项目采用MIT许可证 

## Acknowledgments / 致谢

- ESPCN model from [TF-ESPCN](https://github.com/fannymonori/TF-ESPCN)
- OpenCV for image processing
- MoviePy for video handling

- ESPCN模型来自[TF-ESPCN](https://github.com/fannymonori/TF-ESPCN)
- 使用OpenCV进行图像处理
- 使用MoviePy处理视频
