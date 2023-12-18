+++
title = "Milnor's Proof of the Fundamental Theorem of Algebra"
date = 2023-12-18T00:29:31-06:00
draft = true
math = true
+++

I came across the following interesting proof of the fundamental theorem of algebra. The argument is due to Milnor and can be found in his book *Topology from the Differentiable Viewpoint*. The proof uses differential topology and some very elementary complex analysis. In particular, it does not use Liouville's theorem, which is one of the most common ways to prove the fundamental theorem of algebra.

<span style="color:blue">$\boldsymbol{\sf Theorem\textsf{ (Fundamental Theorem of Algebra)}.}$</span>	Every nonconstant polynomial $p\in\mathbb{C}[x]$ has a zero.

*Proof*. Recall that since $p$ is analytic, we have the Cauchy Riemann conditions
$$
u\_x=v\_y\quad\text{and}\quad u\_y=-v\_x.
$$
Hence, the Jacobian is $u\_x^2+u\_y^2$, which is zero if and only if $p^{\prime}(z)=0$. Since $p'$ has only finitely many zeros, $p: \mathbb{R}^2 \rightarrow \mathbb{R}^2$ has only finitely many critical points. Let $F \subset \mathbb{R}^2$ be the finite set of critical values.

If $p(z)=a\_nz^n+\cdots+a\_1z+a\_0$, with $a\_n\ne0$, then
$$
|p(z)|\ge|a\_n||z|^n-|a\_{n-1}||z|^{n-1}-\cdots-|a\_{1}||z|-|a\_0|,
$$
whence $|p(z)| \to \infty$ as $|z| \to \infty$. This implies that $p$ extends to a map of the one-point compactification $S^2$ of $\mathbb{R}^2$. Recall that a map between locally compact Hausdorff (LCH) spaces is proper if and only if it extends to a map between the corresponding one-point compactifications. Furthermore, because proper maps between LCH spaces are closed. Therefore, $p$ is a closed map.

For any $c \in \mathbb{C}$, $p^{-1}(c)$ consists of the zeros of the polynomial $p(z)-c$ and so it contains at most $n$ points. Let $k=k(c)$ be the number of points in $p^{-1}(c)$. Suppose $c$ is a regular value and $p^{-1}(c)=\\{z\_1, \ldots, z\_k\\}$. By the inverse function theorem, there are disjoint open balls $B\_i$ containing $z\_i$ such that $p|\_{B\_i}:B\_i\to p(B\_i)$ are diffeomorphisms. Since $f$ is closed, the set $G=f(\mathbb{R}^2-\left(B\_1 \cup \cdots \cup B\_k\right))$ is closed, and $c\notin G$. Hence, there is an open neighborhood $V$ containing $c$ that is disjoint from $G$. Then $f^{-1}(V)\subseteq B\_1\cup\cdots\cup B\_k$. Let $W\_i=(f|\_{B\_i})^{-1}(V)$. Then $f|\_{W\_i}:W\_i\to V$ are diffeomorphisms, and $p^{-1}(V)=\coprod\_{i=1}^kW\_i$.

It follows that $k(c)$ is locally constant on the set $\mathbb{R}^2\setminus F$ of regular values. Since $\mathbb{R}^2\setminus F$ is connected, $k(c)$ is constant on $\mathbb{R}^2-F$. This constant cannot be zero since that would imply that the image of $p$ is $F$, and hence that $p$ is constant since $F$ is disconnected, but $p$ is not constant. This shows that  the image of $p$ contains $\left(\mathbb{R}^2\setminus F\right) \cup F=\mathbb{R}^2$, so that $p$ takes on all values of $\mathbb{C}$, including 0.
<div style="float: right; width: 0.8em; height: 0.8em; border: 0.4em solid black; position: relative; top: -2.5em"></div>

<span style="color:#eb861c">$\boldsymbol{\sf Remark.}$</span>	There are other arguments with a similar flavor of this one. For example, a proper map $f:M\to N$ between smooth manifolds of the same dimension induces a map on the top-degree compactly supported de Rham cohomology $f^*:H\_c^\mathrm{top}(N)\to H\_c^\mathrm{top}(M)$. Using this data we may define the degree of a proper map, which is a real number. It is a nontrivial fact that degree is an integer, and the proof uses a very similar construction as the one given above!