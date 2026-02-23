## NeRF Reconstruction Pipeline
This project implements a complete neural radiance field (NeRF) reconstruction pipeline, beginning with real-world video capture and proceeding through COLMAP-based camera pose estimation, NeRF training using Nerfstudio’s nerfacto model, and final point cloud export. The project required resolving CUDA configuration and environment integration challenges within WSL, and resulted in a structurally accurate 3D reconstruction.

## Results
- Detailed report: `NeRF_project_report_Aaron_Miller.pdf` (1.5 MB)
- Exported point cloud: `outputs/reconstruction.ply` (26 MB)
- Sample input video: `data/sample_video.mp4` (5 MB)
  
This repository documents the reconstruction pipeline and environment configuration used for experimentation. It is not intended to be a fully portable executable package.
