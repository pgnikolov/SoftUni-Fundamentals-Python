import re

html_input = input()
title_pattern = r"<title>(.*?)<\/title>"
body_pattern = r"<body>(.*?)<\/body>"
title_match = re.search(title_pattern, html_input)
body_match = re.search(body_pattern, html_input)
title = title_match.group(1) if title_match else ""
content = body_match.group(1) if body_match else ""
content = re.sub(r"<.*?>", " ", content)
content = re.sub(r"\s+", " ", content)
content = content.strip()

print(f"Title: {title}")
print(f"Content: {content}")
