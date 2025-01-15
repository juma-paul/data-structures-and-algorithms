<h2>Explanation of the solution</h2>
<p>
  <ol>
    <li>Use two pointers to solve the problem.</li>
    <li>Set two pointers <strong>i</strong> and <strong>j</strong> to the first index of <strong>s</strong> and <strong>t</strong> respectively.</li>
    <li>Iterate through the strings <strong>s</strong> and <strong>t</strong> until pointer <strong>i</strong> reaches the end of <strong>s</strong> or pointer <strong>j</strong> reaches the end of <strong>t</strong>.</li>
    <li>Compare the characters at the current positions of <strong>i</strong> and <strong>j</strong>.</li>
    <li>If the characters match, increment the pointer <strong>i</strong> to check the next character in <strong>s</strong>.</li>
    <li>Always increment the pointer <strong>j</strong> to continue checking the next character in <strong>t</strong>.</li>
    <li>After the loop, if pointer <strong>i</strong> has reached the end of <strong>s</strong>, it means all characters of <strong>s</strong> have been found in <strong>t</strong> in the correct order, and the function returns <strong>True</strong>.</li>
    <li>If pointer <strong>i</strong> has not reached the end of <strong>s</strong>, it means <strong>s</strong> is not a subsequence of <strong>t</strong>, and the function returns <strong>False</strong>.</li>
  </ol>
</p>​
