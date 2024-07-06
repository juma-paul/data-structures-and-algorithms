​<h2>Explanation of the solution</h2>
<p>
  <ol>
    <li>Initialize two hash maps: <strong>encode_hash</strong> to store the mapping from original URLs to shortened URLs, and <strong>decode_hash</strong> to store the mapping from shortened URLs to original URLs.</li>
    <li>Set the base URL for the shortened URLs as <strong>http://tinyurl.com/</strong>.</li>
    <li>For the <strong>encode</strong> function:
      <ol>
        <li>Check if the given <strong>longUrl</strong> is already present in the <strong>encode_hash</strong>.</li>
        <li>If not, create a new shortened URL by appending the current size of <strong>encode_hash</strong> + 1 to the base URL.</li>
        <li>Store the mapping of <strong>longUrl</strong> to the new shortened URL in <strong>encode_hash</strong> and the reverse mapping in <strong>decode_hash</strong>.</li>
        <li>Return the shortened URL from <strong>encode_hash</strong>.</li>
      </ol>
    </li>
    <li>For the <strong>decode</strong> function:
      <ol>
        <li>Retrieve the original URL corresponding to the given <strong>shortUrl</strong> from <strong>decode_hash</strong>.</li>
        <li>Return the original URL.</li>
      </ol>
    </li>
  </ol>
</p>
