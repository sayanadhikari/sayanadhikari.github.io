#!/usr/bin/env python
# coding: utf-8
---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.10'
    jupytext_version: 1.5.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# # Numerical methods
# 
# My (now finished) PhD student Miroslav Kuchta has been looking at numerical methods to solve
# saddle point systems arising from trace constraints coupling 2D and 1D domains,
# or 3D and 1D domains {cite}`kuchta2016,kuchta2016preconditioning,kuchta15`.
# 
# We have also been studying the singular Neumann problem of linear elasticity
# {cite}`kuchta2016singular`.
# Four different formulations of the problem have been analyzed and mesh independent preconditioners established for the resulting linear systems within the framework of operator preconditioning. We have proposed a preconditioner for the (singular) mixed formulation of linear elasticity, that is robust with respect to the material parameters. Using an orthonormal basis of the space of rigid motions, discrete projection operators have been derived and employed in a modification to the conjugate gradients method to ensure optimal error convergence of the solution.
# 
# With colleagues at the Extreme Computing Research Center (ECRC), King Abdullah University of Science and Technology (KAUST), we have been using [spectralDNS](https://github.com/spectralDNS) to investigate time integration of Fourier pseudospectral Direct Numerical Simulations {cite}`ketcheson2020`. We investigate the use of higher‐order Runge‐Kutta pairs and automatic step size control based on local error estimation. We find that the fifth‐order accurate Runge‐Kutta pair of Bogacki and Shampine gives much greater accuracy at a significantly reduced computational cost.

# ## References
# 
# ```{bibliography} ../../references.bib
# :filter: docname in docnames
# ```
