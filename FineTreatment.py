# -*- coding: utf-8 -*-
'''
@Time    : 2023/8/30 9:51
@Author  : hejipei
@File    : FineTreatment.py
@function:
@reference:https://blog.csdn.net/qq_36686437/article/details/110566329
'''
import open3d as o3d

mesh = o3d.io.read_triangle_mesh("UV.ply")
mesh.compute_vertex_normals()
print(
    f'The mesh has {len(mesh.vertices)} vertices and {len(mesh.triangles)} triangles'
)
o3d.visualization.draw_geometries([mesh], mesh_show_wireframe=True)
mesh = mesh.subdivide_loop(number_of_iterations=2)
print(
    f'After subdivision it has {len(mesh.vertices)} vertices and {len(mesh.triangles)} triangles'
)
o3d.visualization.draw_geometries([mesh], mesh_show_wireframe=True)

