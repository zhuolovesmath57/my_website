+++
title = "Tensoriality"
date = 2024-02-17
draft = false
math = true
+++

We introduce an important concept called tensoriality, which you may also recognize as $C^{\infty}(M)$-linearity. It is a very common argument in tensor analysis. I have made this note as self-contained as possible.

<span style="color:green">$\boldsymbol{\sf Definition\textsf{}.}$</span>	Let $V$ be a finite dimensional real vector space. We define
$$
T^{(k,l)}V:=\underbrace{V\otimes\cdots\otimes V}\_k\otimes \underbrace{V^\ast\otimes\cdots\otimes V^\ast}\_{l}.
$$
Similarly, if $E\to M$ is a vector bundle, we define
$$
T^{(k,l)}E:=\underbrace{E\otimes\cdots\otimes E}\_k\otimes \underbrace{E^\ast\otimes\cdots\otimes E^\ast}\_{l}.
$$


<span style="color:green">$\boldsymbol{\sf Definition\textsf{}.}$</span>	A tensor field on a manifold $M$ is a section of $T^{(k,l)}TM$ for some $(k,l)$.

<span style="color:#eb861c">$\boldsymbol{\sf Remark.}$</span>	A $(k,l)$-tensor on $V$ can take in $k$ covectors and $l$ vectors and output a number. Similarly, a $(k,l)$-tensor field on $M$ can take in $k$ covector fields and $l$ vector fields and output a function.



<span style="color:blue">$\boldsymbol{\sf{Proposition\textsf{}.}}$</span>	Let $A$ be a rough $(k,l)$-tensor field on $M$. Then TFAE.

1. $A:M\to T^{(k,l)}TM$ is smooth;

2. for any $\omega\_1,\ldots,\omega\_k\in \Gamma(M,T^\ast M)\approx \mathcal{T}^1M$, and $X\_1,\ldots,X\_l\in\Gamma(M,TM)\approx \mathfrak{X}(M)$, the function
   $$
   A(\omega\_1,\ldots,\omega\_k,X\_1,\ldots,X\_l):M\to\mathbb{R}
   $$
   is smooth.



This proposition shows that $A$ determines a map (which we still denote by $A$):
$$
A: \underbrace{\mathcal{T}^1(M) \times \cdots \times \mathcal{T}^1(M)}\_{k} \times \underbrace{\mathfrak{X}(M) \times \cdots \times \mathfrak{X}(M)}\_{l} \rightarrow C^{\infty}(M).
$$
Clearly this map is $C^{\infty}(M)$-linear, where the LHS is considered as a $C^{\infty}(M)$-module. We have the following important theorem.



<span style="color:blue">$\boldsymbol{\sf Theorem\textsf{ (Tensor Characterization Lemma)}.}$</span>	Any $C^{\infty}(M)$ map
$$
A: \underbrace{\mathcal{T}^1(M) \times \cdots \times \mathcal{T}^1(M)}\_{k} \times \underbrace{\mathfrak{X}(M) \times \cdots \times \mathfrak{X}(M)}\_{l} \rightarrow C^{\infty}(M)
$$
is induced by a unique smooth $(k, l)$-tensor field.

> Because of this result, it is common to use the same symbol for both a tensor field and the multilinear map on sections that it defines, and to refer to either of these objects as a tensor field.

*Proof*. This is similar to the proof of the Serre-Swan theorem.

<span style="color:#c90076">$\boldsymbol{\sf{Step~1}\textsf{}}$</span>	We first show that $A$ acts *locally*, i.e., the value of $A(\omega\_1,\ldots,\omega\_k,X\_1,\ldots,X\_l)$ at $p$ only depends on the values of $\omega\_i$ and $X\_j$ in a neighborhood of $p$.

We prove this for $X\_1$. The other cases are just the same. By linearity, we can consider the difference of two (co)vector fields. Hence, it suffices to assume that $X\_1=0$ in a neighborhood $U$ of $p$. Choose a bump function $\tau$ with $\tau(p)=1$ and $\operatorname{supp}\tau\subseteq U$. Then $\tau X\_1=0$ on $M$. Therefore,
$$
0=A(\omega\_1,\ldots,\omega\_k,\tau X\_1,\ldots,X\_l)(p)=\tau(p)A(\omega\_1,\ldots,\omega\_k,X\_1,\ldots,X\_l)(p).
$$
It follows that $A(\omega\_1,\ldots,\omega\_k,X\_1,\ldots,X\_l)(p)=0$.

