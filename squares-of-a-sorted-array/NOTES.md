<h2>Explanation of the Solution</h2><hr>
<p>We can square and then sort the array; however, it won't be the most efficient solution.</p>
<p>
  <ol>
    <li>We can do better by using two pointers since the array is already sorted.</li>
    <li>Set two pointers <strong>i</strong> and <strong>j</strong> to the first and last indices respectively.</li>
    <li>Iterate through the array from the end to the beginning.</li>
    <li>Compare the absolute values of the elements at <strong>i</strong> and <strong>j</strong>.</li>
    <li>Place the larger square value at the current position in the result array <strong>res</strong>.</li>
    <li>Increment the pointer <strong>i</strong> or decrement the pointer <strong>j</strong> based on which side had the larger absolute value.</li>
    <li>Return the result array <strong>res</strong> containing the squared values in sorted order.</li>
  </ol>
</p>