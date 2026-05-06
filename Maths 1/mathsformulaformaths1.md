# Data Science Calculus Master Cheat Sheet

## Phase 1: Pre-Calculus Foundations

**Slope:** $m = \frac{y_2-y_1}{x_2-x_1}$

**Line Equations:**

- Point-slope: $y-y_1 = m(x-x_1)$
- Slope-intercept: $y = mx+b$

**Quadratic Formula:** $x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}$

**Log Properties:**

- $\log_b(x) = y \iff b^y = x$
- $\log_b(x^n) = n\log_b(x)$
- $\ln(e^x) = x$, $e^{\ln(x)} = x$

---

## Phase 2: Differential Calculus

**Power Rule:** $\frac{d}{dx}[x^n] = nx^{n-1}$

**Constant Rule:** $\frac{d}{dx}[c] = 0$

**Exponential:** $\frac{d}{dx}[e^x] = e^x$

**Logarithmic:** $\frac{d}{dx}[\ln(x)] = \frac{1}{x}$

**Product Rule:** $(fg)' = f'g + fg'$

**Quotient Rule:** $(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$

**Chain Rule:** $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$

---

## Phase 3: Integral Calculus

**Reverse Power Rule:** $\int x^n dx = \frac{x^{n+1}}{n+1} + C$ (for $n \neq -1$)

**Exception:** $\int \frac{1}{x}dx = \ln|x| + C$

**Exponential:** $\int e^x dx = e^x + C$

**Fundamental Theorem:** $\int_a^b f(x)dx = F(b) - F(a)$

**Area Between Curves:** $\int_a^b [\text{top} - \text{bottom}]dx$

# 🎓 IITM BS Foundation: Mathematics & Statistics Cheat Sheet

> **Focus:** Mathematics for Data Science 1 & Statistics for Data Science 1
> **Context:** Compiled from Foundation Level Quiz and End-Term Patterns (2022-2025)

---

## 📐 Mathematics for Data Science 1

### 1. Set Theory & Functions

* **Surjective (Onto) Functions:** For $f: A \to B$ where $|A| = n$ and $|B| = m$:
  * If $m=2$, the number of onto functions is: $2^n - 2$.
* **Composition Domain ($f \circ g$):**
  $$
  f \circ g = \{x \in D_g \mid g(x) \in D_f\}
  $$
* **Sum of Functions Domain:** For $f_1(x) + f_2(x)$, the domain is the intersection: $D_1 \cap D_2$.
* **Logarithmic Identity:**
  $$
  \log_b c = c^{\log_b a}
  $$

### 2. Calculus & Sequences

* **Continuity at Point $c$:**
  $$
  \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = f(c)
  $$
* **Equation of Tangent Line:** At point $x_0$:
  $$
  f(x_0) = f'(x_0)(x - x_0)
  $$
* **Limits of Sequences:**
  * For rational functions $\frac{P(n)}{Q(n)}$, if degrees are equal, the limit is the ratio of leading coefficients.
  * **Growth Order:** $e^n \gg n^k \gg \log(n)$ as $n \to \infty$.

### 3. Coordinate Geometry (Parabolas)

* **Standard Vertex Form:** $y = a(x - h)^2 + k$
* **Suspension Bridge Problems:** If the vertex (lowest point) is at $(0, L_{\text{min}})$, the equation is:
  $$
  y = ax^2 + L_{\text{min}}
  $$

---

## 📊 Statistics for Data Science 1

### 1. Combinatorics & Probability

* **Permutations vs. Combinations:**
  * $nP_r = \frac{n!}{(n-r)!}$
  * $nC_r = \frac{n!}{r!(n-r)!}$
* **Circular Arrangement:** For $n$ items, if one position is fixed: $(n-1)!$ ways.
* **Bayes' Theorem:**
  $$
  P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)}
  $$

### 2. Common Probability Distributions

| Distribution           | Mean$E[X]$      | Variance$Var(X)$     | Notes                        |
| :----------------------- | :---------------- | :--------------------- | :----------------------------- |
| **Bernoulli($p$)**     | $p$             | $p(1-p)$             | Single trial                 |
| **Binomial($n, p$)**   | $np$            | $np(1-p)$            | $n$ independent trials       |
| **Poisson($\lambda$)** | $\lambda$       | $\lambda$            | Rare events in interval      |
| **Geometric($p$)**     | $1/p$           | $(1-p)/p^2$          | Trials until first success   |
| **Uniform($a, b$)**    | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | Equal probability over range |

### 3. Statistical Laws & Inequalities

* **Markov’s Inequality:** For non-negative $X$ and $c > 0$:
  $$
  P(X \ge c) \le \frac{E[X]}{c}
  $$
* **Chebyshev’s Inequality:**
  $$
  P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}
  $$
* **Central Limit Theorem (CLT):** For large $n$, the sample mean $\bar{X}$ approximates:
  $$
  \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)
  $$
* **Sample Covariance:**
  $$
  {xy} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n-1}
  $$

---

## 💡 Exam Strategy Tips

* **Maths 1:** Focus heavily on the **Domain and Range** questions in Section 1. They appear in every paper.
* **Stats 1:** Always check if a probability problem is **"with replacement"** or **"without replacement"** before choosing between Binomial and Hypergeometric logic.
* **Numerical Answers:** Always double-check the rounding instructions (e.g., "correct to two decimal places").
