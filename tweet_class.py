class ProtoTweet:
    max_char = 140
    num_likes = 0
    num_retweets = 0
    
    def __init__(self, author, body):
        self.author = author
        self.body = body

    def like(self):
        self.num_likes +=1

    def retweet(self):
        self.num_likes +=1

    def publish(self):
        if len(self.body) > self.max_char:
            overage = self.max_char - len(self.body)
            print("Tweet too long. {} characters.".format(overage))
        else:
            print(self.body)

    