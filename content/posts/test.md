+++
title = 'Test'
date = 2023-12-16T11:43:50-06:00
draft = false
math = true
+++



Hello! I'm Zhuo.

Consider $v\in M_n(\mathbb{R})$. Then $\gamma(t)=I+tv$ is a curve in $GL_n(\mathbb{R})$, for $t$ small, with $\gamma(0)=I$. Then $\dot\gamma(0)=v$. It follows that


$$
\begin{aligned}
T_IF(v)=(F\circ\gamma)^\boldsymbol{\cdot}(0)&=\frac{d}{dt}\bigg|_0(I+tv)^\mathsf{T}(I+tv)
\newline
&=\frac{d}{dt}\bigg|_0(I+t(v^\mathsf{T}+v)+t^2v^\mathsf{T}v)
\newline
&=v^\mathsf{T}+v.
\end{aligned}
$$


hi


Since $\operatorname{Sym}^2(\mathbb{R}^n)$ is a vector space, its tangent space can be identified with itself. For every $B\in\operatorname{Sym}^2(\mathbb{R}^n)$, one can write
$$
B=\frac{1}{2}(B^\mathsf{T}+B).
$$
Hence, $T_IF$ is onto.