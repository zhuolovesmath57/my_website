+++
title = "Milnor's Exercise"
date = 2024-01-27
draft = false
math = true
+++

The following interesting theorem is sometimes called "Milnor's exercise." Of couse, Milnor did not provide a solution himself, and it seems that the result was first proved by Pursell.

<span style="color:blue">$\boldsymbol{\sf Theorem\textsf{}.}$</span>	Let $M$ be a smooth manifold (with or without boundary). Suppose $\mathcal{F}=C^{\infty}(M)$ is the $\mathbb{R}$-algebra of smooth real-valued functions on $M$. Then for any $\mathbb{R}$-algebra homomorphism $p:\mathcal F\to\mathbb{R}$, there exists a unique $x\in X$ such that
$$
p(f)=f(x),\quad \forall f\in\mathcal F,
$$
i.e., $p=\mathrm{ev}_{x}$, the evaluation map at for a unique $x\in X$.

*Proof*. Consider the assignment $\theta:M\to \mathcal F^*$ given by $\theta(x)=\mathrm{ev}_{x}$. We need to show that $\theta$ is a bijection. Clearly $\theta$ is injective, for if $x\ne y$, then there exists $f\in C^{\infty}(M)$ such that $f(x)\ne f(y)$. It remains to show that $\theta$ is surjective.
	
Suppose $p: \mathcal{F} \rightarrow \mathbb{R}$ is an $\mathbb{R}$-algebra homomorphism onto $\mathbb{R}$. Choose a smooth function $f \in C^{\infty}(M)$ all of whose level sets are compact. For example, one may take $f$ to be a smooth exhaustion function on $M$, which exists for any manifold with or without boundary. Then, in particular, the set $L=f^{-1}(\lambda)$, where $\lambda=p(f)$, is compact. Suppose that $p \in\mathcal F^*$ is not the evaluation map at any point of $M$. Then for any point $a \in M$ there exists a function $f_a \in \mathcal{F}$ for which $f_a(a) \neq p\left(f_a\right)$. The sets
$$
M_a=\\{x \in M \mid f_a(x) \neq p(f_a)\\}
$$
are open in $M$, and $a\in M_a$. The sets $\{M_a:a\in L\}$ constitute an open covering of $L$. Since $L$ is compact, we can choose a finite subcovering $M_{a_1}, \ldots, M_{a_m}$. Consider the function
$$
g=(f-p(f))^2+\sum_{i=1}^m\left(f_{a_i}-p\left(f_{a_i}\right)\right)^2 .
$$
This is a smooth nonvanishing function on $M$, so that $1 / g \in \mathcal{F}$, i.e., $g$ is a unit in $C^{\infty}(M)$. However, by the definition of $g$,
$$
p(g)=(p(f)-p(f))^2+\sum_{i=1}^m\left(p\left(f_{a_i}\right)-p\left(f_{a_i}\right)\right)^2=0,
$$
which is a contradiction, proving the surjectivity of $\theta$.

<div style="float: right; width: 0.8em; height: 0.8em; border: 0.4em solid black; position: relative; top: -2.1em"></div>