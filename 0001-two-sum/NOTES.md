<h2>Explanation of the solution</h2>
<p>
  <ol>
    <li>Initialize a hash map <code>hash</code> to store values and their indices.</li>
    <li>Iterate through the <code>nums</code> list using <code>enumerate</code> to track both index (<code>idx</code>) and value (<code>val</code>).</li>
    <li>Calculate <code>delta</code> as the difference between <code>target</code> and <code>val</code>.</li>
    <li>Check if <code>delta</code> exists in <code>hash</code>; if so, return the indices stored in <code>hash</code> corresponding to <code>delta</code> and <code>idx</code>.</li>
    <li>Store the current <code>val</code> as a key in <code>hash</code> with its <code>idx</code> as the value.</li>
  </ol>
</p>
​