<span style="color:#c90076">$\boldsymbol{\sf{Step~2}\textsf{}}$</span>	We now show that $A$ acts *pointwise*, i.e., the value of $A(\omega\_1,\ldots,\omega\_k,X\_1,\ldots,X\_l)$ at $p$ only depends on the values of $\omega\_i$ and $X\_j$ at the single point $p$.

We prove this for $X\_1$. The other cases are just the same. Suppose $X\_1(p)=0$. Choose a chart $U$ around $p$, and write $X\_1$ in $U$ as
$$
X\_1=\sum\_{i=1}^mf\_i \frac{\partial }{\partial x\_i},
$$
where $f\_i\in C^{\infty}(U)$. We know that $f\_i(p)=0$ because $X\_1(p)=0$. By choosing bump functions again, we may extend $f\_i$ to $\tilde f\_i\in C^{\infty}(M)$ and $\frac{\partial }{\partial x\_i}$ to $V\_i\in \mathfrak{X}(M)$ such that $f\_i,\tilde f\_i$ and $\frac{\partial }{\partial x\_i},V\_i$ both agree in a neighborhood of $p$. In particular, $\tilde f\_i(p)=f\_i(p)=0$. Let $Y=\sum\_i\tilde f\_i V\_i$. Then $Y\in\mathfrak{X}(M)$ and $Y$ agrees $X\_1$ in a neighborhood of $p$. Since $A$ is local and is $C^{\infty}(M)$-linear, we have
$$
A(\omega\_1,\ldots,\omega\_k,X\_1,\ldots,X\_l)(p)=A(\omega\_1,\ldots,\omega\_k,Y,\ldots,X\_l)(p)
$$
$$
=\sum\_{i=1}^m\tilde f\_i(p)A(\omega\_1,\ldots,\omega\_k,V\_i,\ldots,X\_l)(p)=0.
$$
It follows by linearity that $A(\omega\_1,\ldots,\omega\_k,X\_1,\ldots,X\_l)(p)$ depends only on the value of $\omega\_i$ and $X\_j$ at $p$.

<span style="color:#c90076">$\boldsymbol{\sf{Step~3}\textsf{}}$</span>	Now we define a rough tensor field $\tilde A: M \rightarrow T^{(k,l)} T M$ by
$$
\tilde A\_p\left(h\_1, \ldots, h\_k,v\_1, \ldots, v\_l\right)=A\left(\omega\_1,\ldots,\omega\_k,V\_1, \ldots, V\_l\right)(p)
$$
for $p \in M$, $h\_i\in T^\ast\_pM$, and $v\_j\in T\_pM$, where $\omega\_i$ and $V\_j$ are any smooth global (co)vector fields on $M$ satisfying $\omega\_1(p)=h\_i$ and $V\_j(p)=v\_j$. Step 2 shows that this is well defined, and the resulting tensor field is smooth by the preceding proposition. Clearly $\tilde A$ induces the multilinear map $A$ as above. Finally, The tensor field $\tilde A$ is unique, for if $\tilde A$ were to induce $A$, then $\tilde A$ has to satisfy the above equation.
<div style="float: right; width: 0.8em; height: 0.8em; border: 0.4em solid black; position: relative; top: -2.5em"></div>


<span style="color:#eb861c">$\boldsymbol{\sf Remark.}$</span>	The theorem has many variants, all of which describe the relation between tensoriality and $C^{\infty}(M)$-linearity. The tensor fields are from the manifold to the mixed tangent and cotangent bundles. These can certainly be replaced by arbitrary vector bundles. The codomain of the linear map is $C^{\infty}(M)$, which can be replaced by sections of a possibly different vector bundle.

In other words, we have the following general theorem.

<span style="color:blue">$\boldsymbol{\sf Theorem\textsf{}.}$</span>	Let $E\_i,F\_j,G$ be vector bundles over $M$. Any $C^{\infty}(M)$-linear map of the form
$$
A:\Gamma(M,E\_1^\ast)\times\cdots\Gamma(M,E\_k^\ast)\times\Gamma(M,F\_1)\times\cdots\Gamma(M,F\_l)\to\Gamma(M,G)
$$
must be induced by a unique section of the bundle
$$
E\_1\otimes\cdots\otimes E\_k\otimes F\_1^\ast\otimes\cdots\otimes F\_l^\ast\otimes G
$$
over $M$.

*Proof*. Exactly the same argument, almost verbatim.
<div style="float: right; width: 0.8em; height: 0.8em; border: 0.4em solid black; position: relative; top: -2.5em"></div>
