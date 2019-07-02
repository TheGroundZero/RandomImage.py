#!/usr/bin/env python3

import cgi

def get_form_values():
    form = cgi.FieldStorage()
    username = form.getfirst("username", "").lower()
    password = form.getfirst("password", "").lower()
    return (username, password)


def print_headers(user):
    print("Status: 303 See other")
    print("Content-Type: text/html")
    print("Set-Cookie: user={};path=/;max-age={}".format(user, 2*60*60))
    print("Location: /")
    print()


def print_content():
    print (
'''
<html>
<head>
<meta http-equiv="refresh" content="0;url=/" />
<title>Redirecting</title>
</head>
<body>
<p>Redirecting... Click <a href="/">here</a> if you are not redirected automatically.</p>
</body>
</html>
'''
    )


def main():
    username, password = get_form_values()
    print_headers(username)
    print_content()


if __name__ == "__main__":
    main()
