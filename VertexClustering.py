# -*- coding: utf-8 -*-
'''
@Time    : 2023/8/30 10:18
@Author  : hejipei
@File    : VertexClustering.py
@function:
@reference:https://blog.csdn.net/qq_36686437/article/details/110578644
'''
import open3d as o3d

mesh = o3d.io.read_triangle_mesh("bunny.ply")
mesh.compute_vertex_normals()
print(f'Input mesh has {len(mesh.vertices)} vertices and {len(mesh.triangles)} triangles')
o3d.visualization.draw_geometries([mesh])

voxel_size = max(mesh.get_max_bound() - mesh.get_min_bound()) / 32
print(f'voxel_size = {voxel_size:e}')
mesh_smp = mesh.simplify_vertex_clustering(
    voxel_size=voxel_size,
    contraction=o3d.geometry.SimplificationContraction.Average)
print(f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')
o3d.visualization.draw_geometries([mesh_smp])

voxel_size = max(mesh.get_max_bound() - mesh.get_min_bound()) / 16
print(f'voxel_size = {voxel_size:e}')
mesh_smp = mesh.simplify_vertex_clustering(
    voxel_size=voxel_size,
    contraction=o3d.geometry.SimplificationContraction.Average)
print(f'Simplified mesh has {len(mesh_smp.vertices)} vertices and {len(mesh_smp.triangles)} triangles')
o3d.visualization.draw_geometries([mesh_smp])
