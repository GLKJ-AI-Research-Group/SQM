# -*- coding: utf-8 -*-
'''
@Time    : 2023/8/30 9:58
@Author  : hejipei
@File    : MeanFiltering.py
@function:
@reference:https://blog.csdn.net/qq_36686437/article/details/110421201
'''
import open3d as o3d
import numpy as np

class o3dtut:
    def get_knot_mesh():
        mesh = o3d.io.read_triangle_mesh("Armadillo.ply")
        mesh.compute_vertex_normals()
        return mesh

mesh_in = o3dtut.get_knot_mesh()
vertices = np.asarray(mesh_in.vertices)
noise = 5
vertices += np.random.uniform(0, noise, size=vertices.shape)
mesh_in.vertices = o3d.utility.Vector3dVector(vertices)
mesh_in.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh_in],width=800,height=800)

print('filter with average with 1 iteration')
mesh_out = mesh_in.filter_smooth_simple(number_of_iterations=10)
mesh_out.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh_out],width=800,height=800)

print('filter with average with 5 iterations')
mesh_out = mesh_in.filter_smooth_simple(number_of_iterations=20)
mesh_out.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh_out],width=800,height=800)

