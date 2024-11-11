# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings.
# >>> print a
# ['this', 'is', 'a', 'string']
# Joining a string is simple:
# >>> a = "_".join(a)
# >>> print a
# this-is-a-string
# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# Function Description
# Complete the split_and_join function in the editor below.
# split_and_join has the following parameters:
# string line: a string of space-separated words
# Returns
# string: the resulting string
# Input Format
# The one line contains a string consisting of space separated words.
# Sample Input
# this is a string
# Sample Output
# this-is-a-string

def split_and_join(s):
    space=x.split(" ")
    print(space)
    join_str="-".join(space)
    return join_str


x = "this is a string"
print(split_and_join(x))
# base=_url="https://www.pfizer.com/"
# data_url="https://www.pfizer.com/news/articles/pharma_peers_unite_to_build_dna_encoded_"
# xpath_link="//div[@class="cell medium-7 large-offset-1 lmedium-6 large-5 small-12"]"
# menu_tags="//div[@class="article-body copy-clipboard"]/h3"
# get_review="(//span[@class="wiI7pd"])[position() <= 5]"
# get_url="https://www.google.com/maps/place/Sharnbasveshwar+College+of+Science,+Gulbarga/@17.3373748,76.6448791,12z/data=!4m8!3m7!1s0x3bc8b8abeb33b44d:0xfba38b632d8471bd!8m2!3d17.3278857!4d76.8233766!9m1!1b1!16s%2Fg%2F11btz33sl_?entry=ttu&g_ep=EgoyMDI0MTAwMi4xIKXMDSoASAFQAw%3D%3D"
# get_review='(//span[@class="wiI7pd"])[position() <= 5]'
from lxml import html
import requests

# Fetch the content
url ='https://www.google.com/maps/place/Sharnbasveshwar+College+of+Science,+Gulbarga/@17.3373748,76.6448791,12z/data=!4m8!3m7!1s0x3bc8b8abeb33b44d:0xfba38b632d8471bd!8m2!3d17.3278857!4d76.8233766!9m1!1b1!16s%2Fg%2F11btz33sl_?entry=ttu&g_ep=EgoyMDI0MTAwMi4xIKXMDSoASAFQAw%3D%3D'
response = requests.get(url)
print(response)
# print(response.text)
tree = html.fromstring(response.content)

# Extract the first 5 elements
# elements = tree.xpath('//span[@class="wiI7pd"]/text()')
# elements=tree.xpath('//div[@class="MyEned"]/span/text()')
eleemnts=tree.xpath('//div[@data-review-id="ChZDSUhNMG9nS0VJQ0FnSUN5bE9pdEpBEAE"]//text()')


print(eleemnts)

# Get the text content
texts = [element.text_content() for element in eleemnts]
print(texts)














