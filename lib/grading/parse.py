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

def parse_overview(html):
  for tr in html.find('table', attrs={'class':'overview'}).find_all('tr')[3:]:
    student = tr\
      .find('td', {'class':'overviewLeft'})\
      .text

    student = re.sub(r"[ \-\n]{1,}", '_', student.strip(), re.M).lower()

    assignments = map(
      lambda x: (x.a.attrs.get("href"), parse_status(x.a.attrs.get("class"))),
      tr.find_all('td', title="Deadline: Tue 24 Feb 2015 00:00")
    )

    yield (student, assignments)

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
  if len(sys.argv) < 2:
    print("You should pass me a cookie string")
    sys.exit()

  cookie = sys.argv[1]

  overviewcontent = urlopen(Request(overview, headers={'cookie':cookie})).read()
  html = BS(overviewcontent)

  studs = parse_overview(html)

  for (student, ass) in studs:
    # make sure student dir exists
    try:
      os.mkdir(student)
    except IOError: pass

    # download his files
    for (page, st) in ass:
      if st == SUBMITTED or st == RESUBMITTED:
        (name, downloadlink) = get_latest_solution(page, cookie)

        # download the file
        r = Request(os.path.join(base, "projects", downloadlink), headers={'cookie':cookie})
        page = urlopen(r)
        with open(os.path.join(student, name), 'b+w') as fh:
          print("... writing " + name + " for student " + student)
          fh.write(page.read())

