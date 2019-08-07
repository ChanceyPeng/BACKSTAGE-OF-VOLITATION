def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://47.92.87.172:8000/complete/weibo/"
    auth_url = weibo_auth_url + "?client_id={client_id}&redirect_uri={re_url}".format(client_id=237999617,
                                                                                      re_url=redirect_url)

    print(auth_url)


def get_access_token(code="971408f0569897d6ec44a227857335fe"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    import requests
    re_dict = requests.post(access_token_url, data={
        "client_id": "237999617",
        "client_secret": "2c60b652a3a0c649d1bb12ab8bb86a24",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://47.92.87.172:8000/complete/weibo/"
    })
    pass


def get_user_info(access_token="", uid=""):
    user_url = "httpss://api.weibo.com/2/users/show.json?access_token{token}&uid={uid}".format(token=access_token,
                                                                                               uid=uid)
    print(user_url)


if __name__ == "__main__":
    # get_auth_url()
    # get_access_token(code="971408f0569897d6ec44a227857335fe")
    get_user_info(access_token="2.ooERyF580VZcGQ913ba86110dM5ML", uid="1272188234")
