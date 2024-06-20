<h2>Explanation of the solution</h2>
<p>
  <ol>
    <li>Initialize three pointers: <code>i</code> at <code>m - 1</code>, <code>j</code> at <code>n - 1</code>, and <code>k</code> at <code>m + n - 1</code>.</li>
    <li>Iterate through <code>nums1</code> and <code>nums2</code> from the end towards the beginning using the pointers <code>i</code> and <code>j</code>.</li>
    <li>Compare the elements pointed to by <code>i</code> and <code>j</code>:</li>
    <ul>
      <li>If <code>nums1[i]</code> is greater than or equal to <code>nums2[j]</code>, place <code>nums1[i]</code> at position <code>k</code> in <code>nums1</code> and decrement <code>i</code>.</li>
      <li>Otherwise, place <code>nums2[j]</code> at position <code>k</code> in <code>nums1</code> and decrement <code>j</code>.</li>
      <li>Decrement <code>k</code> after each operation.</li>
    </ul>
    <li>If there are remaining elements in <code>nums2</code> (i.e., <code>j</code> is still greater than or equal to 0), copy them into <code>nums1</code> at the beginning.</li>
    <li>The merged array is now in <code>nums1</code>.</li>
  </ol>
</p>
​
