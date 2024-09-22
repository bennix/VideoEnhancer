import cv2
import numpy as np
from moviepy.editor import VideoFileClip
import os
import urllib.request

# 模型文件的URL和本地保存路径
MODEL_URL = "https://github.com/fannymonori/TF-ESPCN/raw/master/export/ESPCN_x4.pb"
MODEL_PATH = "ESPCN_x4.pb"

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("正在下载模型...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("模型下载完成")

def enhance_frame(frame, sr):
    # 预处理
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(frame)
    
    # 使用超分辨率模型处理Y通道
    y = sr.upsample(y)
    
    # 调整Cr和Cb通道的大小以匹配新的Y通道
    cr = cv2.resize(cr, (y.shape[1], y.shape[0]), cv2.INTER_CUBIC)
    cb = cv2.resize(cb, (y.shape[1], y.shape[0]), cv2.INTER_CUBIC)
    
    # 合并通道并���回BGR
    enhanced = cv2.merge([y, cr, cb])
    enhanced = cv2.cvtColor(enhanced, cv2.COLOR_YCrCb2BGR)
    
    return enhanced

def process_video(input_path, output_path):
    # 下载模型（如果需要）
    download_model()
    
    # 加载超分辨率模型
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel(MODEL_PATH)
    sr.setModel("espcn", 4)  # 4倍放大
    
    clip = VideoFileClip(input_path)
    
    def enhance(get_frame, t):
        frame = get_frame(t)
        return enhance_frame(frame, sr)
    
    enhanced_clip = clip.fl(enhance)
    enhanced_clip.write_videofile(output_path, codec='libx264')

# 使用示例
input_video = "input.mp4"
output_video = "enhanced_output.mp4"
process_video(input_video, output_video)
