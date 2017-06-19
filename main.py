import falcon
import json
import redis

r = redis.Redis("redis")

class QuoteResource:
    def on_get(self, req, resp, postId):
        """Handles get blog post requests."""
        postId = int(postId)
        post = r.hgetall("post:{}".format(postId))
        resp.body = json.dumps(post)
        r.hincrby("post:{}".format(postId), "read", amount=1)

 
api = falcon.API()
api.add_route('/post/{postId}', QuoteResource())
