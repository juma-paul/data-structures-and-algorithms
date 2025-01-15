class Codec:
    def __init__(self):
        self.encode_hash = {}
        self.decode_hash = {}
        self.domain_url = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode_hash:
            shortUrl = self.domain_url + str(len(self.encode_hash) + 1)
            self.encode_hash[longUrl] = shortUrl
            self.decode_hash[shortUrl] = longUrl
        return self.encode_hash[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_hash[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))