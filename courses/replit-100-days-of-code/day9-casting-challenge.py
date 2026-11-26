"""
Challenge

Generation Identifier
Which year were you born?
Hah! Millennial! Avocado toast and Starbucks much!

Year of Birth        Name
1883-1900          Lost Generation
1901-1927          Greatest Generation
1928-1945          Silent Generation
1946-1964          Baby Boomers
1965-1980          Generation X
1981-1996          Millennials
1997-2012          Generation Z
2012-Present       Generation Alpha
"""

year_born = int(input("What year were you born? "))
# if year_born>= 1883 and year_born<=1900:
if 1883 <= year_born <= 1900:
    print("Lost Generation")
elif 1901 <= year_born <= 1927:
    print("Greatest Generation")
elif 1928 <= year_born <= 1945:
    print("Silent Generation")
elif 1946 <= year_born <= 1964:
    print("Baby Boomers")
elif 1965 <= year_born <=1980:
    print("Generation X")
elif 1981 <= year_born <= 1996:
    print("Millennials")
elif 1997 <= year_born <= 2012:
    print("Generation Z")
else:
     print("Generation Alpha")

