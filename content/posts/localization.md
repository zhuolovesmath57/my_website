+++
title = "Localization of smooth functions"
date = 2024-04-17
draft = false
math = true
+++

In this note we prove a rather surprising fact: the ring of smooth functions on an open subset $U$ of a manifold $M$ is the same as localizing the ring of smooth functions on $M$ at the multiplicative system of smooth functions that do not vanish on $U$. As far as I know, this is a known result, but I couldn't find it any literature that rigorously proves this fact, so I decided to write it down myself.

The following lemma deals with the most technical part of the proof. 

<span style="color:blue">$\boldsymbol{\sf Lemma\textsf{}.}$</span>	Let $M$ be a manifold and $U\subset M$ be open. For every smooth function $f:U\to\mathbb{R}$, there exists smooth function $g:M\to[0,1]$ such that $g$ is strictly positive on $U$, vanishes outisde $U$, and the function
$$
fg(x)=\begin{cases}
f(x)g(x)&~x\in U,
\\
0&~x\notin U,
\end{cases}
$$
is smooth on $M$.

*Proof*.

<span style="color:#c90076">$\boldsymbol{\sf{Step~1.}\textsf{}}$</span>	First suppose that $U\subset\mathbb{R}^n$.

Cover $U$ by countably many balls $B(x_i,r_i)$ satisfying $\overline{B(x_i,2r_i)}\subset U$. For each $i$, choose a bump function $\psi_i$ such that $\psi_i=1$ on $\overline{B(x_i,r_i)}$ and $\operatorname{supp}\psi_i\subset B(x_i,2r_i)$. Then the function $\psi_if$ is well defined by extension to 0 outside $U$.

Let $C_i>0$ (resp. $D_i>0$) be positive constants that bound the absolute values of all partial derivatives of $\psi_i$ (resp. $\psi_if$) up to order $i$ on $\overline{B(x_i,2r_i)}$, and hence on all of $\mathbb{R}^n$, since $\psi_i$ and $\psi_if$ are supported in $B(x_i,2r_i)$. Consider the function
$$
g(x)=\sum_{i=1}^\infty2^{-i}\frac{\psi_i(x)}{1+C_i+D_i}.
$$
Clearly $0<g<1$ on $U$ and $g=0$ outside $U$. To show that $g$ is smooth, let $\partial_k$ denote any $k$th partial derivative. Then
$$
2^{-i}\frac{\partial_k\psi_i}{1+C_i+D_i}<2^{-i},
$$
provided that $i>k$. Hence, the series of partial derivatives of $g$ converge uniformly, and so $g$ is smooth. A similar consideration shows that
$$
fg(x)=\sum_{i=1}^\infty2^{-i}\frac{\psi_if(x)}{1+C_i+D_i}
$$
is smooth on $\mathbb{R}^n$, as required.

<span style="color:#c90076">$\boldsymbol{\sf{Step~2.}\textsf{}}$</span>	Now, for the general case, suppose that $U\subset M$.

Cover $M$ by coordinate balls $\{B_\alpha\}$, each of which is diffeomorphic to $\mathbb{R}^n$. Note that the conclusion in step 1 remains trivially true if $U$ is empty. For each $\alpha$, $U\cap B_\alpha$ is an open subset of $B_\alpha$ (possibly empty). The function $f:U\cap B_\alpha\to\mathbb{R}$ is smooth, and so by step 1 there exists a smooth function $g_\alpha:B_\alpha\to[0,1]$ such that $0<g_\alpha<1$ on $U\cap B_\alpha$, $g_\alpha=0$ on $B_\alpha\setminus U$, and $g_\alpha f$ is smooth on $B_\alpha$. Choose a partition of unity $\{\psi_\alpha\}$ on $M$ subordinate to the open cover $\{B_\alpha\}$. Then the function
$$
g=\sum_\alpha\psi_\alpha g_\alpha
$$
is smooth on $M$. We argue that $0<g<1$ on $U$ and $g=0$ outside $U$. To see this, note first that each $g_\alpha$ satisfies $0\le g_\alpha\le1$, and so any convex linear combination of values of $g_\alpha$ must also lie in $[0,1]$. Furthermore, for all $x\in U$, there is at least one $\alpha_0$ for which $x\in U\cap B_{\alpha_0}$, whence $g_{\alpha_0}(x)>0$. Finally, if $x\notin U$, then $g_\alpha(x)=0$ for all $\alpha$, whence $g(x)=0$.

It remains to check that $gf$ is smooth on $M$. Indeed, we have
$$
gf=\sum_\alpha\psi_\alpha\cdot(g_\alpha f),
$$
where $g_\alpha f$ is smooth on $B_\alpha$. But since $\operatorname{supp}\psi_\alpha\subset B_\alpha$, the functions $\psi_\alpha\cdot(g_\alpha f)$ are well defined and smooth on $M$. Since $\{\psi_\alpha\}$ is a partition of unity, $gf$ is also smooth on $M$.

<div style="float: right; width: 0.7em; height: 0.7em; border: 0.35em solid black; position: relative; top: -2.1em"></div>

<span style="color:blue">$\boldsymbol{\sf Theorem\textsf{}.}$</span>	Let $M$ be a manifold and $U\subset M$ be open. Let $S\subset C^{\infty}(M)$ be the subset consisting of all smooth functions on $M$ that do not vanish anywhere on $U$. Then $C^{\infty}(U)\cong S^{-1}C^{\infty}(M)$.

*Proof*. Consider the restriction map $\rho:C^{\infty}(M)\to C^{\infty}(U)$. Clearly $\rho$ sends $S$ to units in $C^{\infty}(U)$, so $\rho$ induces a unique map $\bar\rho: S^{-1}C^{\infty}(M)\to C^{\infty}(U)$. We claim that $\bar\rho$ is an isomorphism.

Suppose that $\bar\rho\left(f / s\right)=0$. Then $f=0$ on $U$. Choose a characteristic function of $U$, i.e., a function $g\in C^{\infty}(M)$ such that $g^{-1}(0)=M\setminus U$.

> Note that this follows directly from the preceding lemma, but it didn't require its full strength. In fact, this is a known theorem due to Whitney: every closed subset of a manifold is the zero set of some smooth function.

Hence, $g$ is nonzero on $U$ and is zero outside $U$. It follows that $g\in S$, and $fg=0$. Hence, $f/s=0$, so $\bar\rho$ is injective. The fact that $\bar\rho$ is surjective follows from the preceding lemma.

<div style="float: right; width: 0.7em; height: 0.7em; border: 0.35em solid black; position: relative; top: -2.1em"></div>

