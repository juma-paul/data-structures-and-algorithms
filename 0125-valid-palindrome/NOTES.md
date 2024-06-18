<h2>Explanation of the solution</h2>
<p>
  <ol>
    <li>Convert the input string <code>s</code> to lowercase and remove all non-alphanumeric characters using regular expressions.</li>
    <li>Initialize two pointers, <code>left</code> and <code>right</code>, to the first and last indices of the cleaned string, respectively.</li>
    <li>Iterate through the string using the two pointers until they meet or cross.</li>
    <li>If the characters at the <code>left</code> and <code>right</code> pointers are not equal, return <code>False</code> as the string is not a palindrome.</li>
    <li>Otherwise, continue iterating by incrementing the <code>left</code> pointer and decrementing the <code>right</code> pointer.</li>
    <li>If the loop completes without returning <code>False</code>, the string is a palindrome, so return <code>True</code>.</li>
  </ul>
</p>​
