# -*- coding: utf-8 -*-
'''
@Time    : 2023/8/30 10:48
@Author  : hejipei
@File    : Surfacereconstruction.py
@function:
@reference:https://blog.csdn.net/qq_36686437/article/details/110500177
'''
import open3d as o3d
import numpy as np


pcd = o3d.io.read_point_cloud("bunny.ply")
o3d.visualization.draw_geometries([pcd], width=800, height=800,
                                  window_name="原始点云",
                                  mesh_show_back_face=False)  # 可视化点云
alpha = 0.03
print(f"alpha={alpha:.3f}")
mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha)  # 执行单一alpah阈值
mesh.compute_vertex_normals()  # 计算mesh的法线
o3d.visualization.draw_geometries([mesh], window_name="单一alpah阈值的结果",
                                  width=800, height=800,
                                  mesh_show_back_face=True)
# 从给定点云中计算多个a-shape
tetra_mesh, pt_map = o3d.geometry.TetraMesh.create_from_point_cloud(pcd)  # 从点云创建四面体网格
for alpha in np.logspace(np.log10(0.5), np.log10(0.01), num=4):
    print(f"alpha={alpha:.3f}")
    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(
        pcd, alpha, tetra_mesh, pt_map)
    mesh.compute_vertex_normals()
    o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)

