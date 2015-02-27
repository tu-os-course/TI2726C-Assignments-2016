from bs4 import BeautifulSoup as BS
import sys
import os
import re
from urllib.request import *

NOT_SUBMITTED = "not submitted"
APPROVED = "approved"
SUBMITTED = "submitted"
RESUBMITTED = "resubmitted"
UNKNOWN = "unknown"

base = "https://cpm.ewi.tudelft.nl"
overview = "https://cpm.ewi.tudelft.nl/projects/projectOverview.php?projectName=TI2627_C_2015_02&studentNaming=&overviewDisplayMode=labCourse&studentSearch=&ignoreMaxMembers=1&directStatusChange="

# columns with title=deadline will get selected for downloading
deadline="Deadline: Tue 24 Feb 2015 00:00"

def parse_status(status):
  if "Not_Submitted" in status:
    return NOT_SUBMITTED
  elif "Approved" in status:
    return APPROVED
  elif "Submitted" in status:
    return SUBMITTED
  elif "Resubmitted" in status:
    return RESUBMITTED
  else:
    return UNKNOWN

def parse_overview(html, deadline):
  for tr in html.find('table', attrs={'class':'overview'}).find_all('tr')[3:]:
    student = tr\
      .find('td', {'class':'overviewLeft'})\
      .text

    student = re.sub(r"[ \-\n]{1,}", '_', student.strip(), re.M).lower()
    group, name = re.search(r"^(?:group_([0-9]+)_)?([a-zA-Z0-9]+)$", student.strip()).groups()
    if group: group = int(group)

    assignments = map(
      lambda x: (x.a.attrs.get("href"), parse_status(x.a.attrs.get("class"))),
      tr.find_all('td', title=deadline)
    )

    yield (group, name, assignments)

def get_latest_solution(page, cookie):
  r = Request(base + page, headers={'cookie':cookie})
  with urlopen(r) as p:
    content = BS(p.read())

  return parse_latest_solution(content)

def parse_latest_solution(html):
  tds = html\
    .find('form', id="reviewForm") \
    .find_all('tr')[1]\
    .find_all('td')

  return (re.sub(r'[0-9]+[:] ', '', tds[1].text).strip(), tds[-1].a.attrs.get("href"))

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("You should pass me a cookie string and a deadline string")
    sys.exit()

  cookie = sys.argv[1]
  deadline = sys.argv[2]
  if len(sys.argv) > 3:
    groups = set(map(lambda x: int(x), sys.argv[3:]))
  else:
    groups = None

  overviewcontent = urlopen(Request(overview, headers={'cookie':cookie})).read()
  html = BS(overviewcontent)

  studs = parse_overview(html, deadline)

  for (group, student, ass) in studs:
    name = (str(group) + "_" + student).lower()
    if groups and group not in groups:
      continue

    # make sure student dir exists
    try:
      os.mkdir(name)
    except IOError: pass

    # download his files
    for (page, st) in ass:
      if st == SUBMITTED or st == RESUBMITTED:
        assname, downloadlink = get_latest_solution(page, cookie)

        # download the file
        r = Request(os.path.join(base, "projects", downloadlink), headers={'cookie':cookie})
        page = urlopen(r)
        with open(os.path.join(name, assname), 'b+w') as fh:
          print("... writing " + assname + " for student " + name)
          fh.write(page.read())

