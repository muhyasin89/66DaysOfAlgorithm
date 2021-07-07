===========================================
what is related topic that you need to  |||
understand before big O,                |||
and explain why?                        |||
===========================================

The dominant term===========================================
The dominant term is the term the one that gets biggest (i.e. dominates) as N gets bigger. 
and as N gets very large, the N^4 is going to get biggest (irrespective of the 200 that you multiply it by)


coefficients===========================================
MATHEMATICS
A coefficient is a number multiplied by a variable.
a numerical or constant quantity placed before and multiplying the variable in an algebraic expression (e.g. 4 in 4x y).

Example:
4x, 4y

PHYSICS
a multiplier or factor that measures some property.

Time Complexity
Time complexity is the amount of time taken by an algorithm to run, as a function of the length of the input. It measures the time taken to execute each statement of code in an algorithm.

Space Complexity
The space complexity is related to how much memory the program will use, and therefore is also an important factor to analyze.


Big O, Little O, Omega & Theta===========================================
<ul>
    <li>Big O: “f(n) is O(g(n))” iff for some constants c and N₀, f(N) ≤ cg(N) for all N > N₀</li>
    <li>Omega: “f(n) is Ω(g(n))” iff for some constants c and N₀, f(N) ≥ cg(N) for all N > N₀</li>
    <ul>
        <li>This is the framework for you to understand something the topic in data structure</li>
    </ul>
    <li>Theta: “f(n) is Θ(g(n))” iff f(n) is O(g(n)) and f(n) is Ω(g(n))</li>
    <li>Little O: “f(n) is o(g(n))” iff f(n) is O(g(n)) and f(n) is not Θ(g(n))</li>
</ul>

—Formal Definition of Big O, Omega, Theta and Little O

simplified above:
Big O (O()) describes the upper bound of the complexity.
Omega (Ω()) describes the lower bound of the complexity.
Theta (Θ()) describes the exact bound of the complexity.
Little O (o()) describes the upper bound excluding the exact bound.

<img src="https://www.freecodecamp.org/news/content/images/2021/06/1_O-dcXbYXojkAPEnDuVZMvA.png" alt="Relationships between Big O, Little O, Omega & Theta Illustrated
"/>

For example, the function g(n) = n² + 3n is O(n³), o(n⁴), Θ(n²) and Ω(n). But you would still be right if you say it is Ω(n²) or O(n²).

Big-O complexity chart
<img src="https://www.freecodecamp.org/news/content/images/2021/06/1_KfZYFUT2OKfjekJlCeYvuQ.jpeg" />
<p>Complexity Growth Illustration from <a href="https://www.bigocheatsheet.com/">Big O Cheatsheet</a></p>


<ul>
    <li>O(1) has the least complexity</li>
    <ul>
        <li>Often called “constant time”, if you can create an algorithm to solve the problem in O(1), you are probably at your best. In some scenarios, the complexity may go beyond O(1), then we can analyze them by finding its O(1/g(n)) counterpart. For example, O(1/n) is more complex than O(1/n²).</li>
    </ul>
    <li>O(log(n)) is more complex than O(1), but less complex than polynomials</li>
    <ul>
        <li>As complexity is often related to divide and conquer algorithms, O(log(n)) is generally a good complexity you can reach for sorting algorithms. O(log(n)) is less complex than O(√n), because the square root function can be considered a polynomial, where the exponent is 0.5.</li>
    </ul>
    <li>Complexity of polynomials increases as the exponent increases</li>
    <ul>
        <li>For example, O(n⁵) is more complex than O(n⁴). Due to the simplicity of it, we actually went over quite many examples of polynomials in the previous sections.</li>
    </ul>
    <li><Exponentials have greater complexity than polynomials as long as the coefficients are positive multiples of n/li>
    <ul>
        <li>O(2ⁿ) is more complex than O(n⁹⁹), but O(2ⁿ) is actually less complex than O(1). We generally take 2 as base for exponentials and logarithms because things tends to be binary in Computer Science, but exponents can be changed by changing the coefficients. If not specified, the base for logarithms is assumed to be 2.</li>
    </ul>
    <li>Factorials have greater complexity than exponentials</li>
    <ul>
        <li>If you are interested in the reasoning, look up the Gamma function, it is an analytic continuation of a factorial. A short proof is that both factorials and exponentials have the same number of multiplications, but the numbers that get multiplied grow for factorials, while remaining constant for exponentials.</li>
    </ul>
    <li>Multiplying terms</li>
    <ul>
        <li>When multiplying, the complexity will be greater than the original, but no more than the equivalence of multiplying something that is more complex. For example, O(n * log(n)) is more complex than O(n) but less complex than O(n²), because O(n²) = O(n * n) and n is more complex than log(n).</li>
    </ul>
    
</ul>



To test your understanding, try ranking the following functions from the most complex to the lease complex. The solutions with detailed explanations can be found in a later section as you read. Some of them are meant to be tricky and may require some deeper understanding of math. As you get to the solution, you will understand them more.

Question: Rank following functions from the most complex to the lease complex.</p>


![plot](https://www.freecodecamp.org/news/content/images/2021/06/1_69bzUpQxBwZFLBimaMe7kQ.png?raw=true "Free Code Camp"))
<p>Examples taken from <a href="https://www.chegg.com/homework-help/questions-and-answers/problem-ask-refresh-knowledge-asymptotic-notations-rank-following-functions-order-growth-f-q23698273">Textbook Problems</a></p>



General Rules:
certain terms "dominate" others
O(1) < O(log n) < O(n) < O(nlogn) < O(n²) < O(2ⁿ) < O(n!)

Reference:
https://www.youtube.com/watch?v=__vX2sjlpXU (Best)
