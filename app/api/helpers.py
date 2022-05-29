import re

def validate_email(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False

def to_json(template):
    if template:
        id = str(template.get('_id'))
        template_name = template['template_name']
        subject = template['subject']
        body = template['body']
        author_id = str(template['author_id'])

        json = {
            'id': id,
            'template_name': template_name,
            'subject': subject,
            'body': body,
            'author_id': author_id}
        
        return json

def valid_template_id(template_id):
    len_tid = len(template_id)
    if (len_tid == 24): return True
    return False