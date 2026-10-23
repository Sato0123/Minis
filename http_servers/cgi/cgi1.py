#! /usr/bin/env python3
import os

name = os.getenv("QUERY_STRING") or "world"

print("Content-Type: text/html")
print()
print(f"<h1>Hello, {name}!</h1>")
